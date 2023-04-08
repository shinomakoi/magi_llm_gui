import asyncio
# import configparser
import glob
import platform
import sys
from datetime import datetime

from PySide6 import QtWidgets
from PySide6.QtCore import QSize, QThread, Signal, Slot
from PySide6.QtGui import *
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
                    # Print intermediate steps
                    # print(response)
                    self.resultReady.emit(response)

                # Print final result
                print('Final response:', response)
                self.final_resultReady.emit(response)

            asyncio.run(get_result())

        else:
            response = api_fetch.textgen(
                self.ooba_params, self.ooba_server_ip, self.message)
            print('Final response:', response)

            self.resultReady.emit(response)
            self.final_resultReady.emit(response)


class SettingsWindow(QtWidgets.QWidget, Ui_Settings_Dialog):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

        icon = QIcon()
        icon.addFile(str("appicon.png"),
                     QSize(), QIcon.Normal, QIcon.Off)
        self.setWindowIcon(icon)

        param_preset = glob.glob("presets/*.txt")

        count = 0
        for preset in param_preset:
            print(preset)
            self.paramsPresetsComboBox.addItem(preset)
            count += 1

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

        # def set_preset_params():
        #     current_preset = self.paramsPresetsComboBox.currentText()
        #     print(current_preset)

        #     config = configparser.ConfigParser()
        #     config.read(current_preset)

        #     print(config["Params"]["repetition_penalty"])
        #     repetition_penalty = float(
        #         config["Params"]["repetition_penalty"])*100
        #     (self.reppenaltySliderLabel).setText(str(repetition_penalty))
        #     self.reppenaltySlider.setValue(repetition_penalty)

        # self.paramsPresetsComboBox.currentTextChanged.connect(
        #     lambda: set_preset_params())


class ChatWindow(QtWidgets.QMainWindow, Ui_magi_llm_window):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

        self.settings_win = SettingsWindow()

        icon = QIcon()
        icon.addFile(str("appicon.png"),
                     QSize(), QIcon.Normal, QIcon.Off)
        self.setWindowIcon(icon)

        self.defaultGenerateButton.clicked.connect(
            lambda: self.textgen_switcher('default_mode'))
        self.notebookGenerateButton.clicked.connect(
            lambda: self.textgen_switcher('notebook_mode'))
        self.chatGenerateButton.clicked.connect(
            lambda: self.textgen_switcher('chat_mode'))

        self.actionSettings.triggered.connect(
            lambda: self.settings_win.show())
        self.actionExit.triggered.connect(lambda: app.quit())

        self.chatPresetComboBox.currentTextChanged.connect(
            lambda: self.chat_preset_set())

        self.statusbar.showMessage(f"Status: Idle")

    @Slot(str)
    def handleResult(self, reply):
        # Update the chat history with

        if textgen_mode == 'default_mode':
            self.defaultTextHistory.setPlainText(reply)
        elif textgen_mode == 'notebook_mode':
            self.notebookHistory.setPlainText(reply)
        elif textgen_mode == 'chat_mode':
            reply += '\n'
            self.chatHistory.setPlainText(reply)

    @Slot(str)
    def final_handleResult(self, reply):

        current_date = self.get_chat_date()
        with open(f"logs/chat_{current_date}.txt", "a", encoding='utf-8') as f:
            f.write('\n'+self.chatHistory.toPlainText())

        self.statusbar.showMessage(f"Status: Generation complete")

    def chat_preset_set(self):

        if self.chatPresetComboBox.currentText() == 'Default':
            self.chatHistory.setPlainText(
                'Assistant is a digital personal assistant to You. It is always helpful, honest, patient, nuanced, scientific, introspective, verbose, and writes responses to all inquiries thoroughly and in great detail.\n')

        elif self.chatPresetComboBox.currentText() == 'Vicuna':
            self.chatHistory.setPlainText(
                "A chat between a curious human and an artificial intelligence assistant. The assistant gives helpful, detailed, and polite answers to the human's questions.\n")

        elif self.chatPresetComboBox.currentText() == 'Alpaca':
            self.chatHistory.setPlainText(
                'Below is an instruction that describes a task. Write a response that appropriately completes the request.\n')

        elif self.chatPresetComboBox.currentText() == 'Open Assistant':
            self.chatHistory.setPlainText(
                '<|assistant|> is a digital personal assistant to <|prompter|>. It is always helpful, honest, patient, nuanced, scientific, introspective, verbose, and writes responses to all inquiries thoroughly and in great detail.\n')

        elif self.chatPresetComboBox.currentText() == 'Custom':
            self.chatHistory.clear()

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
        }
        print('Parameters:', ooba_params)
        return ooba_params, ooba_server_ip

    def get_chat_date(self):
        today = datetime.today()
        day = today.day
        month = today.month
        year = today.year
        return (f'{day}-{month}-{year}')

    def textgen_switcher(self, pre_textgen_mode):

        global textgen_mode
        textgen_mode = pre_textgen_mode

        if pre_textgen_mode == 'default_mode':
            message = self.defaultTextInput.toPlainText()
            self.launch_textgen(message)

        if pre_textgen_mode == 'notebook_mode':
            message = self.notebookHistory.toPlainText()
            self.launch_textgen(message)

        if pre_textgen_mode == 'chat_mode':
            message = self.chatInput.toPlainText()

            if self.chatPresetComboBox.currentText() == 'Vicuna':
                chat_user_prefix = '### Human: '
                bot_user_prefix = '### Assistant:'

            elif self.chatPresetComboBox.currentText() == 'Alpaca':
                chat_user_prefix = '### Instruction:\n'
                bot_user_prefix = '### Response:\n'

            elif self.chatPresetComboBox.currentText() == 'Default':
                chat_user_prefix = 'You: '
                bot_user_prefix = 'Assistant:'

            elif self.chatPresetComboBox.currentText() == 'Open Assistant':
                chat_user_prefix = '<|prompter|>'
                bot_user_prefix = '<|endoftext|><|assistant|>'

            elif self.chatPresetComboBox.currentText() == 'Custom':
                chat_user_prefix = f'{self.customChatUserPrefix.text()}: '
                bot_user_prefix = f'{self.customChatBotPrefix.text()}:'

            if self.chatPresetComboBox.currentText() == 'Open Assistant':
                self.chatHistory.append(
                    f"{chat_user_prefix}{message}{bot_user_prefix}")
            else:
                self.chatHistory.append(f"{chat_user_prefix}{message}")
                self.chatHistory.append(f"{bot_user_prefix}")

            self.chatInput.clear()
            message = self.chatHistory.toPlainText()

            self.launch_textgen(message)

    def launch_textgen(self, message):
        ooba_params, ooba_server_ip = self.get_params()
        self.statusbar.showMessage(f"Status: Generating...")

        self.workerThread = WorkerThread(
            ooba_params, ooba_server_ip, message, self.streamEnabledCheck.isChecked())
        # Connect signals and slots
        self.workerThread.resultReady.connect(self.handleResult)
        self.workerThread.final_resultReady.connect(self.final_handleResult)
        self.workerThread.finished.connect(self.workerThread.deleteLater)
        # Start the thread
        self.workerThread.start()


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
