import configparser
import csv
import glob
import json
import platform
import sys
from datetime import datetime
from functools import partial
from pathlib import Path

import requests
import yaml
from PySide6 import QtWidgets
from PySide6.QtCore import QSize, QThread, Signal, Slot
from PySide6.QtGui import QIcon, QTextCursor
from PySide6.QtWidgets import QApplication, QFileDialog
from qt_material import apply_stylesheet

from llama_tokenize import Tokenizer
from settings_window import Ui_Settings_Dialog
from ui_magi_llm_ui import Ui_magi_llm_window

# Constants for the directories and file names
APP_ICON = Path("assets/icons/appicon.png")
CHAT_PRESETS_DIR = Path("presets/instruct")
CHARACTER_PRESETS_DIR = Path("presets/character")
PROMPTS_FILE = Path("presets/prompts.csv")
SETTINGS_FILE = Path("settings.ini")

# Use constants for the backend names
EXLLAMA = "exllama"
LLAMA_CPP = "llama.cpp"
LLAMA_CPP_SERVER = "llama.cpp_server"
TS_SERVER = "ts-server"
RWKV_CPP = "rwkv.cpp"


# A class to run text generation in a separate thread.
class TextgenThread(QThread):

    resultReady = Signal(str)
    final_resultReady = Signal(str)

    def __init__(
        self,
        exllama_params: dict,
        message: str,
        stream_enabled: bool,
        run_backend: str,
        cpp_params: dict,
        ts_model: str,
    ):
        super().__init__()
        self.exllama_params = exllama_params
        self.message = message
        self.stream_enabled = stream_enabled
        self.run_backend = run_backend
        self.cpp_params = cpp_params
        self.ts_model = ts_model

        self.stop_flag = False

    def run(self):
        # Use a dictionary to dispatch the backend methods
        backend_methods = {
            EXLLAMA: self.run_exllama,
            LLAMA_CPP: self.run_llama_cpp,
            LLAMA_CPP_SERVER: self.run_llama_cpp_server,
            TS_SERVER: self.run_ts_server,
            RWKV_CPP: self.run_rwkv_cpp,
        }

        # Call the appropriate method based on the run_backend attribute
        backend_method = backend_methods.get(self.run_backend)
        if backend_method:
            try:
                backend_method()
            except Exception as error:
                self.final_resultReady.emit('')
                print('--- Error running backend:\n', error)
                return

        else:
            raise ValueError(f"Invalid run_backend: {self.run_backend}")

    def run_exllama(self):
        # Use a generator expression to iterate over the responses
        responses = exllama_model.generate_with_streaming(
            self.message, self.exllama_params)

        # Use a variable to store the previous response
        final_response = ''
        for response in responses:
            final_response += response
            if self.stop_flag:
                break

            # Emit the stripped response as resultReady signal
            if self.stream_enabled:
                self.resultReady.emit(response)
        if not self.stream_enabled:
            self.resultReady.emit(final_response)

        # Emit the final response as final_resultReady signal
        self.final_resultReady.emit(final_response)

    def run_llama_cpp(self):
        # Use keyword arguments to pass the cpp_params to the model methods
        kwargs = {
            "max_tokens": self.cpp_params["max_new_tokens"],
            "temperature": self.cpp_params["temperature"],
            "top_p": self.cpp_params["top_p"],
            "top_k": self.cpp_params["top_k"],
            "repeat_penalty": self.cpp_params["repetition_penalty"],
            "mirostat_mode": self.cpp_params["mirostat_mode"],
            "stop": self.cpp_params["stop"],
            "tfs_z": self.cpp_params["tfs_z"],
            "frequency_penalty": self.cpp_params["frequency_penalty"],
            "presence_penalty": self.cpp_params["presence_penalty"],
        }

        # Use a generator expression to iterate over the responses
        responses = cpp_model.generate_with_streaming(
            self.message, **kwargs
        ) if self.stream_enabled else [cpp_model.generate(self.message, **kwargs)]

        # Use a list to store the responses and join them at the end
        response_list = []
        for response in responses:
            if self.stop_flag:
                break
            # Emit the response as resultReady signal
            self.resultReady.emit(response)
            # Append the response to the list
            response_list.append(response)

        # Join the message and the responses and emit as final_resultReady signal
        final_text = f"{''.join(response_list)}"
        self.final_resultReady.emit(final_text)

    """Run the llama.cpp server and generate a response.
    Emits signals with the results.
    """

    def run_llama_cpp_server(self):
        import llamacpp_server_generate

        final_text = ""
        if self.stream_enabled:
            # Generate a response with streaming
            for response in llamacpp_server_generate.generate_with_streaming(
                self.message, self.cpp_params
            ):
                if self.stop_flag:
                    break
                final_text += response
                self.resultReady.emit(response)
        else:
            # Generate a response without streaming
            final_text = llamacpp_server_generate.generate_nostream(
                self.message, self.cpp_params
            )
            self.resultReady.emit(final_text)

        # Emit the final result
        self.final_resultReady.emit(final_text)

    def run_ts_server(self):
        ts_args = {
            "prompt": self.message,
            "max_tokens": self.cpp_params["max_new_tokens"],
            "temperature": self.cpp_params["temperature"],
            "top_p": self.cpp_params["top_p"],
            "top_k": self.cpp_params["top_k"],
            "repetition_penalty": self.cpp_params["repetition_penalty"],
            "stop": self.cpp_params["stop"],
        }

        # Set the URL
        url = f"http://localhost:8080/v1/engines/{self.ts_model}/completions"
        # Set the headers
        headers = {"Content-Type": "application/json"}
        # Set the data
        data = ts_args
        # Make a post request and get the response
        response = requests.post(url, headers=headers, json=data)
        # Decode the bytes to a string using utf-8 encoding
        response_str = response.content.decode("utf-8")
        # Load the string as a json object
        response_json = json.loads(response_str)
        # Get the "text" value from the json object
        final_text = response_json["text"]

        self.resultReady.emit(final_text)
        self.final_resultReady.emit(final_text)

    def run_rwkv_cpp(self):

        rwkv_params = {
            "max_tokens": self.cpp_params["max_new_tokens"],
            "temperature": self.cpp_params["temperature"],
            "top_p": self.cpp_params["top_p"],
            "repetition_penalty": self.cpp_params["repetition_penalty"],
            "stop": self.cpp_params["stop"],
        }

        import rwkvcpp_generate
        final_text = ""
        for response in rwkvcpp_generate.generate(self.message, rwkv_cpp_model, rwkv_params):
            if self.stop_flag:
                break
            final_text += response
            self.resultReady.emit(response)
        self.final_resultReady.emit(final_text)

    def stop(self):
        """Set the stop flag to True."""
        self.stop_flag = True


