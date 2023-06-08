import sys
from pathlib import Path

import torch

sys.path.insert(0, str(Path("exllama")))

# Import the ExLlama modules
from exllama.generator import ExLlamaGenerator
from exllama.model import ExLlama, ExLlamaCache, ExLlamaConfig
from exllama.tokenizer import ExLlamaTokenizer


# Define a class for the ExLlama model
class ExllamaModel:
    def __init__(self):
        pass

    @classmethod
    def from_pretrained(self, path_to_model):
        # Load the model and the tokenizer from a pretrained path
        # Convert the path to a Path object
        path_to_model = Path(path_to_model)
        # Get the paths for the tokenizer model and the model config
        tokenizer_model_path = path_to_model / "tokenizer.model"
        model_config_path = path_to_model / "config.json"

        # Find the model checkpoint
        model_path = None
        # Loop through the possible extensions
        for ext in ['.safetensors', '.pt', '.bin']:
            # Find all the files with that extension in the path
            found = list(path_to_model.glob(f"*{ext}"))
            # If there are any files found
            if len(found) > 0:
                # If there are more than one file found
                if len(found) > 1:
                    # Print a warning message that the last one will be selected
                    print(
                        f'More than one {ext} model has been found. The last one will be selected. It could be wrong.')

                # Set the model path to the last file found
                model_path = found[-1]
                print(model_path)
                # Break the loop
                break

        # Load the config from the config path and set some attributes
        config = ExLlamaConfig(str(model_config_path))
        config.model_path = str(model_path)
        config.max_seq_len = 2048
        # Load the model from the config
        model = ExLlama(config)
        # Create a cache for the model
        cache = ExLlamaCache(model)
        # Load the tokenizer from the tokenizer model path
        tokenizer = ExLlamaTokenizer(str(tokenizer_model_path))

        # Create an instance of this class and set its attributes
        result = self()
        result.config = config
        result.model = model
        result.cache = cache
        result.tokenizer = tokenizer

        # Return a tuple of the instance and itself (why?)
        return result, result

    def generate(self, context, params):
        # Generate text from a given context and parameters

        # Disable gradient computation and initialize CUDA if available
        torch.set_grad_enabled(False)
        torch.cuda._lazy_init()

        # Create a generator object with the model, tokenizer and cache
        generator = ExLlamaGenerator(self.model, self.tokenizer, self.cache)
        # Set the generator settings from the parameters dictionary
        generator.settings.temperature = params["temperature"]
        generator.settings.top_p = params["top_p"]
        generator.settings.top_k = params["top_k"]
        generator.settings.token_repetition_penalty_max = params["repetition_penalty"]
        generator.settings.beams = params["num_beams"]

        generator.settings.min_p = params["min_p"]
        generator.settings.token_repetition_penalty_sustain = params[
            "token_repetition_penalty_sustain"]
        generator.settings.token_repetition_penalty_decay = generator.settings.token_repetition_penalty_sustain // 2
        generator.settings.beam_length = params["beam_length"]

        # Generate text using the simple method with the context and max new tokens limit
        text = generator.generate_simple(
            context, max_new_tokens=params["max_new_tokens"])

        # Return the generated text
        return text
    
        # Generate text from a given context and parameters using streaming
    def generate_with_streaming(self, context, params):

        # Disable gradient computation and initialize CUDA if available
        torch.set_grad_enabled(False)
        torch.cuda._lazy_init()

        # Create a generator object with the model, tokenizer and cache
        generator = ExLlamaGenerator(self.model, self.tokenizer, self.cache)
        # Set the generator settings from the parameters dictionary
        generator.settings.temperature = params["temperature"]
        generator.settings.top_p = params["top_p"]
        generator.settings.top_k = params["top_k"]
        generator.settings.token_repetition_penalty_max = params["repetition_penalty"]
        generator.settings.beams = params["num_beams"]

        generator.settings.min_p = params["min_p"]
        generator.settings.token_repetition_penalty_sustain = params[
            "token_repetition_penalty_sustain"]
        generator.settings.token_repetition_penalty_decay = generator.settings.token_repetition_penalty_sustain // 2
        generator.settings.beam_length = params["beam_length"]

        # End the beam search if it is still running
        generator.end_beam_search()
        # Encode the context into ids
        ids = generator.tokenizer.encode(context)
        # Begin the generation with the ids
        generator.gen_begin(ids)
        # Get the initial length of the sequence
        initial_len = generator.sequence[0].shape[0]
        # Create an empty list for all tokens
        all_tokens = []

        # Loop through the max new tokens limit
        for i in range(params["max_new_tokens"]):
            # Generate a single token
            token = generator.gen_single_token()
            # Yield the decoded sequence from the initial length to the end
            yield (generator.tokenizer.decode(generator.sequence[0][initial_len:]))

            # If the token is the end of sentence token
            if token.item() == generator.tokenizer.eos_token_id:
                # Replace it with a newline token
                generator.replace_last_token(
                    generator.tokenizer.newline_token_id)
                break

    def encode(self, string, **kwargs):
        # Encode a string into ids using the tokenizer
        return self.tokenizer.encode(string)
