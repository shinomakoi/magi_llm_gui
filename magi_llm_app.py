import asyncio
import configparser
import glob
import platform
import sys
from datetime import datetime
from pathlib import Path

from PySide6 import QtWidgets
from PySide6.QtCore import QProcess, QSize, QThread, Signal, Slot
from PySide6.QtGui import QIcon, QTextCursor
from PySide6.QtWidgets import QApplication

import api_fetch
from settings_window import Ui_Settings_Dialog
from ui_magi_llm_ui import Ui_magi_llm_window


class WorkerThread(QThread):
    resultReady = Signal(str)
    final_resultReady = Signal(str)

    def __init__(self, ooba_params, ooba_server_ip, message, stream_enabled):
        super().__init__()
        self.ooba_params = ooba_params
        self.ooba_server_ip = ooba_server_ip
        self.message = message
        self.stream_enabled = stream_enabled

    def run(self):
        if self.stream_enabled is True:

            async def get_result():
                async for response in api_fetch.run(self.message, self.ooba_params, self.ooba_server_ip):
                    # Intermediate steps
                    self.resultReady.emit(response)

                # Final result
                self.final_resultReady.emit(response)
            asyncio.run(get_result())

        else:
            response = api_fetch.textgen(
                self.ooba_params, self.ooba_server_ip, self.message)

            self.final_resultReady.emit(response)


