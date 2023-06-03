import sys
from pathlib import Path

import torch

from exllama.generator import ExLlamaGenerator
from exllama.model import ExLlama, ExLlamaCache, ExLlamaConfig
from exllama.tokenizer import ExLlamaTokenizer

sys.path.insert(0, str(Path("exllama")))


class ExllamaModel:
    def __init__(self):
        pass

    @classmethod
    def from_pretrained(self, path_to_model):

        path_to_model = Path(path_to_model)
        tokenizer_model_path = path_to_model / "tokenizer.model"
        model_config_path = path_to_model / "config.json"

        # Find the model checkpoint
        model_path = None
        for ext in ['.safetensors', '.pt', '.bin']:
            found = list(path_to_model.glob(f"*{ext}"))
            if len(found) > 0:
                if len(found) > 1:
                    print(
                        f'More than one {ext} model has been found. The last one will be selected. It could be wrong.')

                model_path = found[-1]
                print(model_path)
                break

        config = ExLlamaConfig(str(model_config_path))
        config.model_path = str(model_path)
        config.max_seq_len = 2048
        model = ExLlama(config)
        cache = ExLlamaCache(model)
        tokenizer = ExLlamaTokenizer(str(tokenizer_model_path))

        result = self()
        result.config = config
        result.model = model
        result.cache = cache
        result.tokenizer = tokenizer

        return result, result

    def generate(self, context, params):
        torch.set_grad_enabled(False)
        torch.cuda._lazy_init()

        generator = ExLlamaGenerator(self.model, self.tokenizer, self.cache)
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

        text = generator.generate_simple(
            context, max_new_tokens=params["max_new_tokens"])
        return text

    def generate_with_streaming(self, context, params):

        torch.set_grad_enabled(False)
        torch.cuda._lazy_init()

        generator = ExLlamaGenerator(self.model, self.tokenizer, self.cache)
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

        generator.end_beam_search()
        ids = generator.tokenizer.encode(context)
        generator.gen_begin(ids)
        initial_len = generator.sequence[0].shape[0]
        all_tokens = []
        for i in range(params["max_new_tokens"]):
            token = generator.gen_single_token()
            yield (generator.tokenizer.decode(generator.sequence[0][initial_len:]))
            if token.item() == generator.tokenizer.eos_token_id:
                break

    def encode(self, string, **kwargs):
        return self.tokenizer.encode(string)
