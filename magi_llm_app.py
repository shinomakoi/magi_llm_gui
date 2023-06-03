import configparser
import csv
import glob
import platform
import sys
from datetime import datetime
from pathlib import Path

import yaml
from PySide6 import QtWidgets
from PySide6.QtCore import QSize, QThread, Signal, Slot
from PySide6.QtGui import QIcon, QTextCursor
from PySide6.QtWidgets import QApplication, QFileDialog

from api_fetch import ExllamaModel
from llamacpp_model_generate import LlamaCppModel
from settings_window import Ui_Settings_Dialog
from ui_magi_llm_ui import Ui_magi_llm_window


class textgenThread(QThread):
    resultReady = Signal(str)
    final_resultReady = Signal(str)

    def __init__(self, exllama_params, message, stream_enabled, run_backend, cpp_params):
        super().__init__()
        self.exllama_params = exllama_params
        self.message = str(message)
        self.stream_enabled = stream_enabled
        self.run_backend = run_backend
        self.cpp_params = cpp_params

        self.stop_flag = False

    def run(self):

        if self.run_backend == 'exllama':
            print('Exllama parameters:', self.exllama_params)

            self.message = self.message.strip()

            if self.stream_enabled:
                replies = []

                for response in ExllamaModel.generate_with_streaming(exllama_model, self.message, self.exllama_params):
                    # Intermediate steps
                    replies.append(response)

                    # Strip to individual tokens
                    if len(replies) > 1:
                        stripped_response = replies[1].replace(
                            replies[0], "")
                        replies.pop(0)
                        self.resultReady.emit(stripped_response)
                    else:
                        self.resultReady.emit(response)

                    if self.stop_flag:
                        break

                # Final result
                response = str(response).strip()
                self.final_resultReady.emit(response)

                # print(response)

            else:

                response = ExllamaModel.generate(
                    exllama_model, self.message, self.exllama_params)
                self.final_resultReady.emit(response)

        if self.run_backend == 'llama.cpp':
            print("llama.cpp parameters:", self.cpp_params)

            final_response = ''
            for response in cpp_model.generate(self.message,
                                               self.cpp_params["token_count"],
                                               self.cpp_params["temperature"],
                                               self.cpp_params["top_p"],
                                               self.cpp_params["top_k"],
                                               self.cpp_params["repetition_penalty"],
                                               self.cpp_params["mirostat_mode"],
                                               ):

                if self.stream_enabled:
                    self.resultReady.emit(response)
                final_response += response
                final_text = self.message+final_response

                if self.stop_flag:
                    break
            # Final result
            self.final_resultReady.emit(final_text)

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
        self.exllama_model_loaded = False

        # Ooba set settings sliders
        self.tempSlider.valueChanged.connect(
            lambda: self.tempSliderLabel.setText(str(self.tempSlider.value()/100)))
        self.top_pSlider.valueChanged.connect(
            lambda: self.top_pSliderLabel.setText(str(self.top_pSlider.value()/100)))
        self.reppenaltySlider.valueChanged.connect(
            lambda: self.reppenaltySliderLabel.setText(str(self.reppenaltySlider.value()/100)))


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
        chat_presets_load = glob.glob("presets/chat/*.yaml")
        character_presets_load = glob.glob("presets/character/*.yaml")

        for chat_preset in chat_presets_load:
            # print(chat_preset)
            chat_preset_stem = Path(chat_preset).stem
            self.chatPresetComboBox.addItem(chat_preset_stem)

        for character_preset in character_presets_load:
            # print(character_preset)
            character_preset_stem = Path(character_preset).stem
            self.characterPresetComboBox.addItem(character_preset_stem)

        filename = "presets/prompts.csv"
        with open(filename, "r",  encoding="utf-8") as csvfile:
            datareader = csv.reader(csvfile)
            for row in datareader:
                self.awesomePresetComboBox.addItem(row[0])
            self.awesomePresetComboBox.removeItem(0)
            # row is a list of values

        self.set_preset_params('chat')

        # Load settings
        config = configparser.ConfigParser()
        config.read('settings.ini')
        self.cppModelPath.setText(config["Settings"]["cpp_model_path"])
        self.exllamaModelPath.setText(config["Settings"]["exllama_model_path"])

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

        self.defaultStopButton.clicked.connect(lambda: self.stop_textgen())
        self.notebookStopButton.clicked.connect(lambda: self.stop_textgen())
        self.chatStopButton.clicked.connect(lambda: self.stop_textgen())

        self.settingsPathSaveButton.clicked.connect(
            lambda: self.save_settings())

        self.chatClearButton.clicked.connect(
            lambda: self.set_preset_params('chat'))

        self.cppModelSelect.clicked.connect(lambda: self.cpp_model_select())
        self.exllamaModelSelect.clicked.connect(
            lambda: self.exllama_model_select())

        self.chatPresetComboBox.currentTextChanged.connect(
            lambda: self.set_preset_params('chat'))
        self.characterPresetComboBox.currentTextChanged.connect(
            lambda: self.set_preset_params('character'))
        self.awesomePresetComboBox.currentTextChanged.connect(
            lambda: self.awesome_prompts())

        # Quit from menu
        self.actionSettings.triggered.connect(
            lambda: self.settings_win.show())
        self.actionExit.triggered.connect(app.exit)

        # Status bar
        self.statusbar.showMessage(f"Status: Ready")

    # Browse for the GGML model
    def cpp_model_select(self):
        file_x = (QFileDialog.getOpenFileName(
            self, 'Open file', '', "GGML models (*bin)")[0])

        if len(file_x) > 0:
            self.cppModelPath.setText(file_x)

    def exllama_model_select(self):
        file_x = str(QFileDialog.getExistingDirectory(
            self, "Select Directory"))

        if len(file_x) > 0:
            self.exllamaModelPath.setText(file_x)

    # Save any settings
    def save_settings(self):

        config = configparser.ConfigParser()
        config.read("settings.ini")
        config.set("Settings", "cpp_model_path", self.cppModelPath.text())
        config.set("Settings", "exllama_model_path",
                   self.exllamaModelPath.text())

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

        # Invert readonly_mode for buttons
        if readonly_mode:
            readonly_mode = False
        else:
            readonly_mode = True

        self.chatPresetComboBox.setEnabled(readonly_mode)
        self.characterPresetComboBox.setEnabled(readonly_mode)
        self.streamEnabledCheck.setEnabled(readonly_mode)

        self.defaultContinueButton.setEnabled(readonly_mode)
        self.notebookContinueButton.setEnabled(readonly_mode)
        self.chatContinueButton.setEnabled(readonly_mode)

        self.defaultGenerateButton.setEnabled(readonly_mode)
        self.notebookGenerateButton.setEnabled(readonly_mode)
        self.chatGenerateButton.setEnabled(readonly_mode)

        self.defaultClearButton.setEnabled(readonly_mode)
        self.notebookClearButton.setEnabled(readonly_mode)
        self.chatClearButton.setEnabled(readonly_mode)

    # Stop button logic

    def stop_textgen(self):
        self.textgenThread.stop()

        self.defaultStopButton.setEnabled(False)
        self.notebookStopButton.setEnabled(False)
        self.chatStopButton.setEnabled(False)

    # Continue button logic
    def continue_textgen(self, text_tab):

        if not self.exllamaCheck.isEnabled():
            if self.exllamaCheck.isChecked():
                run_backend = 'exllama'
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

            # reply=reply.replace(" ","&nbsp;")
            cursor.insertText(reply)

            self.chatHistory.verticalScrollBar().setValue(
                self.chatHistory.verticalScrollBar().maximum())

    # Handle the final response from textgen
    @Slot(str)
    def final_handleResult(self, final_text):

        if not self.streamEnabledCheck.isChecked():
            if textgen_mode == 'default_mode':
                self.defaultTextHistory.setPlainText(final_text)
            elif textgen_mode == 'notebook_mode':
                self.notebookHistory.setPlainText(final_text)
            elif textgen_mode == 'chat_mode':
                # final_text += '\n'
                self.chatHistory.setPlainText(final_text)

        # fix this later
        self.chatHistory.appendPlainText('\n\n')

        # Write chat log
        if textgen_mode == 'chat_mode' and self.logChatCheck.isChecked():
            current_date = self.get_chat_date()

            with open(f"logs/chat_{current_date}.txt", "a", encoding='utf-8') as f:
                f.write('\n'+final_text)
            print('Wrote chat log')

        self.statusbar.showMessage(f"Status: Generation complete")
        self.history_readonly_logic(False)

        self.defaultStopButton.setEnabled(False)
        self.notebookStopButton.setEnabled(False)
        self.chatStopButton.setEnabled(False)

        self.textgenThread.quit()
        self.textgenThread.wait()

    def get_llama_cpp_params(self):

        cpp_params = {
            'token_count': int(self.settings_win.maxnewtokensSlider.value()),
            'temperature': float(self.settings_win.tempSlider.value()/100),
            'top_p': float(self.settings_win.top_pSlider.value()/100),
            'top_k': int(self.settings_win.top_kSlider.value()),
            'repetition_penalty': float(self.settings_win.reppenaltySlider.value()/100),
            'mirostat_mode': int(self.settings_win.cppMirastatMode.value())
        }

        return cpp_params

    # Get the WebUi parameters
    def get_exllama_params(self):

        exllama_params = {
            'max_new_tokens': self.settings_win.maxnewtokensSlider.value(),
            'temperature': self.settings_win.tempSlider.value()/100,
            'top_p': self.settings_win.top_pSlider.value()/100,
            'repetition_penalty': self.settings_win.reppenaltySlider.value()/100,
            'top_k': self.settings_win.top_kSlider.value(),
            'num_beams': self.settings_win.numbeamsSlider.value(),
            'beam_length': self.settings_win.beamLengthSlider.value(),
            'min_p': self.settings_win.minPSlider.value(),
            'token_repetition_penalty_sustain': self.settings_win.token_repetition_penalty_decaySlider.value(),

            # 'seed': -1,
            # 'ban_eos_token': self.settings_win.eosTokenBanCheck.isChecked(),
            # 'skip_special_tokens': self.settings_win.skipSpecialTokensCheck.isChecked(),
            # 'stopping_strings': self.settings_win.custStopTokenLine.text()
        }

        return exllama_params

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
        preset_file = (f"presets/chat/{current_preset}.yaml")

        with open(preset_file, 'r') as file:
            chat_preset = yaml.safe_load(file)

            # print(chat_preset)

        return chat_preset

    # First load of llama.cpp model
    def load_exllama_model(self):
        global exllama_model
        exllama_model, tokenizer = ExllamaModel.from_pretrained(
            self.exllamaModelPath.text())

    def load_cpp_model(self):

        cpp_model_params = {
            'model_path': str(self.cppModelPath.text()),
            'seed': int(self.settings_win.seedValue.value()),
            'n_threads': int(self.settings_win.cppThreads.text()),
            'n_batch': int(self.settings_win.cppBatchSizeSlider.value()),
            'n_ctx': int(self.settings_win.CPP_ctxsize_Slider.value()),
            'use_mmap': bool(self.settings_win.cppMmapCheck.isChecked()),
            'use_mlock': bool(self.settings_win.cppMlockCheck.isChecked()),
        }

        if self.settings_win.gpuAccelCheck.isChecked():
            cpp_model_params["n_gpu_layers"] = self.settings_win.gpuLayersSlider.value(
            )
        if len(self.settings_win.cppLoraLineEdit.text()) > 0:
            cpp_model_params["lora_path"] = self.settings_win.cppLoraLineEdit.text()

        print('llama.cpp model load params:', cpp_model_params)
        print('Loading llama.cpp model...')

        global cpp_model
        cpp_model, tokenizer = LlamaCppModel.from_pretrained(cpp_model_params)

    def set_textgen_things(self):
        self.history_readonly_logic(True)

        self.defaultStopButton.setEnabled(True)
        self.notebookStopButton.setEnabled(True)
        self.chatStopButton.setEnabled(True)

    # Main launcher logic
    def textgen_switcher(self, pre_textgen_mode):

        if self.cppCheck.isEnabled():
            self.cppCheck.setEnabled(False)
            self.exllamaCheck.setEnabled(False)

            if self.cppCheck.isChecked():
                self.load_cpp_model()
            else:
                self.load_exllama_model()

        global textgen_mode
        textgen_mode = pre_textgen_mode

        if pre_textgen_mode == 'default_mode':
            input_message = self.defaultTextInput.toPlainText()
            if input_message:
                self.defaultTextHistory.setPlainText(input_message)
                if not self.cppCheck.isChecked():
                    self.launch_backend(input_message, 'exllama')
                else:
                    self.launch_backend(input_message, 'llama.cpp')

        if pre_textgen_mode == 'notebook_mode':
            input_message = self.notebookHistory.toPlainText()
            if input_message:
                if not self.cppCheck.isChecked():
                    self.launch_backend(input_message, 'exllama')
                else:
                    self.launch_backend(input_message, 'llama.cpp')

        if pre_textgen_mode == 'chat_mode':
            input_message = self.chatInput.toPlainText()

            if input_message:
                final_prompt = self.prompt_generation(pre_textgen_mode)
                self.chatHistory.setPlainText(final_prompt)

                if self.cppCheck.isChecked() == False:
                    self.launch_backend(final_prompt, 'exllama')
                else:
                    self.launch_backend(final_prompt, 'llama.cpp')

                self.chatInput.clear()

    # Launch QThread to textgen
    def launch_backend(self, message, run_backend):

        exllama_params = self.get_exllama_params()
        cpp_params = self.get_llama_cpp_params()

        self.statusbar.showMessage(f"Status: Generating...")

        self.textgenThread = textgenThread(
            exllama_params, message, self.streamEnabledCheck.isChecked(), run_backend, cpp_params)

        # Connect signals and slots
        self.textgenThread.resultReady.connect(self.handleResult)
        self.textgenThread.final_resultReady.connect(self.final_handleResult)
        self.textgenThread.finished.connect(self.textgenThread.deleteLater)

        # Start the thread
        self.textgenThread.start()
        self.set_textgen_things()

    def prompt_generation(self, pre_textgen_mode):

        # if pre_textgen_mode == 'default_mode':

        # if pre_textgen_mode == 'notebook_mode':

        if pre_textgen_mode == 'chat_mode':
            if self.instructRadioButton.isChecked():

                chat_preset = self.get_chat_presets()

                final_prompt = chat_preset["turn_template"]\
                    .replace("<|user|>", chat_preset["user"])\
                    .replace("<|user-message|>", self.chatInput.toPlainText())\
                    .replace("<|bot|>", chat_preset["bot"])

                # fix this later
                final_prompt = final_prompt.replace(
                    "<|bot-message|>", "").strip()
                final_prompt = (
                    f"{self.chatHistory.toPlainText()}{final_prompt}")

            else:
                chat_user_prefix = self.yourNameLine.text()+': '
                bot_user_prefix = self.characterPresetComboBox.currentText()+': '

                final_prompt = (f"""{self.chatHistory.toPlainText()}{chat_user_prefix}
{self.chatInput.toPlainText()}
{bot_user_prefix}""")

        if self.customResponsePrefixCheck.isChecked():
            final_prompt += ' '+self.customResponsePrefix.text()
        return final_prompt

    # Get chat presets from files
    def set_preset_params(self, preset_mode):

        if preset_mode == 'chat':
            self.instructRadioButton.setChecked(True)

            chat_preset = self.get_chat_presets()
            self.chatHistory.setPlainText(chat_preset["context"])

        elif preset_mode == 'character':
            self.charactersRadioButton.setChecked(True)
            current_preset = self.characterPresetComboBox.currentText()
            preset_file = (f"presets/character/{current_preset}.yaml")

            with open(preset_file, 'r') as file:
                self.chatHistory.clear()
                character_preset = yaml.safe_load(file)

                for x in character_preset:
                    value = character_preset[x]
                    # final = f"{x.capitalize()}: {value}"
                    value = value.replace(r"{{char}}", character_preset["name"]).replace(
                        r"{{user}}", self.yourNameLine.text())
                    self.chatHistory.appendPlainText(f"{value}\n")

    def awesome_prompts(self):

        filename = "presets/prompts.csv"
        with open(filename, "r",  encoding="utf-8") as csvfile:
            datareader = csv.reader(csvfile)
            for row in datareader:
                if row[0] == self.awesomePresetComboBox.currentText():
                    self.chatInput.setPlainText(row[1])
                    break


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
