import json
import random
import string

import requests
import websockets


# API non-streaming mode
def textgen(params, server, prompt='Tea is the best drink there is because'):

    payload = json.dumps([prompt, params])

    response = requests.post(f"http://{server}:7860/run/textgen", json={
        "data": [
            payload
        ]
    }).json()

    reply = response["data"][0]
    # print(reply)
    return reply


# API Streaming mode
async def run(context, params, server):

    def random_hash():
        letters = string.ascii_lowercase + string.digits
        return ''.join(random.choice(letters) for i in range(9))


    session = random_hash()

    async with websockets.connect(f"ws://{server}:7860/queue/join") as websocket:
        while content := json.loads(await websocket.recv()):
            # Python3.10 syntax, replace with if elif on older
            match content["msg"]:
                case "send_hash":
                    await websocket.send(json.dumps({
                        "session_hash": session,
                        "fn_index": 12
                    }))
                case "estimation":
                    pass
                case "send_data":
                    await websocket.send(json.dumps({
                        "session_hash": session,
                        "fn_index": 12,
                        "data": [
                            context,
                            params['max_new_tokens'],
                            params['do_sample'],
                            params['temperature'],
                            params['top_p'],
                            params['typical_p'],
                            params['repetition_penalty'],
                            params['encoder_repetition_penalty'],
                            params['top_k'],
                            params['min_length'],
                            params['no_repeat_ngram_size'],
                            params['num_beams'],
                            params['penalty_alpha'],
                            params['length_penalty'],
                            params['early_stopping'],
                            params['seed'],
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
