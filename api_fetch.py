import json

import requests
import websockets

# API non-streaming mode


def textgen(params, server, prompt):

    server_addr = f'{server}:5000'
    server_url = f'http://{server_addr}/api/v1/generate'

    params["prompt"] = prompt
    request = params

    response = requests.post(server_url, json=request)

    if response.status_code == 200:
        result = response.json()['results'][0]['text']
        final_result = (prompt + result)
        return final_result


async def run(context, params, server):

    server_addr = f'{server}:5005'
    server_url = f'ws://{server_addr}/api/v1/stream'

    params["prompt"] = context
    request = params

    async with websockets.connect(server_url, ping_interval=None) as websocket:
        await websocket.send(json.dumps(request))

        yield context  # Remove this if you just want to see the reply

        while True:
            incoming_data = await websocket.recv()
            incoming_data = json.loads(incoming_data)

            match incoming_data['event']:
                case 'text_stream':
                    yield incoming_data['text']
                case 'stream_end':
                    return
