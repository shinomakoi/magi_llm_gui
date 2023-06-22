import sys
from pathlib import Path

import torch

sys.path.insert(0, str(Path("exllama")))

from exllama.tokenizer import ExLlamaTokenizer
from exllama.model import ExLlama, ExLlamaCache, ExLlamaConfig
from exllama.generator import ExLlamaGenerator

# Simple interactive chatbot script
MODEL_EXTENSIONS = [".safetensors", ".pt", ".bin"]


class ExllamaModel:
    def __init__(self):
        # Initialize the attributes of the class to None
        self.config = None
        self.model = None
        self.cache = None
        self.tokenizer = None

    @classmethod
    def from_pretrained(cls, params):

        MODEL_PATH = Path(params["model_path"])
        # Get the paths for the tokenizer model and the model config
        TOKENIZER_MODEL_PATH = MODEL_PATH / "tokenizer.model"
        MODEL_CONFIG_PATH = MODEL_PATH / "config.json"

        # Create an instance of the class from a pretrained model

        # Load the model config from a json file
        config = ExLlamaConfig(str(MODEL_CONFIG_PATH))

        # Find the model file with one of the extensions
        model_path = None
        for ext in MODEL_EXTENSIONS:
            found = list(MODEL_PATH.glob(f"*{ext}"))
            if len(found) > 0:
                # If more than one file is found, use the last one
                if len(found) > 1:
                    print(
                        f"More than one {ext} model has been found. The last one will be selected. It could be wrong."
                    )
                model_path = found[-1]
                print('--- Exllama model:', model_path)
                break

        # Set the model path and max sequence length in the config
        config.model_path = str(model_path)
        config.max_seq_len = 2048

        # Multi-gpu mode
        if params["gpu_split"]:
            config.set_auto_map(params["gpu_split_values"])
            config.gpu_peer_fix = True

        # Create an instance of ExLlama with the config
        model = ExLlama(config)

        # Create an instance of ExLlamaCache with the model
        cache = ExLlamaCache(model)

        # Create an instance of ExLlamaTokenizer with the tokenizer model path
        tokenizer = ExLlamaTokenizer(str(TOKENIZER_MODEL_PATH))

        # Create an instance of ExllamaModel and assign its attributes
        result = cls()
        result.config = config
        result.model = model
        result.cache = cache
        result.tokenizer = tokenizer

        return result

    # Check if exceeded context limit and if so prune it from the start
    def check_token_count(self, in_tokens, max_response_tokens):

        token_count = in_tokens.shape[-1]

        if token_count >= 1024:
            print('--- Exllama context:', token_count, 'tokens')
        if token_count >= 2048:
            print('Context limit reached. Trimming')

            amount_to_trim = (token_count - 2048) + max_response_tokens
            # print('trimming amount', amount_to_trim)
            in_tokens = torch.cat(
                (in_tokens[:, :0], in_tokens[:, amount_to_trim:]), axis=1)
            amount_to_trim = 0
        return in_tokens
        

    def generate_with_streaming(self, context, params):
        # Disable gradient computation and initialize CUDA device
        torch.set_grad_enabled(False)
        torch.cuda._lazy_init()

        # Define some constants for the response length
        min_response_tokens = 4
        max_response_tokens = params["max_new_tokens"]

        # Create an instance of ExLlamaGenerator with the model, tokenizer and cache
        generator = ExLlamaGenerator(self.model, self.tokenizer, self.cache)

        # Set some settings for the generator based on params
        generator.settings.temperature = params["temperature"]
        generator.settings.top_p = params["top_p"]
        generator.settings.top_k = params["top_k"]
        generator.settings.token_repetition_penalty_max = params["repetition_penalty"]
        generator.settings.beams = params["num_beams"]
        generator.settings.min_p = params["min_p"]
        generator.settings.token_repetition_penalty_sustain = params[
            "token_repetition_penalty_sustain"
        ]
        generator.settings.token_repetition_penalty_decay = (
            generator.settings.token_repetition_penalty_sustain // 2
        )
        generator.settings.beam_length = params["beam_length"]
        stop_string = params["stop"]

        # Encode the context into tokens
        in_tokens = generator.tokenizer.encode(context)

        # Trim if needed and check if trimmed
        in_tokens = self.check_token_count(
            in_tokens, max_response_tokens)
        
        context = generator.tokenizer.decode(in_tokens)
        context=context[0]

        # Get the number of tokens in the context
        num_res_tokens = in_tokens.shape[-1]

        if max_response_tokens + num_res_tokens >= 2048:
            max_response_tokens = 2048 - num_res_tokens

        # Feed the tokens to the generator
        generator.gen_feed_tokens(in_tokens)

        # Start the beam search
        generator.begin_beam_search()

        # Initialize an empty response line
        res_line = ''

        # Loop for up to max response tokens
        for i in range(max_response_tokens):

            # Disallow newline and eos tokens if below min response tokens
            if i < min_response_tokens:
                generator.disallow_tokens(
                    [generator.tokenizer.newline_token_id, generator.tokenizer.eos_token_id])
            else:
                generator.disallow_tokens(None)

            # Get a token from the beam search
            gen_token = generator.beam_search()

            # If token is EOS, replace it with newline before continuing
            if gen_token.item() == generator.tokenizer.eos_token_id:
                generator.replace_last_token(
                    generator.tokenizer.newline_token_id)

            # Increment the number of response tokens
            num_res_tokens += 1

            # Decode the current sequence and get the new text added
            text = generator.tokenizer.decode(
                generator.sequence_actual[:, -num_res_tokens:][0])
            new_text = text[len(context):]
            new_text = new_text[len(res_line):]

            # Append the new text to the response line
            res_line += new_text

            # End conditions: break if newline or eos token is generated or if stop string: is reached
            if gen_token.item() in [generator.tokenizer.eos_token_id]:
                break

            # Yield the new text to the caller
            yield new_text

            if res_line.endswith(stop_string):
                plen = generator.tokenizer.encode(stop_string).shape[-1]
                generator.gen_rewind(plen)
                break

        # End the beam search
        generator.end_beam_search()
