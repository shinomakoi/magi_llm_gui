import json

import requests


def generate(prompt, cpp_params):
    # Define the URL and the data to send
    url = "http://127.0.0.1:8080/completion"
    data = json.dumps({
        "prompt": prompt,
        "max_tokens": cpp_params["max_new_tokens"],
        "temperature": cpp_params["temperature"],
        "top_p": cpp_params["top_p"],
        "top_k": cpp_params["top_k"],
        "repeat_penalty": cpp_params["repetition_penalty"],
        "mirostat_mode": cpp_params["mirostat_mode"],
        "stop": cpp_params["stop"],
        "tfs_z": cpp_params["tfs_z"],
        "stream": True,
    })

    # Make a POST request with streaming
    response = requests.post(url, stream=True, data=data)
    if not response.ok:
        return
    # Iterate over the response content as JSON objects
    for line in response.iter_lines():
        # Skip empty lines
        if line:
            decoded_line = line.decode("utf8")
            if decoded_line.startswith("data: "):
                message = decoded_line[6:]
                json_data = json.loads(message)
                final = json_data['content']
                yield final
