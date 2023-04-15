import json
# import random
# import string

import requests
import websockets


# API non-streaming mode
def textgen(params, server, prompt='Tea is the best drink there is because'):

    print('Oobabooga prompt:', prompt)

    # Input prompt
    payload = json.dumps([prompt, params])

    response = requests.post(f"http://{server}:7860/run/textgen", json={
        "data": [
            payload
        ]
    }).json()

    reply = response["data"][0]
    # print(reply)
    return reply

async def run(context, params, server):

    params['prompt'] = context

    async with websockets.connect(f"ws://{server}:5000/api/v1/stream") as websocket:
        await websocket.send(json.dumps(params))

        while incoming_data := json.loads(await websocket.recv()):
            match incoming_data['event']:
                case 'text_stream':
                    yield incoming_data['text']
                case 'stream_end':
                    return
