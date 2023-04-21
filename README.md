# Magi LLM GUI
A QT GUI for large language models


Currently works with https://github.com/oobabooga/text-generation-webui/ and https://github.com/ggerganov/llama.cpp

Uses https://github.com/abetlen/llama-cpp-python for llama.cpp support

Launch the WebUi with the ```--listen``` flag to enable the text-generation-webui API and add ```--no-stream``` if you don't want to use streaming mode.
Has been tested with commit 49aa05054ae13f381381440a9860ce0d68200e80 for text-generation-webui. 

Install requirements with: 
```
pip install -r requirements.txt
```

Then to launch the Magi LLM GUI, use: 
```
python magi_llm_app.py
```
You can set the generation parameters in File > Parameters

![image](https://user-images.githubusercontent.com/112139428/233437918-8f9b7c2a-dd77-4536-a612-a893a2bc90d4.png)
