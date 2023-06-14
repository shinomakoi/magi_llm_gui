# Magi LLM GUI
A Qt GUI for large language models for Windows, Linux (and Mac?)

Uses Exllama, llama.cpp and TextSynth server as backends.


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
./.magi-venv/Scripts/activate ### For Windows
```
```
pip install -r requirements.txt
```
**llama.cpp**

llama-cpp-python is including as a backend for CPU, but you can optionally install with GPU support, e.g. ```CMAKE_ARGS="-DLLAMA_CUBLAS=on" FORCE_CMAKE=1 pip install llama-cpp-python``` for CUDA acceleration. 
See: 
https://github.com/abetlen/llama-cpp-python/#installation-with-openblas--cublas--clblast--metal

**Exllama**

To install Exllama, follow the install instructions at https://github.com/turboderp/exllama inside the magi_llm_gui folder. Also requires CUDA Toolkit installed (installed with Linux package manager or downloaded from NVIDIA for Windows). Tested working on Linux. For Windows, good luck.
```
pip install --pre torch torchvision torchaudio --index-url https://download.pytorch.org/whl/nightly/cu118
pip install safetensors sentencepiece ninja
git clone https://github.com/turboderp/exllama
```
**TextSynth server**

To use the TextSynth backend, download a model and set up according to the documentation at https://bellard.org/ts_server/. Then run the server with ```./ts_server ts_server.cfg``` and enter the 'model' (e.g, "pythia_deduped_1.4B") in the 'TextSynth' tab under File > Parameters. Then you can generate text like with the other backends.

**Usage:**

To launch the Magi LLM GUI, use: 
```
python magi_llm_app.py
```
You can set the generation parameters in File > Parameters

![gfj](https://github.com/shinomakoi/magi_llm_gui/assets/112139428/f0234f46-c765-4e42-9860-d1c07b0beb73)

Uses https://github.com/abetlen/llama-cpp-python for llama.cpp support
