import configparser
import csv
import glob
import platform
import sys
from datetime import datetime
from functools import partial
from pathlib import Path

import yaml
from PySide6 import QtWidgets
from PySide6.QtCore import QSize, QThread, Signal, Slot
from PySide6.QtGui import QIcon, QTextCursor
from PySide6.QtWidgets import QApplication, QFileDialog
from qt_material import apply_stylesheet

from main_window import Ui_MainWindow
from settings_window import Ui_Settings_Dialog

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


# A class to load models in a separate thread
class LoadModelThread(QThread):
    final_resultReady = Signal(bool)

    def __init__(
        self,
        backend: str,
        cpp_model_params: dict,
        exllama_model_params: dict,
        llama_cpp_cache: bool,
    ):
        super().__init__()
        self.cpp_model_params = cpp_model_params
        self.exllama_model_params = exllama_model_params
        self.backend = backend
        self.llama_cpp_cache = llama_cpp_cache

    def run(self):
        load_backend_methods = {
            EXLLAMA: self.load_exllama,
            LLAMA_CPP: self.load_cpp,
        }
        backend_method = load_backend_methods.get(self.backend)
        if backend_method:
            try:
                backend_method()
                self.final_resultReady.emit(True)
            except Exception as error:
                self.final_resultReady.emit(False)
                print("--- Error loading backend:\n", error)
                return
        else:
            raise ValueError(f"Invalid load_backend: {self.backend}")

    def load_cpp(self):
        from llamacpp_generate import LlamaCppModel

        global cpp_model
        cpp_model = LlamaCppModel.from_pretrained(
            self.llama_cpp_cache, self.cpp_model_params
        )

    def load_exllama(self):
        from exllama_generate import ExllamaModel

        global exllama_model
        exllama_model = ExllamaModel.from_pretrained(self.exllama_model_params)


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
    ):
        super().__init__()
        self.exllama_params = exllama_params
        self.message = message
        self.stream_enabled = stream_enabled
        self.run_backend = run_backend
        self.cpp_params = cpp_params
        self.stop_flag = False

        # print("---" + self.message + "---")

    def run(self):
        """Run the appropriate backend method based on the run_backend attribute."""
        backend_methods = {
            EXLLAMA: self.run_exllama,
            LLAMA_CPP: self.run_llama_cpp,
            LLAMA_CPP_SERVER: self.run_llama_cpp_server,
        }
        backend_method = backend_methods.get(self.run_backend)
        if backend_method:
            try:
                backend_method()
            except Exception as error:
                self.final_resultReady.emit("")
                print("--- Error running backend:\n", error)
                return
        else:
            raise ValueError(f"Invalid run_backend: {self.run_backend}")

    def run_exllama(self):
        """Run the Exllama model and generate a response."""
        responses = exllama_model.generate_with_streaming(
            self.message, self.exllama_params
        )
        final_response = ""
        for response in responses:
            final_response += response
            if self.stop_flag:
                break
            if self.stream_enabled:
                self.resultReady.emit(response)
        if not self.stream_enabled:
            self.resultReady.emit(final_response)
        self.final_resultReady.emit(final_response)

    def run_llama_cpp(self):
        """Run the llama.cpp model and generate a response."""
        kwargs = {
            "max_tokens": self.cpp_params["max_new_tokens"],
            "temperature": self.cpp_params["temperature"],
            "top_p": self.cpp_params["top_p"],
            "top_k": self.cpp_params["top_k"],
            "repeat_penalty": self.cpp_params["repetition_penalty"],
            "mirostat_mode": self.cpp_params["mirostat_mode"],
            "mirostat_tau": self.cpp_params["mirostat_tau"],
            "mirostat_eta": self.cpp_params["mirostat_eta"],
            "stop": self.cpp_params["stop"],
            "tfs_z": self.cpp_params["tfs_z"],
            "frequency_penalty": self.cpp_params["frequency_penalty"],
            "presence_penalty": self.cpp_params["presence_penalty"],
        }

        responses = (
            cpp_model.generate_with_streaming(self.message, **kwargs)
            if self.stream_enabled
            else [cpp_model.generate(self.message, **kwargs)]
        )
        response_list = []

        for response in responses:
            if self.stop_flag:
                break
            self.resultReady.emit(response)
            response_list.append(response)
        final_text = f"{''.join(response_list)}"
        self.final_resultReady.emit(final_text)

    def run_llama_cpp_server(self):
        """Run the llama.cpp server and generate a response."""
        import llamacpp_server_generate

        final_text = ""
        if self.stream_enabled:
            for response in llamacpp_server_generate.generate_with_streaming(
                self.message, self.cpp_params
            ):
                if self.stop_flag:
                    break
                final_text += response
                self.resultReady.emit(response)
        else:
            final_text = llamacpp_server_generate.generate_nostream(
                self.message, self.cpp_params
            )
            self.resultReady.emit(final_text)
        self.final_resultReady.emit(final_text)

    def stop(self):
        """Set the stop flag to True."""
        self.stop_flag = True


