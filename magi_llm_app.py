import asyncio
import configparser
import glob
import platform
import sys
from datetime import datetime
from pathlib import Path

from PySide6 import QtWidgets
from PySide6.QtCore import QSize, QThread, Signal, Slot
from PySide6.QtGui import QIcon, QTextCursor
from PySide6.QtWidgets import QApplication, QFileDialog

import api_fetch
from llamacpp_model_generate import LlamaCppModel
from settings_window import Ui_Settings_Dialog
from ui_magi_llm_ui import Ui_magi_llm_window


class WorkerThread(QThread):
    resultReady = Signal(str)
    final_resultReady = Signal(str)

    def __init__(self, ooba_params, ooba_server_ip, message, stream_enabled, run_backend, cpp_params):
        super().__init__()
        self.ooba_params = ooba_params
        self.ooba_server_ip = ooba_server_ip
        self.message = str(message)
        self.stream_enabled = stream_enabled
        self.run_backend = run_backend
        self.cpp_params = cpp_params

        self.stop_flag = False

    def run(self):

        if self.run_backend == 'ooba':
            self.message = self.message.strip()

            if self.stream_enabled is True:
                replies = []

                async def get_result():

                    async for response in api_fetch.run(self.message, self.ooba_params, self.ooba_server_ip):

                        # Intermediate steps
                        replies.append(response)

                        # Strip to individual tokens
                        if len(replies) > 1:
                            stripped_response = replies[1].replace(
                                replies[0], "")
                            replies.pop(0)
                            self.resultReady.emit(stripped_response)

                        if self.stop_flag:
                            break

                    # Final result
                    self.final_resultReady.emit(response)

                    # print(response)
                asyncio.run(get_result())

            else:
                response = api_fetch.textgen(
                    self.ooba_params, self.ooba_server_ip, self.message)
                self.final_resultReady.emit(response)

        if self.run_backend == 'llama.cpp':
            final_response = ''
            for response in cpp_model.generate(self.message,
                                               self.cpp_params["token_count"],
                                               self.cpp_params["temperature"],
                                               self.cpp_params["top_p"],
                                               self.cpp_params["top_k"],
                                               self.cpp_params["repetition_penalty"],
                                               ):

                if self.stream_enabled is True:
                    self.resultReady.emit(response)
                final_response += response
                final_text = self.message+final_response

                if self.stop_flag:
                    break

            # Final result
            self.final_resultReady.emit(final_text)

        # output = model.generate()[0]
        # print(output)

    def stop(self):
        # Set the stop flag to True
        self.stop_flag = True


class SettingsWindow(QtWidgets.QWidget, Ui_Settings_Dialog):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

        icon = QIcon()
        icon.addFile(str("appicon.png"),
                     QSize(), QIcon.Normal, QIcon.Off)
        self.setWindowIcon(icon)

        self.cpp_model_loaded = False

        # Ooba set settings sliders
        self.tempSlider.valueChanged.connect(
            lambda: self.tempSliderLabel.setText(str(self.tempSlider.value()/100)))
        self.top_pSlider.valueChanged.connect(
            lambda: self.top_pSliderLabel.setText(str(self.top_pSlider.value()/100)))
        self.typicalPSlider.valueChanged.connect(
            lambda: self.typicalPSliderLabel.setText(str(self.typicalPSlider.value()/100)))
        self.encoderrepSlider.valueChanged.connect(
            lambda: self.encoderrepSliderLabel.setText(str(self.encoderrepSlider.value()/100)))
        self.reppenaltySlider.valueChanged.connect(
            lambda: self.reppenaltySliderLabel.setText(str(self.reppenaltySlider.value()/100)))
        self.penaltyAlphaSlider.valueChanged.connect(
            lambda: self.penaltyAlphaSliderLabel.setText(str(self.penaltyAlphaSlider.value()/100)))
        self.lengthpenaltySlider.valueChanged.connect(
            lambda: self.lengthpenaltySliderLabel.setText(str(self.lengthpenaltySlider.value()/10)))