class SettingsWindow(QtWidgets.QWidget, Ui_Settings_Dialog):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

        icon = QIcon()
        icon.addFile(str("appicon.png"),
                     QSize(), QIcon.Normal, QIcon.Off)
        self.setWindowIcon(icon)

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

        self.llamacpp_process = None

        # Chat presets load
        chat_presets_load = glob.glob("presets/chat/*.txt")

        for chat_preset in chat_presets_load:
            print(chat_preset)
            chat_preset_stem = Path(chat_preset).stem
            self.chatPresetComboBox.addItem(chat_preset_stem)

        # Load settings
        config = configparser.ConfigParser()
        config.read('settings.ini')
        self.cppBinaryPath.setText(config["Settings"]["cpp_binary_path"])
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

        self.settingsPathSaveButton.clicked.connect(
            lambda: self.save_settings())
        self.chatClearButton.clicked.connect(lambda: self.set_preset_params())

        self.actionSettings.triggered.connect(
            lambda: self.settings_win.show())
        self.actionExit.triggered.connect(app.exit)
        self.stopButton.clicked.connect(self.stop_logic)

        self.chatPresetComboBox.currentTextChanged.connect(
            lambda: self.set_preset_params())

        # Status bar
        self.statusbar.showMessage(f"Status: Idle")

    def save_settings(self):

        config = configparser.ConfigParser()
        config.read("settings.ini")
        config.set("Settings", "cpp_binary_path", self.cppBinaryPath.text())
        config.set("Settings", "cpp_model_path", self.cppModelPath.text())

        with open("settings.ini", "w") as f:
            # Write the ConfigParser object to the file
            config.write(f)
        f.close()

        print('Settings saved')

    def stop_logic(self):
        print('llama.cpp: Stopped')
        if self.llamacpp_process:
            self.llamacpp_process_terminate()

    def history_readonly_logic(self, readonly_mode):

        if textgen_mode == 'notebook_mode':
            self.notebookHistory.setReadOnly(readonly_mode)
        elif textgen_mode == 'chat_mode':
            self.chatHistory.setReadOnly(readonly_mode)

    # Continue response logic
    def continue_textgen(self, text_tab):

        self.history_readonly_logic(True)

        if self.cppCheck.isChecked() == False:
            if text_tab == 'defaultContinue':
                self.launch_ooba(
                    self.defaultTextHistory.toPlainText())
            elif text_tab == 'notebookContinue':
                self.launch_ooba(
                    self.notebookHistory.toPlainText())
            elif text_tab == 'chatContinue':
                self.launch_ooba(self.chatHistory.toMarkdown())

        elif self.llamacpp_process is None:
            if text_tab == 'defaultContinue':
                self.launch_llama_cpp(
                    self.defaultTextHistory.toPlainText())
            elif text_tab == 'notebookContinue':
                self.launch_llama_cpp(
                    self.notebookHistory.toPlainText())
            elif text_tab == 'chatContinue':
                self.launch_llama_cpp(self.chatHistory.toMarkdown())

    @Slot(str)
    def handleResult(self, reply):

        # Update the chat history
        if textgen_mode == 'default_mode':
            self.defaultTextHistory.setPlainText(reply)
        elif textgen_mode == 'notebook_mode':
            self.notebookHistory.setPlainText(reply)
        elif textgen_mode == 'chat_mode':
            self.chatHistory.setMarkdown(reply)

    @Slot(str)
    def final_handleResult(self, reply):

        if textgen_mode == 'default_mode':
            self.defaultTextHistory.setPlainText(reply)
        elif textgen_mode == 'notebook_mode':
            self.notebookHistory.setPlainText(reply)
        elif textgen_mode == 'chat_mode':
            reply += '\n'
            self.chatHistory.setMarkdown(reply)
            self.chatHistory.scroll

        if textgen_mode == 'chat_mode' and self.logChatCheck.isChecked() == True:
            current_date = self.get_chat_date()
            with open(f"logs/chat_ooba_{current_date}.txt", "a", encoding='utf-8') as f:
                f.write('\n'+self.chatHistory.toPlainText())

        print('Wrote Ooba chat log')

        self.statusbar.showMessage(f"Oobabooga: Generation complete")
        self.history_readonly_logic(False)

    def set_preset_params(self):
        current_preset = self.chatPresetComboBox.currentText()

        config = configparser.ConfigParser()
        config.read(f'presets/chat/{current_preset}.txt')
        preset_text = config["Settings"]["preset_text"].replace("\\n", "\n")

        self.chatHistory.setMarkdown(f"{preset_text}\n")
        self.chatHistory.setFontWeight

    def get_params(self):

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
            'seed': self.settings_win.seedValue.value(),
            'add_bos_token': True,
            'custom_stopping_strings': [],
            'truncation_length': 2048,
            'ban_eos_token': False,
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

        return chat_user_prefix, bot_user_prefix

    def textgen_switcher(self, pre_textgen_mode):

        global textgen_mode
        textgen_mode = pre_textgen_mode

        def set_textgen_things():
            self.history_readonly_logic(True)
            self.cppCheck.setEnabled(False)
            self.oobaCheck.setEnabled(False)

        if self.cppCheck.isChecked() == True and self.llamacpp_process and pre_textgen_mode == 'chat_mode':

            chat_user_prefix, bot_user_prefix = self.get_chat_presets()

            print('llama.cpp: Write mode')
            self.chatHistory.append(self.chatInput.toPlainText())
            self.chatHistory.append(f"\n{bot_user_prefix} ")
            self.llamacpp_process.write(
                f"{self.chatInput.toPlainText()}\n{bot_user_prefix}".encode())
            return

        if pre_textgen_mode == 'default_mode':
            message = self.defaultTextInput.toPlainText()
            if message:
                if self.cppCheck.isChecked() == False:
                    self.launch_ooba(message)
                elif self.llamacpp_process is None:
                    self.launch_llama_cpp(message)
                set_textgen_things()

        if pre_textgen_mode == 'notebook_mode':
            
            message = self.notebookHistory.toPlainText()
            if message:
                if self.cppCheck.isChecked() == False:
                    self.launch_ooba(message)
                elif self.llamacpp_process is None:
                    self.launch_llama_cpp(message)
                set_textgen_things()

        if pre_textgen_mode == 'chat_mode':

            message = self.chatInput.toPlainText()
            if message:
                # Get chat prefixes
                chat_user_prefix, bot_user_prefix = self.get_chat_presets()

                self.chatHistory.setMarkdown(
                    f"{self.chatHistory.toMarkdown()}{chat_user_prefix} {message}\n{bot_user_prefix}")

                # Add custom response prefix
                if self.customResponsePrefixCheck.isChecked():
                    self.chatHistory.append(self.customResponsePrefix.text())

                final_prompt = self.chatHistory.toMarkdown()

                if self.cppCheck.isChecked() == False:
                    self.launch_ooba(final_prompt)
                elif self.llamacpp_process is None:
                    self.notebook_textgenTab.setEnabled(False)
                    self.default_textgenTab.setEnabled(False)

                    self.launch_llama_cpp(final_prompt)

                set_textgen_things()
                self.chatInput.clear()

    # Oobabooga launch
    def launch_ooba(self, message):
        ooba_params, ooba_server_ip = self.get_params()
        self.statusbar.showMessage(f"Oobabooga: Generating...")

        self.workerThread = WorkerThread(
            ooba_params, ooba_server_ip, message, self.streamEnabledCheck.isChecked())

        # Connect signals and slots
        self.workerThread.resultReady.connect(self.handleResult)
        self.workerThread.final_resultReady.connect(self.final_handleResult)
        self.workerThread.finished.connect(self.workerThread.deleteLater)

        # Start the thread
        self.workerThread.start()

    def handleOutput(self):

        if self.llamacpp_process:
            output = self.llamacpp_process.readAllStandardOutput().data().decode()

            # Get the current cursor of the QPlainTextEdit
            if textgen_mode == 'default_mode':
                cursor = self.defaultTextHistory.textCursor()
            elif textgen_mode == 'notebook_mode':
                cursor = self.notebookHistory.textCursor()
            elif textgen_mode == 'chat_mode':
                cursor = self.chatHistory.textCursor()

            cursor.movePosition(QTextCursor.End)  # Move it to the end
            # Insert the text at the current position
            cursor.insertText(output)

    def launch_llama_cpp(self, message):
        print('llama.cpp: Start')

        llama_cpp_args = [
            '-m', self.cppModelPath.text(),
            '-t', self.settings_win.cppThreads.text(),
            '--n_predict', str(self.settings_win.maxnewtokensSlider.value()),
            '--top_k', str(self.settings_win.top_kSlider.value()),
            '--top_p', str(self.settings_win.top_pSlider.value()/100),
            '--repeat_last_n', str(
                self.settings_win.CPP_repeat_last_nSlider.value()),
            '--repeat_penalty', str(
                self.settings_win.reppenaltySlider.value()/100),
            '--ctx_size', str(self.settings_win.CPP_ctxsize_Slider.value()),
            '--temp', str(self.settings_win.tempSlider.value()/100),
            '--batch_size', str(self.settings_win.cppBatchSizeSlider.value()),
            '-p', message
        ]

        if textgen_mode == "chat_mode":
            chat_user_prefix, bot_user_prefix = self.get_chat_presets()
            llama_cpp_args.append("-i")
            llama_cpp_args.append("-r")
            llama_cpp_args.append(chat_user_prefix)

        print('llama_cpp_args:', llama_cpp_args)

        self.llamacpp_process = QProcess(self)
        self.llamacpp_process.readyReadStandardOutput.connect(
            self.handleOutput)
        self.llamacpp_process.finished.connect(
            self.llamacpp_process_finished)

        self.llamacpp_process.start(
            self.cppBinaryPath.text(), llama_cpp_args)

        if textgen_mode == 'default_mode':
            self.defaultTextHistory.clear()
        if textgen_mode == 'notebook_mode':
            self.notebookHistory.clear()
        if textgen_mode == 'chat_mode':
            self.chatHistory.clear()

        self.statusbar.showMessage(f"llama.cpp: Generating...")

    def llamacpp_process_terminate(self):
        if self.llamacpp_process:
            self.llamacpp_process.terminate()
            print('llama.cpp: Stopped')
            self.statusbar.showMessage(f"llama.cpp: Stopped")

            self.llamacpp_process_finished()

    def llamacpp_process_finished(self):
        current_date = self.get_chat_date()

        if textgen_mode == 'chat_mode' and self.logChatCheck.isChecked() == True:
            with open(f"logs/chat_lcpp_{current_date}.txt", "a", encoding='utf-8') as f:
                f.write('\n'+self.chatHistory.toPlainText())
            print('Wrote llama.cpp chat log')

        self.llamacpp_process = None
        print('llama.cpp: Finished')
        self.statusbar.showMessage(f"llama.cpp: Finished")

        if self.notebook_textgenTab.isEnabled() is False:
            self.notebook_textgenTab.setEnabled(True)
            self.default_textgenTab.setEnabled(True)

        self.history_readonly_logic(False)


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
