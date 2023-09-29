# Magi LLM GUI
A Qt GUI for large language models for Windows, Linux (and Mac?)

Uses Exllama and llama.cpp as backends.


**Installation:**

First make sure Python (3.10+ recommended) and GIT are installed. Then:
```
git clone https://github.com/shinomakoi/magi_llm_gui
cd magi_llm_gui
```
Optionally create a virtual environment (recommended)

```
python -m venv .magi_venv
source ./.magi_venv/bin/activate ### For Linux
.\.magi_venv\Scripts\activate ## For Windows
```
```
pip install -r requirements.txt
```
**llama.cpp**

llama-cpp-python is included as a backend for CPU, but you can optionally install with GPU support, e.g. ```CMAKE_ARGS="-DLLAMA_CUBLAS=on" FORCE_CMAKE=1 pip install llama-cpp-python``` for CUDA acceleration. 
See: 
https://github.com/abetlen/llama-cpp-python/#installation-with-openblas--cublas--clblast--metal

Can also use the llama.cpp server API if it's launched. See: https://github.com/ggerganov/llama.cpp/tree/master/examples/server

**Exllama**

To install Exllama, follow the install instructions at https://github.com/turboderp/exllama inside the magi_llm_gui folder. Also requires CUDA Toolkit installed (installed with Linux package manager or downloaded from NVIDIA for Windows).
```
pip install --pre torch torchvision torchaudio --index-url https://download.pytorch.org/whl/nightly/cu118
pip install safetensors sentencepiece ninja
git clone https://github.com/turboderp/exllama
```

**Usage:**

To launch the Magi LLM GUI, use: 
```
python magi_llm_app.py
```
You can set the generation parameters in Settings > Parameters
![image](https://github.com/shinomakoi/magi_llm_gui/assets/112139428/f39002b9-e450-459c-b2bb-fd3940956fd3)
Uses https://github.com/abetlen/llama-cpp-python for llama.cpp support

Uses https://github.com/UN-GCPDS/qt-material for themes