class SettingsWindow(QtWidgets.QWidget, Ui_Settings_Dialog):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

        # Set the window icon
        icon = QIcon()
        icon.addFile(str(APP_ICON), QSize(), QIcon.Normal, QIcon.Off)
        self.setWindowIcon(icon)

        def exllama_lora_select():
            exllama_lora = get_directory_path("Select LoRA directory")
            if exllama_lora:
                self.exllamaLora.setText(exllama_lora)

        def cpp_lora_select():
            cpp_lora = get_file_path("Open file", "GGML LoRA model (*bin)")
            if cpp_lora:
                self.cppLoraLineEdit.setText(cpp_lora)

        def get_file_path(title, filter):
            file_path = QFileDialog.getOpenFileName(self, title, "", filter)[0]
            return file_path

        def get_directory_path(title):
            directory_path = str(QFileDialog.getExistingDirectory(self, title))
            return directory_path

        self.exllamaLoraSelect.clicked.connect(exllama_lora_select)
        self.cppLoraSelect.clicked.connect(cpp_lora_select)

        # Connect the settings sliders to the spin boxes
        self.temperatureSlider.valueChanged.connect(
            lambda: self.temperatureSpin.setValue(self.temperatureSlider.value() / 100)
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
            lambda: self.cpp_tfszSpin.setValue(self.cpp_tfszSlider.value() / 100)
        )
        self.freqPenaltySlider.valueChanged.connect(
            lambda: self.freqPenaltySpin.setValue(self.freqPenaltySlider.value() / 100)
        )
        self.presencePenaltySlider.valueChanged.connect(
            lambda: self.presencePenaltySpin.setValue(
                self.presencePenaltySlider.value() / 100
            )
        )
        self.typical_pSlider.valueChanged.connect(
            lambda: self.typical_pSpin.setValue(self.typical_pSlider.value() / 100)
        )

        # Connect the spin boxes to the settings sliders
        self.temperatureSpin.valueChanged.connect(
            lambda: self.temperatureSlider.setValue(self.temperatureSpin.value() * 100)
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
            lambda: self.cpp_tfszSlider.setValue(self.cpp_tfszSpin.value() * 100)
        )
        self.freqPenaltySpin.valueChanged.connect(
            lambda: self.freqPenaltySlider.setValue(self.freqPenaltySpin.value() * 100)
        )
        self.presencePenaltySpin.valueChanged.connect(
            lambda: self.presencePenaltySlider.setValue(
                self.presencePenaltySpin.value() * 100
            )
        )
        self.typical_pSpin.valueChanged.connect(
            lambda: self.typical_pSlider.setValue(self.typical_pSpin.value() * 100)
        )
        # Define a function to load parameters presets

        def load_params():
            param_preset_load = glob.glob("presets/model_params/*.yaml")
            # sort the list of files alphabetically
            param_preset_load = sorted(param_preset_load)
            for param_preset in param_preset_load:
                param_preset_stem = Path(param_preset).stem
                self.paramPresets_comboBox.addItem(param_preset_stem)

            # Set the default preset to Magi-Default
            self.paramPresets_comboBox.setCurrentText("Magi-Default")

        # Call the function to load parameters presets
        load_params()

        def set_params():
            # Load and set parameters
            config = configparser.ConfigParser()
            config.read("settings.ini")

            ### Define params ###
            # Params-Shared
            context_size = config["Params-Shared"]["context_size"]
            temperature = config["Params-Shared"]["temperature"]
            top_k = config["Params-Shared"]["top_k"]
            top_p = config["Params-Shared"]["top_p"]
            max_new_tokens = config["Params-Shared"]["max_new_tokens"]
            repetition_penalty = config["Params-Shared"]["repetition_penalty"]
            seed = config["Params-Shared"]["seed"]
            typical_p = config["Params-Shared"]["typical_p"]

            # Params-Exllama
            min_p = config["Params-Exllama"]["min_p"]
            token_repetition_penalty_decay = config["Params-Exllama"][
                "token_repetition_penalty_decay"
            ]
            num_beams = config["Params-Exllama"]["num_beams"]
            beam_length = config["Params-Exllama"]["beam_length"]
            gpu_split = config["Params-Exllama"]["gpu_split"]
            gpu_split_values = config["Params-Exllama"]["gpu_split_values"]
            exllama_lora_path = config["Params-Exllama"]["exllama_lora_path"]
            exllama_lora_check = config["Params-Exllama"]["exllama_lora_check"]
            compress_pos_embed_check = config["Params-Exllama"][
                "compress_pos_embed_check"
            ]
            compress_pos_embed_value = config["Params-Exllama"][
                "compress_pos_embed_value"
            ]

            # Params-LlamaCPP
            threads = config["Params-LlamaCPP"]["threads"]
            tfs_z = config["Params-LlamaCPP"]["tfs_z"]
            batch_size = config["Params-LlamaCPP"]["batch_size"]
            mirostat_mode = config["Params-LlamaCPP"]["mirostat_mode"]
            mirostat_tau = config["Params-LlamaCPP"]["mirostat_tau"]
            mirostat_eta = config["Params-LlamaCPP"]["mirostat_eta"]
            n_gpu_layers = config["Params-LlamaCPP"]["n_gpu_layers"]
            lora_path = config["Params-LlamaCPP"]["lora_path"]
            frequency_penalty = config["Params-LlamaCPP"]["frequency_penalty"]
            presence_penalty = config["Params-LlamaCPP"]["presence_penalty"]

            use_mmap = config["Params-LlamaCPP"]["use_mmap"]
            use_mlock = config["Params-LlamaCPP"]["use_mlock"]
            use_gpu_accel = config["Params-LlamaCPP"]["use_gpu_accel"]
            use_cache = config["Params-LlamaCPP"]["use_cache"]
            use_verbose = config["Params-LlamaCPP"]["use_verbose"]

            ### Set params ###
            # Params-Shared
            self.ctxsizeSpin.setValue(int(context_size))
            self.ctxsizeSlider.setValue(int(context_size))

            self.temperatureSpin.setValue(float(temperature))
            self.temperatureSlider.setValue(int(float(temperature) * 100))

            self.top_kSpin.setValue(int(top_k))
            self.top_kSlider.setValue(int(top_k))

            self.top_pSpin.setValue(float(top_p))
            self.top_pSlider.setValue(int(float(top_p) * 100))

            self.max_new_tokensSpin.setValue(int(max_new_tokens))
            self.max_new_tokensSlider.setValue(int(max_new_tokens))

            self.repetition_penaltySpin.setValue(float(repetition_penalty))
            self.repetition_penaltySlider.setValue(int(float(repetition_penalty) * 100))

            self.typical_pSpin.setValue(float(typical_p))
            self.typical_pSlider.setValue(int(float(typical_p) * 100))

            self.seedSpin.setValue(int(seed))

            # Params-Exllama
            self.minPSpin.setValue(float(min_p))
            self.minPSlider.setValue(int(min_p))

            self.token_repetition_penalty_decaySpin.setValue(
                int(token_repetition_penalty_decay)
            )
            self.token_repetition_penalty_decaySlider.setValue(
                int(token_repetition_penalty_decay)
            )

            self.numbeamsSpin.setValue(int(num_beams))
            self.numbeamsSlider.setValue(int(num_beams))

            self.beamLengthSpin.setValue(int(beam_length))
            self.beamLengthSlider.setValue(int(beam_length))

            self.exllamaGpuSplitCheck.setChecked(eval(gpu_split))
            self.exllamaGpuSplitLine.setText((gpu_split_values))

            self.exllamaLora.setText(exllama_lora_path)
            self.exllamaLoraCheck.setChecked(eval(exllama_lora_check))
            self.compressPosEmbedCheck.setChecked(eval(compress_pos_embed_check))
            self.compressPosEmbedSpin.setValue(int(compress_pos_embed_value))

            # Params-LlamaCPP
            self.cppThreads.setValue(int(threads))

            self.cpp_tfszSpin.setValue(float(tfs_z))
            self.cpp_tfszSlider.setValue(int(float(tfs_z) * 100))

            self.cppBatchSizeSpin.setValue(int(batch_size))
            self.cppBatchSizeSlider.setValue(int(batch_size))

            self.gpuLayersSpin.setValue(int(n_gpu_layers))
            self.gpuLayersSlider.setValue(int(n_gpu_layers))

            self.cppLoraLineEdit.setText(str(lora_path))
            self.cppMirostatMode.setValue(int(mirostat_mode))
            self.cppMirostatTau.setValue(int(mirostat_tau))
            self.cppMirostatEta.setValue(float(mirostat_eta))

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
            self.temperatureSpin.setValue(float(param_preset_name["temperature"]))
            self.temperatureSlider.setValue(int(param_preset_name["temperature"] * 100))
            self.repetition_penaltySpin.setValue(
                float(param_preset_name["repetition_penalty"])
            )
            self.repetition_penaltySlider.setValue(
                int(param_preset_name["repetition_penalty"] * 100)
            )

            # Print a message indicating which preset was applied
            print("--- Applied parameter preset:", Path(preset_file).stem)

        # Connect the function to the combo box signal
        self.paramPresets_comboBox.textActivated.connect(lambda: apply_params_preset())


class MagiApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.settings_win = SettingsWindow()

        icon = QIcon()
        icon.addFile(str(APP_ICON), QSize(), QIcon.Normal, QIcon.Off)
        self.setWindowIcon(icon)

        print("--- Launched app")

        self.model_load = False
        self.continue_textgen_mode = False
        self.textgen_mode = "chat_mode"

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

        # Actions from menu
        self.mode_tab.currentChanged.connect(self.mode_tab_manage)

        self.actionPreferences.triggered.connect(self.settings_win.show)
        self.actionExit.triggered.connect(self.close)

        # Status bar
        self.statusbar.showMessage("Status: Ready")

        # Textgen button clicks
        self.generateButton.clicked.connect(self.textgen_switcher)
        self.continueButton.clicked.connect(self.continue_textgen)
        self.clearButton.clicked.connect(self.clear_histories)
        self.stopButton.clicked.connect(self.stop_textgen)
        self.rewindButton.clicked.connect(self.chat_rewind)
        self.retryButton.clicked.connect(self.retry_button_manage)

        # Load/unload backend
        self.loadModelButton.clicked.connect(self.load_model)
        self.unloadModelButton.clicked.connect(self.unload_model)

        # self.paramWinShowButton.clicked.connect(self.settings_win.show)

        self.settingsPathSaveButton.clicked.connect(self.save_settings)

        # Select the models
        self.cppModelSelect.clicked.connect(self.cpp_model_select)
        self.exllamaModelSelect.clicked.connect(self.exllama_model_select)

        # Clear chat history and set the context
        self.instructPresetComboBox.textActivated.connect(
            partial(self.chat_preset_refresh, "instruct")
        )
        self.characterPresetComboBox.textActivated.connect(
            partial(self.chat_preset_refresh, "character")
        )

        self.awesomePresetComboBox.textActivated.connect(self.awesome_prompts)

        self.chatInputHistoryCombo.textActivated.connect(
            lambda: self.chat_input_history_set()
        )

        self.themeDarkCheck.clicked.connect(lambda: self.set_themes("dark"))
        self.themeLightCheck.clicked.connect(lambda: self.set_themes("light"))
        self.themeNativeCheck.clicked.connect(lambda: self.set_themes("native"))

        self.set_preset_params("instruct")

        if self.backendAutoLaunch.isChecked():
            self.load_model()

    def closeEvent(self, event):
        # close the child window when the parent window is closed
        self.settings_win.close()
        event.accept()

    def retry_button_manage(self):
        self.chat_rewind()
        self.textgen_switcher(True)

    def mode_tab_manage(self):
        index = self.mode_tab.currentIndex()

        if index == 0:
            self.textgen_mode = "chat_mode"
            self.chat_preset_refresh("instruct")
        elif index == 1:
            self.textgen_mode = "chat_mode"
            self.chat_preset_refresh("character")
        elif index == 2:
            self.textgen_mode = "standard_mode"
        elif index == 3:
            self.textgen_mode = "notebook_mode"

        self.set_textgen_mode()

    # Set the textgen mode and update the UI accordingly
    def set_textgen_mode(self):
        self.continueButton.setEnabled(False)

        # Use a dictionary to map the textgen modes to the UI settings
        ui_settings = {
            "chat_mode": {
                "input_enabled": True,
                "output_readonly": True,
                "chat_history_enabled": True,
                "rewind_enabled": self.model_load,
            },
            "standard_mode": {
                "input_enabled": True,
                "output_readonly": True,
                "chat_history_enabled": False,
                "rewind_enabled": False,
            },
            "notebook_mode": {
                "input_enabled": False,
                "output_readonly": False,
                "chat_history_enabled": False,
                "rewind_enabled": False,
            },
        }

        # Get the UI settings based on the textgen mode
        settings = ui_settings.get(self.textgen_mode)

        # Update the UI widgets with the settings
        self.inputText.setEnabled(settings["input_enabled"])
        self.outputText.setReadOnly(settings["output_readonly"])
        self.chatInputHistoryCombo.setEnabled(settings["chat_history_enabled"])

        # Clear all histories
        self.clear_histories()

    # Set themes
    def set_themes(self, theme):
        extra = {"pyside6": True, "density_scale": "-1", "font_family": ""}

        if theme == "dark":
            apply_stylesheet(
                app,
                theme="dark_lightgreen.xml",
                css_file="assets/dark_theme.css",
                extra=extra,
            )
        if theme == "light":
            apply_stylesheet(
                app,
                theme="light_lightgreen.xml",
                css_file="assets/light_theme.css",
                extra=extra,
                invert_secondary=False,
            )
        if theme == "native":
            app.setStyleSheet("")
        print("--- Set theme to:", theme)

    def load_presets(self, directory, combo_box):
        # Load presets from a given directory and populate a combo box.
        presets = glob.glob(f"{directory}/*.yaml")
        presets = sorted(presets)  # sort the list of files alphabetically

        for preset in presets:
            preset_stem = Path(preset).stem
            combo_box.addItem(preset_stem)

    def load_prompts(self, filename):
        # Load prompts from a CSV file and populate a combo box.
        with open(filename, "r", encoding="utf-8") as csvfile:
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

        self.botNameLine.setText(config["Settings"]["bot_name"])
        self.yourNameLine.setText(config["Settings"]["user_name"])

        # Set backend based on the value from the settings section
        if config["Settings"]["backend"] == "llama_cpp_python":
            self.cppCheck.setChecked(True)
        elif config["Settings"]["backend"] == "llama_cpp_server":
            self.cppServerCheck.setChecked(True)
        elif config["Settings"]["backend"] == "exllama":
            self.exllamaCheck.setChecked(True)

        # Set theme based on the value from the settings section
        if config["Settings"]["theme"] == "dark":
            self.themeDarkCheck.setChecked(True)
        elif config["Settings"]["theme"] == "light":
            self.themeLightCheck.setChecked(True)
        elif config["Settings"]["theme"] == "native":
            self.themeNativeCheck.setChecked(True)

        # Set themes by calling set_themes method with theme argument
        self.set_themes(config["Settings"]["theme"])

        auto_launch_backend = eval(config["Settings"]["auto_launch_backend"])
        self.backendAutoLaunch.setChecked(auto_launch_backend)

    # Define a helper function to get the file path from a dialog
    def get_file_path(self, title, filter):
        file_path = QFileDialog.getOpenFileName(self, title, "", filter)[0]
        return file_path

    # Define a helper function to get the directory path from a dialog
    def get_directory_path(self, title):
        directory_path = str(QFileDialog.getExistingDirectory(self, title))
        return directory_path

    # Browse for the GGUF/GGML model
    def cpp_model_select(self):
        cpp_model = self.get_file_path("Open file", "GGUF/GGML models (*.bin *.gguf)")
        if cpp_model:
            self.cppModelPath.setText(cpp_model)

    # Browse for the exllama model
    def exllama_model_select(self):
        exllama_model = self.get_directory_path("Select Directory")
        if exllama_model:
            self.exllamaModelPath.setText(exllama_model)

    # Save the current settings to an INI file
    def save_settings(self):
        # Create a ConfigParser object
        config = configparser.ConfigParser()
        # Read the existing settings from the file
        config.read(SETTINGS_FILE)

        # Set the values for the settings section based on the widgets
        config.set("Settings", "cpp_model_path", self.cppModelPath.text())
        config.set("Settings", "exllama_model_path", self.exllamaModelPath.text())

        config.set("Settings", "user_name", self.yourNameLine.text())
        config.set("Settings", "bot_name", self.botNameLine.text())

        config.set(
            "Settings", "auto_launch_backend", str(self.backendAutoLaunch.isChecked())
        )

        # Save backend based on the checked radio button
        if self.cppCheck.isChecked():
            config.set("Settings", "backend", "llama_cpp_python")
        elif self.cppServerCheck.isChecked():
            config.set("Settings", "backend", "llama_cpp_server")
        elif self.exllamaCheck.isChecked():
            config.set("Settings", "backend", "exllama")

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

        print("--- Settings saved")

    def history_readonly_logic(self, readonly_mode: bool):
        # Invert readonly_mode for buttons
        button_mode = not readonly_mode

        # A list of buttons to enable or disable based on the button mode
        buttons = [
            self.instructPresetComboBox,
            self.characterPresetComboBox,
            self.streamEnabledCheck,
            self.continueButton,
            self.generateButton,
            self.clearButton,
        ]

        if self.textgen_mode == "chat_mode":
            buttons.append(self.rewindButton)
            buttons.append(self.retryButton)

        # Iterate over the buttons and set their enabled status
        for button in buttons:
            button.setEnabled(button_mode)

    # Stop button logic
    def stop_textgen(self):
        self.textgenThread.stop()

        self.stopButton.setEnabled(False)

    # Continue button logic
    def continue_textgen(self, text_tab):
        if self.unloadModelButton.isEnabled():
            # Get the history text from the corresponding tab
            history_text = self.outputText.toPlainText()
            if history_text:
                self.continue_textgen_mode = True
                backend = self.get_current_backend()
                # Launch the backend with the history text and the run backend
                self.launch_backend(history_text, backend)

    def insert_text_and_scroll(self, text_widget, text):
        # Define a helper function to insert text and scroll to the end of a text widget
        cursor = text_widget.textCursor()
        cursor.movePosition(QTextCursor.End)  # Move it to the end
        cursor.insertText(text)
        text_widget.verticalScrollBar().setValue(
            text_widget.verticalScrollBar().maximum()
        )

    @Slot(str)
    def handleResult(self, reply):
        # Get the text widget from the textgen mode
        text_widget = self.outputText

        # Insert the reply and scroll to the end
        self.insert_text_and_scroll(text_widget, reply)

    # Handle the final response from textgen
    @Slot(str)
    def final_handleResult(self, final_text):
        # Remove the trailing "USER:" if present
        final_text = final_text.rstrip("USER:")

        if self.textgen_mode == "chat_mode":
            if self.continue_textgen_mode:
                # Append the final text to the last message in the history
                updated = str(
                    (self.message_history[-1].rstrip()) + final_text.rstrip() + "\n\n"
                )
                self.message_history[-1] = updated
                self.chat_output_list.pop(-1)
                self.continue_textgen_mode = False
            else:
                # Add a new message to the history with an optional prefix
                prefix = (
                    self.customResponsePrefix.text()
                    if self.customResponsePrefixCheck.isChecked()
                    else ""
                )
                self.message_history.append(prefix + final_text.rstrip() + "\n\n")

            # Write chatlog with write_chatlog, no new session
            if self.logChatCheck.isChecked():
                self.write_chatlog(False)

            self.chat_output_list.append(self.outputText.toHtml())

        self.statusbar.showMessage(f"Status: Generation complete")
        self.history_readonly_logic(False)

        # Stop the textgen thread
        self.stop_textgen()

    def write_chatlog(self, new_session):
        # Write chat log
        current_date = self.get_chat_date()
        log_text = ""

        if not new_session:
            # Get the last two messages from the history
            log_text = (
                self.name_history[-2]
                + self.message_history[-2]
                + self.name_history[-1]
                + self.message_history[-1]
            )
        else:
            # Start a new session with a separator
            log_text = "\n############ New session ############\n"

        # Append the log text to the file with the current date
        with open(f"logs/chat_{current_date}.txt", "a", encoding="utf-8") as f:
            f.write("\n" + log_text)
        print("--- Wrote chat log")

    # Get and set the chat stop strings
    def get_stop_strings(self):
        stop_strings = []
        chat_preset = self.get_chat_presets()
        if self.sendStopStringCheck.isChecked():
            if self.mode_tab.currentIndex() == 0:
                stop_strings.append(chat_preset["user"])
            elif self.mode_tab.currentIndex() == 1:
                user_name, bot_name = self.get_user_bot_names()
                stop_strings.append(user_name + ":")
                stop_strings.append(bot_name + ":")
        # print(stop_strings)
        return stop_strings

    # Get the llama.cpp parameters
    def get_llama_cpp_params(self):
        stop_strings = self.get_stop_strings()

        cpp_params = {
            "max_new_tokens": int(self.settings_win.max_new_tokensSpin.value()),
            "temperature": float(self.settings_win.temperatureSpin.value()),
            "top_p": float(self.settings_win.top_pSpin.value()),
            "top_k": int(self.settings_win.top_kSpin.value()),
            "repetition_penalty": float(
                self.settings_win.repetition_penaltySpin.value()
            ),
            "mirostat_mode": int(self.settings_win.cppMirostatMode.value()),
            "mirostat_tau": int(self.settings_win.cppMirostatTau.value()),
            "mirostat_eta": float(self.settings_win.cppMirostatEta.value()),
            "stop": list(stop_strings),
            "tfs_z": float(self.settings_win.cpp_tfszSpin.value()),
            "frequency_penalty": float(self.settings_win.freqPenaltySpin.value()),
            "presence_penalty": float(self.settings_win.presencePenaltySpin.value()),
            "typical_p": self.settings_win.typical_pSpin.value(),        }

        cpp_params["server_cache_check"] = self.settings_win.cppCacheCheck.isChecked()

        # print('--- cpp_params:', cpp_params)
        return cpp_params

    # Get the Exllama parameters
    def get_exllama_params(self):
        stop_string = self.get_stop_strings()

        exllama_params = {
            "max_new_tokens": self.settings_win.max_new_tokensSpin.value(),
            "temperature": self.settings_win.temperatureSpin.value(),
            "top_p": self.settings_win.top_pSpin.value(),
            "repetition_penalty": self.settings_win.repetition_penaltySpin.value(),
            "top_k": self.settings_win.top_kSpin.value(),
            "typical_p": self.settings_win.typical_pSpin.value(),
            "num_beams": self.settings_win.numbeamsSpin.value(),
            "beam_length": self.settings_win.beamLengthSpin.value(),
            "min_p": self.settings_win.minPSpin.value(),
            "token_repetition_penalty_sustain": self.settings_win.token_repetition_penalty_decaySpin.value(),
            "stop": stop_string,
            "max_seq_len": self.settings_win.ctxsizeSpin.value(),
            "exllama_lora_check": self.settings_win.exllamaLoraCheck.isChecked(),
        }

        if self.settings_win.exllamaLoraCheck.isChecked():
            exllama_params["exllama_lora_directory"] = self.get_model_path(
                self.settings_win.exllamaLora
            )

        # print('--- exllama_params:', exllama_params)
        return exllama_params

    # Get data for chat log save
    def get_chat_date(self):
        today = datetime.today()
        day = today.day
        month = today.month
        year = today.year
        return f"{day}-{month}-{year}"

    # Get chat presets from a YAML file
    def get_chat_presets(self):
        if self.mode_tab.currentIndex() == 0:
            chat_mode = "instruct"

        elif self.mode_tab.currentIndex() == 1:
            chat_mode = "character"

        preset_name = getattr(self, chat_mode + "PresetComboBox").currentText()
        preset_file = f"presets/{chat_mode}/{preset_name}.yaml"
        with open(preset_file, "r") as file:
            chat_preset = yaml.safe_load(file)
        if self.mode_tab.currentIndex() == 1:
            user_name = (
                self.yourNameLineChar.text() if self.yourNameLineChar.text() else "User"
            )
            chat_preset["context"] = chat_preset["context"].replace(
                "{{user}}", user_name
            )
            chat_preset["context"] = chat_preset["context"].replace(
                "{{char}}", chat_preset["name"]
            )
        return chat_preset

    def get_model_path(self, line_edit):
        # Get the model path from a line edit widget
        model_path = line_edit.text().strip()
        return model_path

    @Slot(bool)
    def loadModel_handleResult(self, response):
        if response:
            model_stem = Path(self.cppModelPath.text()).stem
            if not self.cppServerCheck.isChecked():
                print(f"--- Status: Loaded model '{model_stem}'")
                self.statusbar.showMessage(f"--- Status: Loaded model '{model_stem}'")

            self.generateButton.setEnabled(True)
            self.unloadModelButton.setEnabled(True)
            self.toggle_backend_visibility(False)
        else:
            print("---Error: Model load failure...")
            self.statusbar.showMessage("Error: Model load failure")
            self.toggle_backend_visibility(True)

    def get_exllama_model_params(self):
        # Get the Exllama model parameters from the settings window
        exllama_model_params = {
            "model_path": self.get_model_path(self.exllamaModelPath),
            "gpu_split": self.settings_win.exllamaGpuSplitCheck.isChecked(),
            "max_seq_len": self.settings_win.ctxsizeSpin.value(),
            "compress_pos_emb_check": self.settings_win.compressPosEmbedCheck.isChecked(),
        }

        if self.settings_win.exllamaGpuSplitCheck.isChecked():
            exllama_model_params[
                "gpu_split_values"
            ] = self.settings_win.exllamaGpuSplitLine.text()
        if self.settings_win.compressPosEmbedCheck.isChecked():
            exllama_model_params[
                "compress_pos_emb"
            ] = self.settings_win.compressPosEmbedSpin.value()

        return exllama_model_params

    def get_cpp_model_params(self):
        # Get the cpp model parameters from the settings window
        cpp_model_params = {
            "model_path": self.get_model_path(self.cppModelPath),
            "seed": self.settings_win.seedSpin.value(),
            "n_threads": self.settings_win.cppThreads.value(),
            "n_batch": self.settings_win.cppBatchSizeSpin.value(),
            "n_ctx": self.settings_win.ctxsizeSpin.value(),
            "use_mmap": self.settings_win.cppMmapCheck.isChecked(),
            "use_mlock": self.settings_win.cppMlockCheck.isChecked(),
            "verbose": self.settings_win.cppVerboseCheck.isChecked(),
        }

        if self.settings_win.gpuAccelCheck.isChecked():
            cpp_model_params["n_gpu_layers"] = self.settings_win.gpuLayersSpin.value()
        if self.settings_win.cppLoraLineEdit.text():
            cpp_model_params["lora_path"] = self.get_model_path(
                self.settings_win.cppLoraLineEdit
            )
        return cpp_model_params

    def toggle_backend_visibility(self, mode: bool):
        # Enable or disable the backend widgets based on the mode
        self.cppCheck.setEnabled(mode)
        self.exllamaCheck.setEnabled(mode)
        self.cppServerCheck.setEnabled(mode)
        self.loadModelButton.setEnabled(mode)

    def load_model(self):
        # Load a model based on its name
        backend = self.get_current_backend()

        # Get the model parameters for each backend
        cpp_model_params = self.get_cpp_model_params()
        exllama_model_params = self.get_exllama_model_params()

        # Print the model parameters for debugging
        print(
            f"--- {backend} model load parameters:",
            locals().get(f"{backend}_model_params"),
        )

        # Check if the backend has a model to load
        if backend in (LLAMA_CPP, EXLLAMA):
            print(f"--- Loading {backend} model...")
            self.statusbar.showMessage(f"Status: Loading {backend} model...")

            llama_cpp_cache = self.settings_win.cppCacheCheck.isChecked()

            # Start a thread to load the model asynchronously
            self.load_modelThread = LoadModelThread(
                backend,
                cpp_model_params,
                exllama_model_params,
                llama_cpp_cache,
            )
            self.load_modelThread.final_resultReady.connect(self.loadModel_handleResult)
            self.load_modelThread.finished.connect(self.load_modelThread.deleteLater)
            self.load_modelThread.start()

            # Disable the backend widgets while loading
            self.toggle_backend_visibility(False)

            # Set the model load flag to True
            self.model_load = True

        else:
            self.loadModel_handleResult(True)

    def unload_model(self):
        # Delete the global model variable and free any memory if needed
        backend = self.get_current_backend()

        if backend == LLAMA_CPP:
            global cpp_model
            del cpp_model
        elif backend == EXLLAMA:
            global exllama_model
            del exllama_model
            from exllama_generate import exllama_free_memory
            exllama_free_memory()

        print(f"--- Unloaded {backend} model")
        self.statusbar.showMessage(f"Status: Unloaded {backend} model")

        # Set the model load flag to False
        self.model_load = False

        # Enable the backend widgets after unloading
        self.toggle_backend_visibility(True)

        # Disable the unload and generate buttons
        self.unloadModelButton.setEnabled(False)
        self.generateButton.setEnabled(False)

    def set_textgen_things(self):
        # Enable the stop buttons for each mode
        self.stopButton.setEnabled(True)

    def get_user_bot_names(self):
        if self.mode_tab.currentIndex() == 0:
            user_name = (
                self.yourNameLine.text() if self.yourNameLine.text() else "Assistant"
            )
            bot_name = self.botNameLine.text() if self.botNameLine.text() else "User"
        elif self.mode_tab.currentIndex() == 1:
            chat_preset = self.get_chat_presets()
            bot_name = chat_preset["name"]
            user_name = (
                self.yourNameLineChar.text() if self.yourNameLineChar.text() else "User"
            )
        return user_name, bot_name

    # Formatting the chat display text
    def chat_formatting(self, input_message):
        # Get the chat input and strip any leading or trailing whitespace
        chat_input = input_message.strip()
        # Create a list of paragraphs for the text history
        paragraphs = []
        # Add a paragraph with the user name and chat input

        user_name, bot_name = self.get_user_bot_names()

        paragraphs.append(
            f"<b style='color: #a92828'>{user_name}</b><br>{chat_input}<br>"
        )
        # Add a paragraph with the bot name and custom response prefix if checked
        prefix = (
            self.customResponsePrefix.text()
            if self.customResponsePrefixCheck.isChecked()
            else ""
        )
        paragraphs.append(f"<b style='color: #3194d0'>{bot_name}</b><br>{prefix}")
        # Join the paragraphs with line breaks and wrap them in <p> tags
        chat_text = f"<p><br>{'<br>'.join(paragraphs)}</p>".strip()

        return chat_text

    def get_current_backend(self):
        # Use a dictionary to map the check boxes to the backend names
        check_boxes = {
            self.cppCheck: LLAMA_CPP,
            self.cppServerCheck: LLAMA_CPP_SERVER,
            self.exllamaCheck: EXLLAMA,
        }

        # Return the first checked check box's corresponding backend name
        for check_box, backend in check_boxes.items():
            if check_box.isChecked():
                return backend

    # Main launcher logic
    def textgen_switcher(self, retry=False):
        backend = self.get_current_backend()

        # Get the input message from the input widget
        if self.textgen_mode != "notebook_mode":
            if retry:
                input_message = self.chat_input_history[-1]
            else:
                input_message = self.inputText.toPlainText()
                self.chat_input_history_add(input_message)
        else:
            input_message = self.outputText.toPlainText()

        # If the input message is not empty
        if input_message:
            if self.textgen_mode == "standard_mode":
                # Set the default mode text history widget to show the input message
                self.outputText.setPlainText(input_message)
            elif self.textgen_mode == "chat_mode":
                # Generate the final prompt for the chat mode
                final_prompt = self.prompt_generation()

                # Replace newlines with HTML line breaks in the input message
                input_message = input_message.strip().replace("\n", "<br>")
                # Format the chat text with the user and bot names and prefixes
                chat_text = self.chat_formatting(input_message)

                # Append the chat text to the chat mode text history widget
                self.outputText.append(chat_text)

                # Clear the chat mode text input widget
                self.inputText.clear()

                # Use the final prompt as the input message for launching the backend
                input_message = final_prompt

            # Launch the backend with the input message and the backend name
            self.launch_backend(input_message, backend)

    def launch_backend(self, message, backend):
        # Get the exllama and cpp parameters from their respective methods
        exllama_params = self.get_exllama_params()
        cpp_params = self.get_llama_cpp_params()

        self.statusbar.showMessage("Status: Generating...")

        # Create a thread to run the text generation asynchronously
        self.textgenThread = TextgenThread(
            exllama_params,
            message,
            self.streamEnabledCheck.isChecked(),
            backend,
            cpp_params,
        )

        # Connect signals and slots
        self.textgenThread.resultReady.connect(self.handleResult)
        self.textgenThread.final_resultReady.connect(self.final_handleResult)
        self.textgenThread.finished.connect(self.textgenThread.deleteLater)

        # Start the thread
        self.textgenThread.start()

        # Set some attributes and methods related to text generation
        self.set_textgen_things()

        # Set the history to read-only mode
        self.history_readonly_logic(True)

    # Define a function to process the turn template for chat mode
    def process_instruct_turn_template(self):
        if self.mode_tab.currentIndex() == 0:
            chat_preset = self.get_chat_presets()
            first_turn_template = str(chat_preset["turn_template"])

        elif self.mode_tab.currentIndex() == 1:
            chat_preset = self.get_chat_presets()
            first_turn_template = (
                "<|user|>: <|user-message|>\n\n<|bot|>:<|bot-message|>\n"
            )

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
        turn_template = first_turn_template.replace(template_user, "").replace(
            template_user_msg, ""
        )
        turn_template = turn_template.split("<|bot-message|>")
        # Get the first part of the turn template as the bot template
        template_bot = turn_template[0]

        # Get the remaining part of the turn template as the bot message template
        template_bot_msg = (
            first_turn_template.replace(template_user, "")
            .replace(template_user_msg, "")
            .replace(template_bot, "")
        )

        if self.mode_tab.currentIndex() == 0:
            user = template_user.replace("<|user|>", chat_preset["user"])
            bot = template_bot.replace("<|bot|>", chat_preset["bot"])
        elif self.mode_tab.currentIndex() == 1:
            user_name, bot_name = self.get_user_bot_names()
            user = template_user.replace("<|user|>", user_name)
            bot = template_bot.replace("<|bot|>", bot_name)

            example_dialogue = (
                str(chat_preset["example_dialogue"])
                .replace("{{char}}", bot_name)
                .replace("{{user}}", user_name)
            )

            pre_prompt = f"{pre_prompt}\n\n{example_dialogue}\n"

            # Replace the user message placeholder with the input text from the chat mode text input widget
        user_msg = template_user_msg.replace(
            "<|user-message|>", self.chat_input_history[-1]
        )

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
        prompt = ""
        # Loop through name history and message history lists and concatenate them into prompt string
        for user, msg in zip(self.name_history, self.message_history):
            prompt += user + msg

        # Add pre prompt and prompt strings together and assign to final prompt variable
        final_prompt = pre_prompt + "\n" + prompt + bot

        if self.customResponsePrefixCheck.isChecked():
            final_prompt = final_prompt + self.customResponsePrefix.text()

        # print('==='+final_prompt+'===')
        return final_prompt

    # Undo the last two chat turns and restore the previous chat output
    def chat_rewind(self):
        # If there are at least two items in the name and message history lists
        if len(self.name_history) and len(self.message_history) >= 2:
            # print("--- Chat rewind")
            # Pop the last two names and messages from their respective lists
            self.name_history.pop()
            self.name_history.pop()
            self.message_history.pop()
            self.message_history.pop()
            # Set the chat mode text history widget to show the second last chat output
            self.outputText.setHtml(self.chat_output_list[-2])
            self.outputText.verticalScrollBar().setValue(
                self.outputText.verticalScrollBar().maximum()
            )
            # Pop the last chat output from the list
            self.chat_output_list.pop()

        # If there are no items in the name history list
        if len(self.name_history) == 0:
            # Get the chat preset dictionary from a file
            chat_preset = self.get_chat_presets()
            # Get the context string from the chat preset and strip any whitespace
            pre_prompt = chat_preset["context"].strip()
            # Set the chat mode text history widget to show the context string
            self.outputText.setPlainText(pre_prompt)

    # Add the chat input to the combo box and the history list
    def chat_input_history_add(self, chat_input):
        # Add the first 96 characters of the chat input to the combo box
        self.chatInputHistoryCombo.addItem(str(chat_input[:96]))
        # Append the chat input to the history list
        self.chat_input_history.append(chat_input)

    # Set the chat input field to the saved history
    def chat_input_history_set(self):
        # If there are any items in the combo box
        if self.chatInputHistoryCombo.count() >= 1:
            # Get the text from the history list based on the combo box index
            text = self.chat_input_history[
                int(self.chatInputHistoryCombo.currentIndex())
            ]
            # Set the chat mode text input widget to show the text
            self.inputText.setPlainText(text)

    # Refresh the chat preset based on the mode and partial arguments
    def chat_preset_refresh(self, mode, partial=None):
        if self.textgen_mode == "chat_mode" and len(self.message_history) < 2:
            # Clear the name, message and output lists
            self.name_history = []
            self.message_history = []
            self.chat_output_list = []
            self.outputText.clear()
            # Set the preset parameters by calling set_preset_params method with mode argument
            self.set_preset_params(mode)

    # Clear all histories
    def clear_histories(self):
        self.continueButton.setEnabled(False)
        self.outputText.clear()

        if self.textgen_mode == "chat_mode":
            # If there are any items in the name and message lists
            if len(self.name_history) and len(self.message_history) >= 2:
                # Clear the name, message and output lists
                self.name_history = []
                self.message_history = []
                self.chat_output_list = []

            # Set the preset parameters by calling set_preset_params method without arguments
            self.set_preset_params()

    # Set the preset parameters based on the preset mode argument
    def set_preset_params(self, preset_mode=None):
        # Clear rewind history by creating a new empty list for output list
        self.chat_output_list = []
        # Append the current html of chat mode text history widget to output list
        self.chat_output_list.append(self.outputText.toHtml().strip())

        # Get the chat preset dictionary for the preset mode from a file
        chat_preset = self.get_chat_presets()

        # Get the context string from the chat preset and strip any whitespace
        if self.custSystemCheck.isChecked():
            pre_prompt = self.custSystemText.toPlainText()
        else:
            pre_prompt = str(chat_preset["context"]).strip()

        # Append it to the chat mode text history widget with a line break
        self.outputText.append(pre_prompt)

    # Get awesome prompts from a csv file
    def awesome_prompts(self):
        filename = "presets/prompts.csv"
        with open(filename, "r", encoding="utf-8") as csvfile:
            datareader = csv.reader(csvfile)
            for row in datareader:
                # If the row matches the current text of the awesome preset combo box
                if row[0] == self.awesomePresetComboBox.currentText():
                    # Set the chat mode text input widget to show the prompt from the row
                    self.inputText.setPlainText(row[1])
                    break


if __name__ == "__main__":
    # Create a Qt application instance
    app = QApplication(sys.argv)

    if platform.system() == "Windows":
        app.setStyle("Fusion")

    # Create a chat window instance and show it
    window = MagiApp()
    window.show()

    # Start the Qt event loop
    app.exec()