class ChatWindow(QtWidgets.QMainWindow, Ui_magi_llm_window):

    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.settings_win = SettingsWindow()

        # Add app icon
        icon = QIcon()
        icon.addFile(str("appicon.png"),
                     QSize(), QIcon.Normal, QIcon.Off)
        self.setWindowIcon(icon)

        # Chat presets load
        chat_presets_load = glob.glob("presets/chat/*.txt")

        for chat_preset in chat_presets_load:
            print(chat_preset)
            chat_preset_stem = Path(chat_preset).stem
            self.chatPresetComboBox.addItem(chat_preset_stem)

        # Load settings
        config = configparser.ConfigParser()
        config.read('settings.ini')
        self.cppModelPath.setText(config["Settings"]["cpp_model_path"])

        # Button clicks
        self.defaultGenerateButton.clicked.connect(
            lambda: self.textgen_switcher('default_mode'))
        self.notebookGenerateButton.clicked.connect(
            lambda: self.textgen_switcher('notebook_mode'))
        self.chatGenerateButton.clicked.connect(
            lambda: self.textgen_switcher('chat_mode'))

        self.defaultContinueButton.clicked.connect(
            lambda: self.continue_textgen('defaultContinue'))
        self.notebookContinueButton.clicked.connect(
            lambda: self.continue_textgen('notebookContinue'))
        self.chatContinueButton.clicked.connect(
            lambda: self.continue_textgen('chatContinue'))

        self.stopButton.clicked.connect(lambda: self.stop_textgen())

        self.settingsPathSaveButton.clicked.connect(
            lambda: self.save_settings())
        self.chatClearButton.clicked.connect(lambda: self.set_preset_params())

        self.cppModelSelect.clicked.connect(lambda: self.cpp_model_select())

        ###
        self.actionSettings.triggered.connect(
            lambda: self.settings_win.show())
        self.actionExit.triggered.connect(app.exit)

        self.chatPresetComboBox.currentTextChanged.connect(
            lambda: self.set_preset_params())

        # Status bar
        self.statusbar.showMessage(f"Status: Idle")

    def cpp_model_select(self):
        file_x = (QFileDialog.getOpenFileName(
            self, 'Open file', '', "GGML models (*bin)")[0])

        if len(file_x) > 0:
            self.cppModelPath.setText(file_x)

    def save_settings(self):

        config = configparser.ConfigParser()
        config.read("settings.ini")
        config.set("Settings", "cpp_model_path", self.cppModelPath.text())

        with open("settings.ini", "w") as f:
            # Write the ConfigParser object to the file
            config.write(f)
        f.close()

        print('Settings saved')

    def history_readonly_logic(self, readonly_mode):

        if textgen_mode == 'notebook_mode':
            self.notebookHistory.setReadOnly(readonly_mode)
        elif textgen_mode == 'chat_mode':
            self.chatHistory.setReadOnly(readonly_mode)

        if readonly_mode is True:
            self.chatPresetComboBox.setEnabled(False)
            self.streamEnabledCheck.setEnabled(False)

            self.defaultContinueButton.setEnabled(False)
            self.notebookContinueButton.setEnabled(False)
            self.chatContinueButton.setEnabled(False)
        else:
            self.chatPresetComboBox.setEnabled(True)
            self.streamEnabledCheck.setEnabled(True)

            self.defaultContinueButton.setEnabled(True)
            self.notebookContinueButton.setEnabled(True)
            self.chatContinueButton.setEnabled(True)

    # Continue response logic

    def stop_textgen(self):
        self.workerThread.stop()
        self.stopButton.setEnabled(False)

    def continue_textgen(self, text_tab):

        if self.oobaCheck.isEnabled() is False:
            if self.oobaCheck.isChecked() is True:
                run_backend = 'ooba'
            else:
                run_backend = 'llama.cpp'

            if text_tab == 'defaultContinue':
                self.launch_backend(
                    self.defaultTextHistory.toPlainText(), run_backend)
            elif text_tab == 'notebookContinue':
                self.launch_backend(
                    self.notebookHistory.toPlainText(), run_backend)
            elif text_tab == 'chatContinue':
                self.launch_backend(
                    self.chatHistory.toPlainText(), run_backend)

            self.history_readonly_logic(True)

    @Slot(str)
    def handleResult(self, reply):

        # Update the chat history

        if textgen_mode == 'default_mode':
            cursor = self.defaultTextHistory.textCursor()
            cursor.movePosition(QTextCursor.End)  # Move it to the end
            cursor.insertText(reply)
            self.defaultTextHistory.verticalScrollBar().setValue(
                self.defaultTextHistory.verticalScrollBar().maximum())

        elif textgen_mode == 'notebook_mode':
            cursor = self.notebookHistory.textCursor()
            cursor.movePosition(QTextCursor.End)  # Move it to the end
            cursor.insertText(reply)
            self.notebookHistory.verticalScrollBar().setValue(
                self.notebookHistory.verticalScrollBar().maximum())

        elif textgen_mode == 'chat_mode':
            cursor = self.chatHistory.textCursor()
            cursor.movePosition(QTextCursor.End)  # Move it to the end
            cursor.insertText(reply)
            self.chatHistory.verticalScrollBar().setValue(
                self.chatHistory.verticalScrollBar().maximum())

    @Slot(str)
    def final_handleResult(self, final_text):

        if self.streamEnabledCheck.isChecked() is False:
            if textgen_mode == 'default_mode':
                self.defaultTextHistory.setPlainText(final_text)
            elif textgen_mode == 'notebook_mode':
                self.notebookHistory.setPlainText(final_text)
            elif textgen_mode == 'chat_mode':
                # final_text += '\n'
                self.chatHistory.setPlainText(final_text)

        # Write chat log
        if textgen_mode == 'chat_mode' and self.logChatCheck.isChecked() == True:
            current_date = self.get_chat_date()

            with open(f"logs/chat_ooba_{current_date}.txt", "a", encoding='utf-8') as f:
                f.write('\n'+final_text)
            print('Wrote chat log')

        self.statusbar.showMessage(f"Status: Generation complete")
        self.history_readonly_logic(False)
        self.stopButton.setEnabled(False)

        self.workerThread.quit()
        self.workerThread.wait()

    def set_preset_params(self):
        current_preset = self.chatPresetComboBox.currentText()

        config = configparser.ConfigParser()
        config.read(f'presets/chat/{current_preset}.txt')
        preset_text = config["Settings"]["preset_text"].replace("\\n", "\n")

        self.chatHistory.setPlainText(f"{preset_text}\n")

    def get_llama_cpp_params(self):

        cpp_params = {
            'token_count': int(self.settings_win.maxnewtokensSlider.value()),
            'temperature': float(self.settings_win.tempSlider.value()/100),
            'top_p': float(self.settings_win.top_pSlider.value()/100),
            'top_k': int(self.settings_win.top_kSlider.value()),
            'repetition_penalty': float(self.settings_win.reppenaltySlider.value()/100),
        }

        print("llama.cpp parameters:", cpp_params)
        return cpp_params

    def get_ooba_params(self):

        ooba_server_ip = self.settings_win.oobaServerAddress.text().strip()

        ooba_params = {
            'max_new_tokens': self.settings_win.maxnewtokensSlider.value(),
            'do_sample': self.settings_win.dosampleCheck.isChecked(),
            'temperature': self.settings_win.tempSlider.value()/100,
            'top_p': self.settings_win.top_pSlider.value()/100,
            'typical_p': self.settings_win.typicalPSlider.value()/100,
            'repetition_penalty': self.settings_win.reppenaltySlider.value()/100,
            'encoder_repetition_penalty': self.settings_win.encoderrepSlider.value()/100,
            'top_k': self.settings_win.top_kSlider.value(),
            'min_length': self.settings_win.minlengthSlider.value(),
            'no_repeat_ngram_size': self.settings_win.norepeatngramSlider.value(),
            'num_beams': self.settings_win.numbeamsSlider.value(),
            'penalty_alpha': self.settings_win.penaltyAlphaSlider.value()/100,
            'length_penalty': self.settings_win.lengthpenaltySlider.value()/10,
            'early_stopping': self.settings_win.earlyStoppingCheck.isChecked(),
            'seed': -1,
            'add_bos_token': True,
            'truncation_length': 2048,
            'ban_eos_token': False,
            'skip_special_tokens': True,
            'stopping_strings': [],
        }

        print('Oobabooga parameters:', ooba_params)
        return ooba_params, ooba_server_ip

    # Get data for chat log save
    def get_chat_date(self):
        today = datetime.today()
        day = today.day
        month = today.month
        year = today.year
        return (f'{day}-{month}-{year}')

    # Set chat prefixes
    def get_chat_presets(self):
        current_preset = self.chatPresetComboBox.currentText()
        config = configparser.ConfigParser()
        config.read(f"presets/chat/{current_preset}.txt")

        # Convert the \n from settings file into new lines
        chat_user_prefix = config["Settings"]["chat_user_prefix"].replace(
            "\\n", "\n")
        bot_user_prefix = config["Settings"]["bot_user_prefix"].replace(
            "\\n", "\n")
        preset_text = config["Settings"]["preset_text"].replace(
            "\\n", "\n")

        return preset_text, chat_user_prefix, bot_user_prefix

    def load_cpp_model(self):

        params = {
            'model_path': str(self.cppModelPath.text()),
            'n_ctx': int(self.settings_win.CPP_ctxsize_Slider.value()),
            'seed': 1337,
            'n_threads': int(self.settings_win.cppThreads.text()),
            'n_batch': int(self.settings_win.cppBatchSizeSlider.value()),
            'n_ctx': int(self.settings_win.CPP_ctxsize_Slider.value())
        }

        print('Loading llama.cpp model...')
        global cpp_model
        cpp_model, tokenizer = LlamaCppModel.from_pretrained(params)

    def set_textgen_things(self):
        self.history_readonly_logic(True)
        self.cppCheck.setEnabled(False)
        self.oobaCheck.setEnabled(False)
        self.stopButton.setEnabled(True)

    def textgen_switcher(self, pre_textgen_mode):

        if self.cppCheck.isEnabled() == True and self.cppCheck.isChecked() == True:
            self.load_cpp_model()

        global textgen_mode
        textgen_mode = pre_textgen_mode

        if pre_textgen_mode == 'default_mode':
            input_message = self.defaultTextInput.toPlainText()
            if input_message:
                self.defaultTextHistory.setPlainText(input_message)
                if self.cppCheck.isChecked() == False:
                    self.launch_backend(input_message, 'ooba')
                else:
                    self.launch_backend(input_message, 'llama.cpp')

        if pre_textgen_mode == 'notebook_mode':
            input_message = self.notebookHistory.toPlainText()
            if input_message:
                if self.cppCheck.isChecked() == False:
                    self.launch_backend(input_message, 'ooba')
                else:
                    self.launch_backend(input_message, 'llama.cpp')

        if pre_textgen_mode == 'chat_mode':
            input_message = self.chatInput.toPlainText()
            if input_message:
                # Get chat prefixes
                preset_text, chat_user_prefix, bot_user_prefix = self.get_chat_presets()

                init_prompt = f"{chat_user_prefix} {input_message}{bot_user_prefix} "

                # Add custom response prefix
                if self.customResponsePrefixCheck.isChecked():
                    init_prompt = f"{chat_user_prefix} {input_message}{bot_user_prefix} {self.customResponsePrefix.text()} "

                self.chatHistory.appendPlainText(init_prompt)

                if self.cppCheck.isChecked() == False:
                    self.launch_backend(self.chatHistory.toPlainText(), 'ooba')
                else:
                    self.launch_backend(
                        self.chatHistory.toPlainText(), 'llama.cpp')

                self.chatInput.clear()

    # Oobabooga launch

    def launch_backend(self, message, run_backend):

        message = ' '+message

        ooba_params, ooba_server_ip = self.get_ooba_params()
        cpp_params = self.get_llama_cpp_params()

        self.statusbar.showMessage(f"Status: Generating...")

        self.workerThread = WorkerThread(
            ooba_params, ooba_server_ip, message, self.streamEnabledCheck.isChecked(), run_backend, cpp_params)

        # Connect signals and slots
        self.workerThread.resultReady.connect(self.handleResult)
        self.workerThread.final_resultReady.connect(self.final_handleResult)
        self.workerThread.finished.connect(self.workerThread.deleteLater)

        # Start the thread
        self.workerThread.start()
        self.set_textgen_things()


if __name__ == "__main__":
    # Create a Qt application instance
    app = QApplication(sys.argv)

    if platform.system() == 'Windows':
        app.setStyle('Fusion')

    # Create a chat window instance and show it
    window = ChatWindow()
    window.show()

    # Start the Qt event loop
    app.exec()

# todo - transformers, openai API support. TTS, chat images, character JSON imports.
