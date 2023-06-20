import json

import requests

# Constants for the URL and the data prefix
URL = "http://127.0.0.1:8080/completion"
DATA_PREFIX = "data: "


def create_data(prompt: str, cpp_params: dict, stream: bool = False) -> str:

    data = {
        "prompt": prompt,
        "max_tokens": cpp_params["max_new_tokens"],
        "temperature": cpp_params["temperature"],
        "top_p": cpp_params["top_p"],
        "top_k": cpp_params["top_k"],
        "repeat_penalty": cpp_params["repetition_penalty"],
        "mirostat_mode": cpp_params["mirostat_mode"],
        "stop": cpp_params["stop"],
        "tfs_z": cpp_params["tfs_z"],
        "stream": stream,
    }
    return json.dumps(data)


def generate_nostream(prompt: str, cpp_params: dict) -> str:

    data = create_data(prompt, cpp_params)

    # Make a POST request without streaming
    try:
        result = requests.post(URL, data=data)
        result.raise_for_status()
        final = result.json().get("content", "")
        return final
    except requests.exceptions.RequestException as e:
        print(f"Failed to generate response: {e}")
        return ""


def generate_with_streaming(prompt: str, cpp_params: dict):

    data = create_data(prompt, cpp_params, stream=True)

    # Make a POST request with streaming
    try:
        response = requests.post(URL, stream=True, data=data)
        response.raise_for_status()

        # Iterate over the response content as JSON objects
        for line in response.iter_lines():
            # Skip empty lines
            if line:
                decoded_line = line.decode("utf8")
                if decoded_line.startswith(DATA_PREFIX):
                    json_data = json.loads(decoded_line[len(DATA_PREFIX):])
                    final = json_data["content"]
                    yield final
    except requests.exceptions.RequestException as e:
        print(f"Failed to generate response: {e}")
        yield ""