class SettingsWindow(QtWidgets.QWidget, Ui_Settings_Dialog):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

        print('--- Launched app')

        # Set the window icon
        icon = QIcon()
        icon.addFile(str(APP_ICON), QSize(), QIcon.Normal, QIcon.Off)
        self.setWindowIcon(icon)

        # Initialize flags for whether the models are loaded or not
        self.cpp_model_loaded = False
        self.exllama_model_loaded = False

        # Connect the settings sliders to the spin boxes
        self.temperatureSlider.valueChanged.connect(
            lambda: self.temperatureSpin.setValue(
                self.temperatureSlider.value() / 100)
        )
        self.top_pSlider.valueChanged.connect(
            lambda: self.top_pSpin.setValue(self.top_pSlider.value() / 100)
        )
        self.repetition_penaltySlider.valueChanged.connect(
            lambda: self.repetition_penaltySpin.setValue(
                self.repetition_penaltySlider.value() / 100
            )
        )
        self.cpp_tfszSlider.valueChanged.connect(
            lambda: self.cpp_tfszSpin.setValue(
                self.cpp_tfszSlider.value() / 100
            )
        )
        self.freqPenaltySlider.valueChanged.connect(
            lambda: self.freqPenaltySpin.setValue(
                self.freqPenaltySlider.value() / 100
            )
        )
        self.presencePenaltySlider.valueChanged.connect(
            lambda: self.presencePenaltySpin.setValue(
                self.presencePenaltySlider.value() / 100
            )
        )

        # Connect the spin boxes to the settings sliders
        self.temperatureSpin.valueChanged.connect(
            lambda: self.temperatureSlider.setValue(
                self.temperatureSpin.value() * 100)
        )
        self.top_pSpin.valueChanged.connect(
            lambda: self.top_pSlider.setValue(self.top_pSpin.value() * 100)
        )
        self.repetition_penaltySpin.valueChanged.connect(
            lambda: self.repetition_penaltySlider.setValue(
                self.repetition_penaltySpin.value() * 100
            )
        )
        self.cpp_tfszSpin.valueChanged.connect(
            lambda: self.cpp_tfszSlider.setValue(
                self.cpp_tfszSpin.value() * 100
            )
        )
        self.freqPenaltySpin.valueChanged.connect(
            lambda: self.freqPenaltySlider.setValue(
                self.freqPenaltySpin.value() * 100
            )
        )
        self.presencePenaltySpin.valueChanged.connect(
            lambda: self.presencePenaltySlider.setValue(
                self.presencePenaltySpin.value() * 100
            )
        )
        # Define a function to load parameters presets

        def load_params():
            param_preset_load = glob.glob("presets/model_params/*.yaml")
            # sort the list of files alphabetically
            param_preset_load = sorted(param_preset_load)
            for param_preset in param_preset_load:
                param_preset_stem = Path(param_preset).stem
                self.paramPresets_comboBox.addItem(
                    param_preset_stem)

            # Set the default preset to Magi-Default
            self.paramPresets_comboBox.setCurrentText("Magi-Default")

        # Call the function to load parameters presets
        load_params()

        def set_params():
            # Load and set parameters
            config = configparser.ConfigParser()
            config.read('settings.ini')

            ### Define params ###
            # Params-Shared
            temperature = config["Params-Shared"]["temperature"]
            top_k = config["Params-Shared"]["top_k"]
            top_p = config["Params-Shared"]["top_p"]
            max_new_tokens = config["Params-Shared"]["max_new_tokens"]
            repetition_penalty = config["Params-Shared"]["repetition_penalty"]
            seed = config["Params-Shared"]["seed"]

            # Params-Exllama
            min_p = config["Params-Exllama"]["min_p"]
            token_repetition_penalty_decay = config["Params-Exllama"]["token_repetition_penalty_decay"]
            num_beams = config["Params-Exllama"]["num_beams"]
            beam_length = config["Params-Exllama"]["beam_length"]

            gpu_split = config["Params-Exllama"]["gpu_split"]
            gpu_split_values = config["Params-Exllama"]["gpu_split_values"]

            # Params-LlamaCPP
            threads = config["Params-LlamaCPP"]["threads"]
            context_size = config["Params-LlamaCPP"]["context_size"]
            tfs_z = config["Params-LlamaCPP"]["tfs_z"]
            batch_size = config["Params-LlamaCPP"]["batch_size"]
            mirostat_mode = config["Params-LlamaCPP"]["mirostat_mode"]
            n_gpu_layers = config["Params-LlamaCPP"]["n_gpu_layers"]
            lora_path = config["Params-LlamaCPP"]["lora_path"]
            frequency_penalty = config["Params-LlamaCPP"]["frequency_penalty"]
            presence_penalty = config["Params-LlamaCPP"]["presence_penalty"]

            use_mmap = config["Params-LlamaCPP"]["use_mmap"]
            use_mlock = config["Params-LlamaCPP"]["use_mlock"]
            use_gpu_accel = config["Params-LlamaCPP"]["use_gpu_accel"]
            use_cache = config["Params-LlamaCPP"]["use_cache"]
            use_verbose = config["Params-LlamaCPP"]["use_verbose"]

            # Params-TextSynth
            ts_model = config["Params-TextSynth"]["ts_model"]

            ### Set params ###
            # Params-Shared
            self.temperatureSpin.setValue(float(temperature))
            self.temperatureSlider.setValue(int(float(temperature)*100))

            self.top_kSpin.setValue(int(top_k))
            self.top_kSlider.setValue(int(top_k))

            self.top_pSpin.setValue(float(top_p))
            self.top_pSlider.setValue(int(float(top_p)*100))

            self.max_new_tokensSpin.setValue(int(max_new_tokens))
            self.max_new_tokensSlider.setValue(int(max_new_tokens))

            self.repetition_penaltySpin.setValue(float(repetition_penalty))
            self.repetition_penaltySlider.setValue(
                int(float(repetition_penalty)*100))

            self.seedSpin.setValue(int(seed))

            # Params-Exllama
            self.minPSpin.setValue(float(min_p))
            self.minPSlider.setValue(int(min_p))

            self.token_repetition_penalty_decaySpin.setValue(
                int(token_repetition_penalty_decay))
            self.token_repetition_penalty_decaySlider.setValue(
                int(token_repetition_penalty_decay))

            self.numbeamsSpin.setValue(int(num_beams))
            self.numbeamsSlider.setValue(int(num_beams))

            self.beamLengthSpin.setValue(int(beam_length))
            self.beamLengthSlider.setValue(int(beam_length))

            self.exllamaGpuSplitCheck.setChecked(eval(gpu_split))
            self.exllamaGpuSplitLine.setText((gpu_split_values))

            # Params-LlamaCPP
            self.cppThreads.setValue(int(threads))

            self.CPP_ctxsize_Spin.setValue(int(context_size))
            self.CPP_ctxsize_Slider.setValue(int(context_size))

            self.cpp_tfszSpin.setValue(float(tfs_z))
            self.cpp_tfszSlider.setValue(int(float(tfs_z)*100))

            self.cppBatchSizeSpin.setValue(int(batch_size))
            self.cppBatchSizeSlider.setValue(int(batch_size))

            self.gpuLayersSpin.setValue(int(n_gpu_layers))
            self.gpuLayersSlider.setValue(int(n_gpu_layers))

            self.cppLoraLineEdit.setText(str(lora_path))
            self.cppMirastatMode.setValue(int(mirostat_mode))

            self.freqPenaltySpin.setValue(float(frequency_penalty))
            self.freqPenaltySlider.setValue(float(frequency_penalty))

            self.presencePenaltySpin.setValue(float(presence_penalty))
            self.presencePenaltySlider.setValue(float(presence_penalty))

            self.cppMmapCheck.setChecked(eval(use_mmap))
            self.cppMlockCheck.setChecked((eval(use_mlock)))
            self.gpuAccelCheck.setChecked(eval(use_gpu_accel))

            self.cppCacheCheck.setChecked(eval(use_cache))
            self.cppVerboseCheck.setChecked(eval(use_verbose))

            # Params-TextSynth

            self.tsModelLine.setText(str(ts_model))

        set_params()
        # Define a function to apply parameters presets

        def apply_params_preset():

            # Get the current preset from the combo box
            current_preset = self.paramPresets_comboBox.currentText()
            # Construct the file name for the preset
            preset_file = f"presets/model_params/{current_preset}.yaml"

            # Open the file and load the parameters as a dictionary
            with open(preset_file, "r") as file:
                param_preset_name = yaml.safe_load(file)

            # Set the values of the spin boxes and sliders according to the parameters
            self.top_pSpin.setValue(float(param_preset_name["top_p"]))
            self.top_pSlider.setValue(int(param_preset_name["top_p"] * 100))
            self.top_kSpin.setValue(int(param_preset_name["top_k"]))
            self.top_kSlider.setValue(int(param_preset_name["top_k"]))
            self.temperatureSpin.setValue(
                float(param_preset_name["temperature"]))
            self.temperatureSlider.setValue(
                int(param_preset_name["temperature"] * 100))
            self.repetition_penaltySpin.setValue(
                float(param_preset_name["repetition_penalty"]))
            self.repetition_penaltySlider.setValue(
                int(param_preset_name["repetition_penalty"] * 100)
            )

            # Print a message indicating which preset was applied
            print("--- Applied parameter preset:", Path(preset_file).stem)

        # Connect the function to the combo box signal
        self.paramPresets_comboBox.textActivated.connect(
            lambda: apply_params_preset())


