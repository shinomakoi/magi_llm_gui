
import sys
from pathlib import Path

import torch

# Add the exllama module to the system path
sys.path.insert(0, str(Path("exllama")))

# Import the necessary classes from exllama
from exllama.tokenizer import ExLlamaTokenizer
from exllama.model import ExLlama, ExLlamaCache, ExLlamaConfig
from exllama.generator import ExLlamaGenerator

# Define some constants for paths and extensions
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

    # Generate text from a given context and parameters
    def generate(self, context, params):
        # Disable gradient computation and initialize CUDA device
        torch.set_grad_enabled(False)
        torch.cuda._lazy_init()

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

        # Generate text using the generator
        text = generator.generate_simple(
            context, max_new_tokens=params["max_new_tokens"]
        )
        return text

    def generate_with_streaming(self, context, params):

        # Disable gradient computation and initialize CUDA device
        torch.set_grad_enabled(False)
        torch.cuda._lazy_init()

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

  
        # Encode the context into ids using the tokenizer
        ids = generator.tokenizer.encode(context)

        # Prevent going over context limit. Refine this later by pruning context
        if ids.shape[-1] >= 2048:
            print('Warning: Context limit exceeded')
            yield ''
            return

        # Begin the generation process with the ids
        generator.gen_begin(ids)

        # Get the initial length of the sequence
        initial_len = generator.sequence[0].shape[0]

        min_response_tokens = 4
        generator.begin_beam_search()

        # Generate tokens one by one and yield them as text
        for i in range(params["max_new_tokens"]):

            if i < min_response_tokens:
                generator.disallow_tokens(
                    [generator.tokenizer.newline_token_id, generator.tokenizer.eos_token_id])
            else:
                generator.disallow_tokens(None)

            token = generator.gen_single_token()
            if token.item() == generator.tokenizer.eos_token_id:
                # Replace it with a newline token
                generator.replace_last_token(
                    generator.tokenizer.newline_token_id)
                break

            yield (generator.tokenizer.decode(generator.sequence[0][initial_len:]))

      # End the previous beam search if any
        generator.end_beam_search()

    def encode(self, string, **kwargs):
        # Encode a string into ids using the tokenizer
        return self.tokenizer.encode(string)
