# Magi LLM GUI
A QT GUI for large language models

Currently works with https://github.com/oobabooga/text-generation-webui/

Launch the WebUi with the ```--listen``` flag to enable the API and add ```--no-stream``` if you don't want to use streaming mode.

Install requirements with: 
```
pip install -r requirements.txt
```

Then to launch the Magi LLM GUI, use: 
```
python magi_llm_app.py
```

Note: streaming mode is broken the latest commit in the WebUi. Use: 
```
git checkout 378d21e80c3d6f11a4835e57597c69e340008e2c 
```
to get it working.
