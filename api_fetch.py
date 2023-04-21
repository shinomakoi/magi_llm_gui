import json
import random
import string

import requests
import websockets

GRADIO_FN = 34

# tested on commit 49aa05054ae13f381381440a9860ce0d68200e80

# API non-streaming mode


def textgen(params, server, prompt):

    # Input prompt
    payload = json.dumps([prompt, params])

    response = requests.post(f"http://{server}:7860/run/textgen", json={
        "data": [
            payload
        ]
    }).json()

    reply = response["data"][0]
    return reply

# API streaming mode


async def run(context, params, server):

    def random_hash():
        letters = string.ascii_lowercase + string.digits
        return ''.join(random.choice(letters) for i in range(9))


    payload = json.dumps([context, params])
    session = random_hash()

    async with websockets.connect(f"ws://{server}:7860/queue/join") as websocket:
        while content := json.loads(await websocket.recv()):
            # Python3.10 syntax, replace with if elif on older
            match content["msg"]:
                case "send_hash":
                    await websocket.send(json.dumps({
                        "session_hash": session,
                        "fn_index": GRADIO_FN
                    }))
                case "estimation":
                    pass
                case "send_data":
                    await websocket.send(json.dumps({
                        "session_hash": session,
                        "fn_index": GRADIO_FN,
                        "data": [
                            payload
                        ]
                    }))
                case "process_starts":
                    pass
                case "process_generating" | "process_completed":
                    yield content["output"]["data"][0]
                    # You can search for your desired end indicator and
                    #  stop generation by closing the websocket here
                    if (content["msg"] == "process_completed"):
                        break