class ChatWindow(QtWidgets.QMainWindow, Ui_magi_llm_window):

    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.settings_win = SettingsWindow()

        icon = QIcon()
        icon.addFile(str(APP_ICON), QSize(), QIcon.Normal, QIcon.Off)
        self.setWindowIcon(icon)

        self.model_load = False
        self.continue_textgen_mode = False
        self.textgen_mode = 'chat_mode'

        # Load chat presets
        self.load_presets(CHAT_PRESETS_DIR, self.instructPresetComboBox)
        # Load character presets
        self.load_presets(CHARACTER_PRESETS_DIR, self.characterPresetComboBox)
        # Load awesome prompts
        self.load_prompts(PROMPTS_FILE)
        # Load settings
        self.load_settings(SETTINGS_FILE)

        self.name_history = []
        self.message_history = []
        self.chat_output_list = []

        self.chat_input_history = []

        # Quit from menu
        self.actionSettings.triggered.connect(self.settings_win.show)
        self.actionExit.triggered.connect(app.exit)

        # Status bar
        self.statusbar.showMessage("Status: Ready")

        # Button clicks
        self.defaultGenerateButton.clicked.connect(
            partial(self.textgen_switcher, 'default_mode'))
        self.notebookGenerateButton.clicked.connect(
            partial(self.textgen_switcher, 'notebook_mode'))
        self.chatGenerateButton.clicked.connect(
            partial(self.textgen_switcher, 'chat_mode'))

        self.defaultContinueButton.clicked.connect(
            partial(self.continue_textgen, 'default_modeContinue'))
        self.notebookContinueButton.clicked.connect(
            partial(self.continue_textgen, 'notebook_modeContinue'))
        self.chatContinueButton.clicked.connect(
            partial(self.continue_textgen, 'chat_modeContinue'))

        self.defaultStopButton.clicked.connect(self.stop_textgen)
        self.notebookStopButton.clicked.connect(self.stop_textgen)
        self.chatStopButton.clicked.connect(self.stop_textgen)

        self.paramWinShowButton.clicked.connect(self.settings_win.show)

        self.settingsPathSaveButton.clicked.connect(self.save_settings)

        self.chatClearButton.clicked.connect(self.clear_histories)

        self.cppModelSelect.clicked.connect(self.cpp_model_select)
        self.exllamaModelSelect.clicked.connect(self.exllama_model_select)
        self.RWKVcppModelSelect.clicked.connect(self.rwkv_model_select)

        self.instructPresetComboBox.textActivated.connect(
            partial(self.chat_preset_refresh, 'instruct'))
        self.characterPresetComboBox.textActivated.connect(
            partial(self.chat_preset_refresh, 'character'))
        self.instructRadioButton.clicked.connect(
            partial(self.chat_preset_refresh, 'instruct'))
        self.charactersRadioButton.clicked.connect(
            partial(self.chat_preset_refresh, 'character'))

        self.awesomePresetComboBox.textActivated.connect(
            self.awesome_prompts)

        self.chatInputSessionCombo.textActivated.connect(
            lambda: self.chat_input_history_set())

        self.themeDarkCheck.clicked.connect(lambda: self.set_themes('dark'))
        self.themeLightCheck.clicked.connect(lambda: self.set_themes('light'))
        self.themeNativeCheck.clicked.connect(
            lambda: self.set_themes('native'))

        self.chatRewindButton.clicked.connect(lambda: self.chat_rewind())

        self.set_preset_params('instruct')

    # Set themes
    def set_themes(self, theme):
        extra = {
            'pyside6': True,
            'density_scale': '-1',
            'font_family': ''
        }

        if theme == 'dark':
            apply_stylesheet(app, theme='dark_lightgreen.xml',
                             css_file='assets/dark_theme.css', extra=extra)
        if theme == 'light':
            apply_stylesheet(app, theme='light_lightgreen.xml',
                             css_file='assets/light_theme.css', extra=extra, invert_secondary=False)
        if theme == 'native':
            app.setStyleSheet('')
        print('--- Set theme to:', theme)

    def load_presets(self, directory, combo_box):
        # Load presets from a given directory and populate a combo box.
        presets = glob.glob(f"{directory}/*.yaml")
        presets = sorted(presets)  # sort the list of files alphabetically

        for preset in presets:
            preset_stem = Path(preset).stem
            combo_box.addItem(preset_stem)

    def load_prompts(self, filename):
        # Load prompts from a CSV file and populate a combo box.
        with open(filename, "r",  encoding="utf-8") as csvfile:
            datareader = csv.reader(csvfile)
            # sort the list of files alphabetically
            datareader = sorted(datareader)

            for row in datareader:
                item = row[0]
                self.awesomePresetComboBox.addItem(item)
            self.awesomePresetComboBox.removeItem(0)
            self.awesomePresetComboBox.addItem(item)

    def load_settings(self, filename: str):
        # Load settings from an INI file and set the corresponding widgets.

        # Create a ConfigParser object
        config = configparser.ConfigParser()

        # Read the settings from the file
        config.read(filename)

        # Set the widgets based on the values from the settings section
        self.cppModelPath.setText(config["Settings"]["cpp_model_path"])
        self.exllamaModelPath.setText(config["Settings"]["exllama_model_path"])
        self.rwkvCppModelPath.setText(
            config["Settings"]["rwkv_cpp_model_path"])

        self.botNameLine.setText(config["Settings"]["bot_name"])
        self.yourNameLine.setText(config["Settings"]["user_name"])

        # Set backend based on the value from the settings section
        if config["Settings"]["backend"] == 'llama_cpp':
            self.cppCheck.setChecked(True)
        elif config["Settings"]["backend"] == 'exllama':
            self.exllamaCheck.setChecked(True)
        elif config["Settings"]["backend"] == 'text_synth':
            self.tsServerCheck.setChecked(True)
        elif config["Settings"]["backend"] == 'rwkv_cpp':
            self.rwkvCppCheck.setChecked(True)

        # Set theme based on the value from the settings section
        if config["Settings"]["theme"] == 'dark':
            self.themeDarkCheck.setChecked(True)
        elif config["Settings"]["theme"] == 'light':
            self.themeLightCheck.setChecked(True)
        elif config["Settings"]["theme"] == 'native':
            self.themeNativeCheck.setChecked(True)

        # Set themes by calling set_themes method with theme argument
        self.set_themes(config["Settings"]["theme"])

    # Define a helper function to get the file path from a dialog

    def get_file_path(self, title, filter):
        file_path = (QFileDialog.getOpenFileName(
            self, title, '', filter)[0])
        return file_path

    # Define a helper function to get the directory path from a dialog
    def get_directory_path(self, title):
        directory_path = str(QFileDialog.getExistingDirectory(
            self, title))
        return directory_path

    # Browse for the GGML model
    def cpp_model_select(self):
        cpp_model = self.get_file_path('Open file', "GGML models (*bin)")
        if cpp_model:
            self.cppModelPath.setText(cpp_model)
    # Browse for the exllama model

    def exllama_model_select(self):
        exllama_model = self.get_directory_path("Select Directory")
        if exllama_model:
            self.exllamaModelPath.setText(exllama_model)

    def rwkv_model_select(self):
        rwkv_model = self.get_file_path('Open file', "GGML models (*bin)")
        if rwkv_model:
            self.rwkvCppModelPath.setText(rwkv_model)

    # Save the current settings to an INI file
    def save_settings(self):
        # Create a ConfigParser object
        config = configparser.ConfigParser()
        # Read the existing settings from the file
        config.read(SETTINGS_FILE)

        # Set the values for the settings section based on the widgets
        config.set("Settings", "cpp_model_path", self.cppModelPath.text())
        config.set("Settings", "exllama_model_path",
                   self.exllamaModelPath.text())
        config.set("Settings", "rwkv_cpp_model_path",
                   self.rwkvCppModelPath.text())

        config.set("Settings", "user_name", self.yourNameLine.text())
        config.set("Settings", "bot_name", self.botNameLine.text())
        config.set("Params-TextSynth", "ts_model",
                   self.settings_win.tsModelLine.text())

        # Save backend based on the checked radio button
        if self.cppCheck.isChecked():
            config.set("Settings", "backend", "llama_cpp")
        elif self.exllamaCheck.isChecked():
            config.set("Settings", "backend", "exllama")
        elif self.tsServerCheck.isChecked():
            config.set("Settings", "backend", "text_synth")
        elif self.rwkvCppCheck.isChecked():
            config.set("Settings", "backend", "rwkv_cpp")

        # Save theme based on the checked radio button
        if self.themeDarkCheck.isChecked():
            config.set("Settings", "theme", "dark")
        elif self.themeLightCheck.isChecked():
            config.set("Settings", "theme", "light")
        elif self.themeNativeCheck.isChecked():
            config.set("Settings", "theme", "native")

        # Open the file in write mode
        with open("settings.ini", "w") as f:
            # Write the ConfigParser object to the file
            config.write(f)

        # Close the file
        f.close()

        print('--- Settings saved')

    def history_readonly_logic(self, readonly_mode: bool):
        """Set the history widget and the buttons to readonly mode or not.
        Args:
            readonly_mode (bool): Whether to enable readonly mode or not.
        """

        # A dictionary to map the textgen modes to the corresponding widgets
        mode_widgets = {
            "notebook_mode": self.notebook_modeTextHistory,
        }

        # Set the history widget to readonly mode based on the textgen mode
        history_widget = mode_widgets.get(self.textgen_mode)
        if history_widget:
            history_widget.setReadOnly(readonly_mode)

        # Invert readonly_mode for buttons
        button_mode = not readonly_mode

        # A list of buttons to enable or disable based on the button mode
        buttons = [
            self.instructPresetComboBox,
            self.characterPresetComboBox,
            self.streamEnabledCheck,
            self.defaultContinueButton,
            self.notebookContinueButton,
            self.chatContinueButton,
            self.defaultGenerateButton,
            self.notebookGenerateButton,
            self.chatGenerateButton,
            self.defaultClearButton,
            self.notebookClearButton,
            self.chatClearButton,
            self.instructRadioButton,
            self.charactersRadioButton,
            self.chatRewindButton,
        ]

        # Iterate over the buttons and set their enabled status
        for button in buttons:
            button.setEnabled(button_mode)

    # Stop button logic
    def stop_textgen(self):
        self.textgenThread.stop()

        # Disable all stop buttons
        for button in [self.defaultStopButton, self.notebookStopButton, self.chatStopButton]:
            button.setEnabled(False)

    # Continue button logic
    def continue_textgen(self, text_tab):

        # Get the history text from the corresponding tab
        history_text = getattr(self, text_tab.replace(
            'Continue', 'TextHistory')).toPlainText()
        if history_text:
            self.continue_textgen_mode = True

            if self.cppCheck.isChecked():
                if not self.cppServerCheck.isChecked():
                    run_backend = 'llama.cpp'
                else:
                    run_backend = 'llama.cpp_server'

            elif self.exllamaCheck.isChecked():
                run_backend = 'exllama'
            elif self.tsServerCheck.isChecked():
                run_backend = 'ts-server'
            elif self.rwkvCppCheck.isChecked():
                run_backend = 'rwkv.cpp'
            # Launch the backend with the history text and the run backend
            self.launch_backend(history_text, run_backend)

    # Define a helper function to insert text and scroll to the end of a text widget
    def insert_text_and_scroll(self, text_widget, text):

        cursor = text_widget.textCursor()
        cursor.movePosition(QTextCursor.End)  # Move it to the end
        cursor.insertText(text)
        text_widget.verticalScrollBar().setValue(
            text_widget.verticalScrollBar().maximum())

    @Slot(str)
    def handleResult(self, reply):
        # Get the text widget from the textgen mode
        text_widget = getattr(self, self.textgen_mode + 'TextHistory')

        # Insert the reply and scroll to the end
        self.insert_text_and_scroll(text_widget, reply)

    # Handle the final response from textgen
    @Slot(str)
    def final_handleResult(self, final_text):
        # Write chat log

        if final_text.endswith('USER:'):
            final_text = final_text.rstrip("USER:")

        if self.textgen_mode == 'chat_mode':
            if self.continue_textgen_mode:
                updated = str(
                    (self.message_history[-1].rstrip())+final_text.rstrip()+'\n\n')
                self.message_history[-1] = updated
                self.chat_output_list.pop(-1)
                self.continue_textgen_mode = False
            else:
                if self.customResponsePrefixCheck.isChecked():
                    self.message_history.append(
                        self.customResponsePrefix.text()+final_text.rstrip()+'\n\n')
                else:
                    self.message_history.append(final_text.rstrip()+'\n\n')

        # Write chatlog with write_chatlog, no new session
        if self.textgen_mode == 'chat_mode' and self.logChatCheck.isChecked():
            self.write_chatlog(False)

        self.statusbar.showMessage(f"Status: Generation complete")
        self.history_readonly_logic(False)

        self.chat_output_list.append(self.chat_modeTextHistory.toHtml())

        # Stop the textgen thread
        self.stop_textgen()

    def write_chatlog(self, new_session):
        current_date = self.get_chat_date()
        log_text = ''

        if not new_session:
            log_text = self.name_history[-2]+self.message_history[-2] + \
                self.name_history[-1]+self.message_history[-1]
        else:
            log_text = '\n############ New session ############\n'

        with open(f"logs/chat_{current_date}.txt", "a", encoding='utf-8') as f:
            f.write('\n'+log_text)
        print('--- Wrote chat log')

    def get_stop_strings(self):
        stop_strings = []

        if self.instructRadioButton.isChecked():
            chat_preset = self.get_chat_presets()
            stop_strings.append(chat_preset["user"])

        elif self.charactersRadioButton.isChecked():
            stop_strings.append(self.yourNameLine.text()+':')

        # print('stopstrings', stop_strings)
        return stop_strings

    # Get the llama.cpp parameters
    def get_llama_cpp_params(self):
        stop_strings = self.get_stop_strings()

        cpp_params = {
            'max_new_tokens': int(self.settings_win.max_new_tokensSpin.value()),
            'temperature': float(self.settings_win.temperatureSpin.value()),
            'top_p': float(self.settings_win.top_pSpin.value()),
            'top_k': int(self.settings_win.top_kSpin.value()),
            'repetition_penalty': float(self.settings_win.repetition_penaltySpin.value()),
            'mirostat_mode': int(self.settings_win.cppMirastatMode.value()),
            'stop': list(stop_strings),
            'tfs_z': float(self.settings_win.cpp_tfszSpin.value()),
            'frequency_penalty': float(self.settings_win.freqPenaltySpin.value()),
            'presence_penalty': float(self.settings_win.presencePenaltySpin.value()),
        }
        # print('--- cpp_params:', cpp_params)
        return cpp_params

    # Get the Exllama parameters
    def get_exllama_params(self):

        stop_strings = self.get_stop_strings()

        exllama_params = {
            'max_new_tokens': self.settings_win.max_new_tokensSpin.value(),
            'temperature': self.settings_win.temperatureSpin.value(),
            'top_p': self.settings_win.top_pSpin.value(),
            'repetition_penalty': self.settings_win.repetition_penaltySpin.value(),
            'top_k': self.settings_win.top_kSpin.value(),
            'num_beams': self.settings_win.numbeamsSpin.value(),
            'beam_length': self.settings_win.beamLengthSpin.value(),
            'min_p': self.settings_win.minPSpin.value(),
            'token_repetition_penalty_sustain': self.settings_win.token_repetition_penalty_decaySpin.value(),
            'stop': str(stop_strings[0]),
        }
        # print('--- exllama_params:', exllama_params)
        return exllama_params

    # Get data for chat log save
    def get_chat_date(self):
        today = datetime.today()
        day = today.day
        month = today.month
        year = today.year
        return (f'{day}-{month}-{year}')

        # Get chat presets from a YAML file
    def get_chat_presets(self):

        if self.instructRadioButton.isChecked():
            chat_mode = "instruct"

        elif self.charactersRadioButton.isChecked():
            chat_mode = "character"

        preset_name = getattr(self, chat_mode + 'PresetComboBox').currentText()
        preset_file = f"presets/{chat_mode}/{preset_name}.yaml"
        with open(preset_file, 'r') as file:
            chat_preset = yaml.safe_load(file)
        return chat_preset

    def get_model_path(self, line_edit):
        # Get the model path from a line edit widget
        model_path = line_edit.text().strip()
        return model_path

    def get_rwkv_cpp_model_params(self):
        # Get the Exllama model parameters from the settings window
        rwkv_cpp_model_params = {
            'model_path': self.get_model_path(self.rwkvCppModelPath),
            'n_threads': self.settings_win.cppThreads.value(),
            'n_gpu_layers': self.settings_win.gpuLayersSpin.value(),
        }

        # if self.settings_win.gpuAccelCheck.isChecked():
        #     rwkv_cpp_model_params["n_gpu_layers"] = self.settings_win.gpuLayersSpin.value()

        return rwkv_cpp_model_params

    def get_exllama_model_params(self):
        # Get the Exllama model parameters from the settings window
        exllama_model_params = {
            'model_path': self.get_model_path(self.exllamaModelPath),
            'gpu_split': self.settings_win.exllamaGpuSplitCheck.isChecked()
        }
        if self.settings_win.exllamaGpuSplitCheck.isChecked():
            exllama_model_params["gpu_split_values"] = self.settings_win.exllamaGpuSplitLine.text(
            )
        return exllama_model_params

    def get_cpp_model_params(self):
        # Get the cpp model parameters from the settings window
        cpp_model_params = {
            'model_path': self.get_model_path(self.cppModelPath),
            'seed': self.settings_win.seedSpin.value(),
            'n_threads': self.settings_win.cppThreads.value(),
            'n_batch': self.settings_win.cppBatchSizeSpin.value(),
            'n_ctx': self.settings_win.CPP_ctxsize_Spin.value(),
            'use_mmap': self.settings_win.cppMmapCheck.isChecked(),
            'use_mlock': self.settings_win.cppMlockCheck.isChecked(),
            'verbose': self.settings_win.cppVerboseCheck.isChecked(),
        }

        if self.settings_win.gpuAccelCheck.isChecked():
            cpp_model_params["n_gpu_layers"] = self.settings_win.gpuLayersSpin.value(
            )
        if self.settings_win.cppLoraLineEdit.text():
            cpp_model_params["lora_path"] = self.get_model_path(
                self.settings_win.cppLoraLineEdit)
        return cpp_model_params

    def load_model(self, model_name):
        # Load a model based on its name
        print(f'--- Loading {model_name} model...')
        self.statusbar.showMessage(f'Status: Loading {model_name} model...')

        if model_name == 'Exllama':
            from exllama_generate import ExllamaModel
            global exllama_model
            exllama_model = ExllamaModel.from_pretrained(
                self.get_exllama_model_params())
            print('--- Exllama model load parameters:',
                  self.get_exllama_model_params())

        elif model_name == 'llama.cpp':
            use_cache = bool(self.settings_win.cppCacheCheck.isChecked())
            from llamacpp_generate import LlamaCppModel
            global cpp_model
            cpp_model = LlamaCppModel.from_pretrained(use_cache,
                                                      self.get_cpp_model_params())
            print('--- llama.cpp model load parameters:',
                  self.get_cpp_model_params())

        elif model_name == 'rwkv.cpp':
            import rwkvcpp_generate
            global rwkv_cpp_model
            rwkv_cpp_model = rwkvcpp_generate.load_model(
                self.get_rwkv_cpp_model_params())
            print('--- rwkv.cpp model load parameters:')

    # Enable the stop buttons for each mode

    def set_textgen_things(self):
        self.defaultStopButton.setEnabled(True)
        self.notebookStopButton.setEnabled(True)
        self.chatStopButton.setEnabled(True)

    # Formatting the chat display text
    def chat_formatting(self, input_message):
        # Get the chat input and strip any leading or trailing whitespace
        chat_input = input_message.strip()
        # Create a list of paragraphs for the text history
        paragraphs = []
        # Add a paragraph with the user name and chat input
        paragraphs.append(
            f"<b style='color: #a92828'>{self.yourNameLine.text()}:</b><br>{chat_input}<br>")
        # Add a paragraph with the bot name and custom response prefix if checked
        if self.customResponsePrefixCheck.isChecked():
            paragraphs.append(
                f"<b style='color: #3194d0'>{self.botNameLine.text()}:</b><br>{self.customResponsePrefix.text()}")
        else:
            paragraphs.append(
                f"<b style='color: #3194d0'>{self.botNameLine.text()}:</b><br>")
        # Join the paragraphs with line breaks and wrap them in <p> tags
        chat_text = f"<p><br>{'<br>'.join(paragraphs)}</p>"

        return chat_text

    # Main launcher logic
    def textgen_switcher(self, textgen_mode):
        self.textgen_mode = textgen_mode

        # Check if the model has been loaded
        if not self.model_load:
            # Load the model based on the user's choice of cpp or exllama
            if self.cppCheck.isChecked() and not self.cppServerCheck.isChecked():
                try:
                    self.load_model('llama.cpp')
                except Exception as error:
                    print('--- Error: Could not load llama.cpp model')
                    print(error)
                    self.statusbar.showMessage(
                        'Status: Error! Could not load llama.cpp model')
                    return
                else:
                    self.model_load = True

            elif self.exllamaCheck.isChecked():
                try:
                    self.load_model('Exllama')
                except Exception as error:
                    print('--- Error: Could not load Exllama model')
                    print(error)
                    self.statusbar.showMessage(
                        'Status: Error! Could not load Exllama model')
                    return
                else:
                    self.model_load = True
            elif self.tsServerCheck.isChecked():
                # TS Server
                pass

            elif self.rwkvCppCheck.isChecked():
                try:
                    self.load_model('rwkv.cpp')
                except Exception as error:
                    print('--- Error: Could not load rwkv.cpp model')
                    print(error)
                    self.statusbar.showMessage(
                        'Status: Error! Could not load rwkv.cpp model')
                    return
                else:
                    self.model_load = True

            # Disable the cpp and exllama checkboxes
            self.cppCheck.setEnabled(False)
            self.exllamaCheck.setEnabled(False)
            self.tsServerCheck.setEnabled(False)
            self.cppServerCheck.setEnabled(False)
            self.rwkvCppCheck.setEnabled(False)

        if not self.cppCheck.isEnabled():
            if self.cppCheck.isChecked():
                if not self.cppServerCheck.isChecked():
                    backend = 'llama.cpp'
                else:
                    backend = 'llama.cpp_server'
            elif self.exllamaCheck.isChecked():
                backend = 'exllama'
            elif self.tsServerCheck.isChecked():
                backend = 'ts-server'
            elif self.rwkvCppCheck.isChecked():
                backend = 'rwkv.cpp'

        # If the pre-textgen mode is default mode
        if self.textgen_mode == 'default_mode':
            input_message = self.defaultTextInput.toPlainText()
            # If the input message is not empty
            if input_message:
                # Set the default mode text history widget to show the input message
                self.default_modeTextHistory.setPlainText(input_message)
                # Launch the backend with the input message and the backend name
                self.launch_backend(input_message, backend)

        # If the pre-textgen mode is notebook mode
        if self.textgen_mode == 'notebook_mode':
            input_message = self.notebook_modeTextHistory.toPlainText()
            # If the input message is not empty
            if input_message:
                # Launch the backend with the input message and the backend name
                self.launch_backend(input_message, backend)

        # If the pre-textgen mode is chat mode
        if self.textgen_mode == 'chat_mode':

            # Get the input message from the chat mode text input widget
            input_message = self.chat_modeTextInput.toPlainText()

            # If the input message is not empty
            if input_message:

                # Generate a final prompt by calling the prompt_generation method with the pre-textgen mode argument
                final_prompt = self.prompt_generation()

                # Get formatted chat text
                input_message = input_message.strip().replace("\n", "<br>")
                chat_text = self.chat_formatting(input_message)

                # Append the text to the chat mode text history widget
                self.chat_modeTextHistory.append(chat_text)

                # Launch the backend with the final prompt and the backend name
                self.launch_backend(final_prompt, backend)

                # Clear the chat mode text input widget
                self.chat_input_history_add(input_message)
                self.chat_modeTextInput.clear()

    def get_token_count(self, message):
        llama_tokenizer = Tokenizer("assets/tokenizer.model")
        encoded_string = llama_tokenizer.encode(message, True, True)
        token_count = len(encoded_string)
        return token_count

    # Launch QThread to textgen
    def launch_backend(self, message, run_backend):

        # Get the exllama and cpp parameters from their respective methods
        exllama_params = self.get_exllama_params()
        cpp_params = self.get_llama_cpp_params()

        token_count = self.get_token_count(message)

        # Show a status message indicating that the generation is in progress
        self.statusbar.showMessage(
            f"Status: Generating... (Context: {token_count} tokens)")

        # Create a textgenThread object with the exllama and cpp parameters, the message, the stream enabled status, and the backend name
        self.textgenThread = TextgenThread(
            exllama_params, message,
            self.streamEnabledCheck.isChecked(), run_backend, cpp_params, self.settings_win.tsModelLine.text())

        # Connect signals and slots
        self.textgenThread.resultReady.connect(self.handleResult)
        self.textgenThread.final_resultReady.connect(self.final_handleResult)
        self.textgenThread.finished.connect(self.textgenThread.deleteLater)

        # Start the thread
        self.textgenThread.start()
        # Set the textgen things
        self.set_textgen_things()

        # Set the history to read-only mode
        self.history_readonly_logic(True)

    # Define a function to process the turn template for chat mode
    def process_instruct_turn_template(self):

        if self.instructRadioButton.isChecked():
            chat_preset = self.get_chat_presets()
            first_turn_template = str(chat_preset["turn_template"])

        elif self.charactersRadioButton.isChecked():
            chat_preset = self.get_chat_presets()
            first_turn_template = "<|user|>:\n<|user-message|>\n\n<|bot|>:\n<|bot-message|>\n\n"

        # Get the context string from the chat preset
        pre_prompt = chat_preset["context"]

        # Split the turn template string by the user message placeholder
        turn_template = first_turn_template.split("<|user-message|>")
        # Get the first part of the turn template as the user template
        template_user = turn_template[0]

        # Remove the user template from the turn template and split by the bot placeholder
        turn_template = first_turn_template.replace(template_user, "")
        turn_template = turn_template.split("<|bot|>")
        # Get the first part of the turn template as the user message template
        template_user_msg = turn_template[0]

        # Remove the user template and user message template from the turn template and split by the bot message placeholder
        turn_template = first_turn_template.replace(
            template_user, "").replace(template_user_msg, "")
        turn_template = turn_template.split("<|bot-message|>")
        # Get the first part of the turn template as the bot template
        template_bot = turn_template[0]

        # Get the remaining part of the turn template as the bot message template
        template_bot_msg = first_turn_template.replace(
            template_user, "").replace(template_user_msg, "").replace(template_bot, "")

        if self.instructRadioButton.isChecked():
            user = template_user.replace("<|user|>", chat_preset["user"])
            bot = template_bot.replace("<|bot|>", chat_preset["bot"])
        elif self.charactersRadioButton.isChecked():
            user = template_user.replace("<|user|>", self.yourNameLine.text())
            bot = template_bot.replace("<|bot|>", chat_preset["name"])

            # Replace the user message placeholder with the input text from the chat mode text input widget
        user_msg = template_user_msg.replace(
            "<|user-message|>", self.chat_modeTextInput.toPlainText())

        # Return a tuple of user, user message, bot, bot message and pre prompt
        return user, user_msg, bot, template_bot_msg, pre_prompt

    # Define a function to generate a final prompt for text generation based on the mode
    def prompt_generation(self):

        # Call process_turn_template function and get a tuple of values
        user, user_msg, bot, bot_msg, pre_prompt = self.process_instruct_turn_template()

        # Append user and user message to name history and message history lists
        self.name_history.append(user)
        self.message_history.append(user_msg)
        # Append bot to name history list
        self.name_history.append(bot)

        # Initialize an empty string for prompt
        prompt = ''
        # Loop through name history and message history lists and concatenate them into prompt string
        for user, msg in zip(self.name_history, self.message_history):
            prompt += user + msg

        # Add pre prompt and prompt strings together and assign to final prompt variable
        final_prompt = pre_prompt+'\n'+prompt+bot

        if self.customResponsePrefixCheck.isChecked():
            final_prompt = final_prompt+self.customResponsePrefix.text()

        # print('='+final_prompt+'=')
        return final_prompt

    def chat_rewind(self):
        # Undo the last two chat turns and restore the previous chat output
        # If there are at least two items in the name and message history lists
        if len(self.name_history) and len(self.message_history) >= 2:
            print('--- Chat rewind')
            # Pop the last two names and messages from their respective lists
            self.name_history.pop()
            self.name_history.pop()
            self.message_history.pop()
            self.message_history.pop()
            # Set the chat mode text history widget to show the second last chat output
            self.chat_modeTextHistory.setHtml(self.chat_output_list[-2])
            self.chat_modeTextHistory.verticalScrollBar().setValue(
                self.chat_modeTextHistory.verticalScrollBar().maximum())
            # Pop the last chat output from the list
            self.chat_output_list.pop()
        # If there are no items in the name history list
        if len(self.name_history) == 0:
            # Get the chat preset dictionary from a file
            chat_preset = self.get_chat_presets()
            # Get the context string from the chat preset and strip any whitespace
            pre_prompt = chat_preset["context"].strip()
            # Set the chat mode text history widget to show the context string
            self.chat_modeTextHistory.setPlainText(pre_prompt)

    def chat_input_history_add(self, chat_input):
        # Add the chat input to the combo box and the history list
        # Add the first 96 characters of the chat input to the combo box
        self.chatInputSessionCombo.addItem(str(chat_input[:96]))
        # Append the chat input to the history list
        self.chat_input_history.append(chat_input)

    def chat_input_history_set(self):
        # Set the chat input field to the saved history
        # If there are any items in the combo box
        if self.chatInputSessionCombo.count() >= 1:
            # Get the text from the history list based on the combo box index
            text = self.chat_input_history[int(
                self.chatInputSessionCombo.currentIndex())]
            # Set the chat mode text input widget to show the text
            self.chat_modeTextInput.setPlainText(text)

    def chat_preset_refresh(self, mode, partial=None):
        # Refresh the chat preset based on the mode and partial arguments
        # Clear the name, message and output lists
        self.name_history = []
        self.message_history = []
        self.chat_output_list = []
        # Set the preset parameters by calling set_preset_params method with mode argument
        self.set_preset_params(mode)

    def clear_histories(self):
        # Clear all histories
        # If there are any items in the name and message lists
        if len(self.name_history) and len(self.message_history) >= 2:
            # Clear the name, message and output lists
            self.name_history = []
            self.message_history = []
            self.chat_output_list = []

        # Set the preset parameters by calling set_preset_params method without arguments
        self.set_preset_params()

    # Set the preset parameters based on the preset mode argument
    def set_preset_params(self, preset_mode=None, partial=None):
        # Clear the chat mode text history widget
        self.chat_modeTextHistory.clear()

        # Clear rewind history by creating a new empty list for output list
        self.chat_output_list = []
        # Append the current html of chat mode text history widget to output list
        self.chat_output_list.append(self.chat_modeTextHistory.toHtml())

        # Use a dictionary to map the preset modes to the radio buttons and file names
        preset_dict = {"instruct": (self.instructRadioButton, "instruct"),
                       "character": (self.charactersRadioButton, "character")}

        # If no preset mode is given, use the checked radio button to determine it
        if not preset_mode:
            for mode, (radio_button, file_name) in preset_dict.items():
                if radio_button.isChecked():
                    preset_mode = mode
                    break

        # Check the radio button for the preset mode
        radio_button, file_name = preset_dict[preset_mode]
        radio_button.setChecked(True)

        # Get the chat preset dictionary for the preset mode from a file
        chat_preset = self.get_chat_presets()

        # Get the context string from the chat preset and strip any whitespace
        pre_prompt = str(chat_preset["context"]).strip()
        # Append it to the chat mode text history widget
        self.chat_modeTextHistory.append(pre_prompt)

    # Get awesome prompts from a csv file
    def awesome_prompts(self):
        filename = "presets/prompts.csv"
        with open(filename, "r",  encoding="utf-8") as csvfile:
            datareader = csv.reader(csvfile)
            for row in datareader:
                # If the row matches the current text of the awesome preset combo box
                if row[0] == self.awesomePresetComboBox.currentText():
                    # Set the chat mode text input widget to show the prompt from the row
                    self.chat_modeTextInput.setPlainText(row[1])
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
