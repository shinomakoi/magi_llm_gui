
# Adapted from Oobabooga's WebUI repo

from llama_cpp import Llama, LlamaCache


class LlamaCppModel:
    def __init__(self):
        self.initialized = False

    @classmethod
    def from_pretrained(self, params):
        result = self()

        self.model = Llama(**params)
        # self.model.set_cache(LlamaCache)

        # This is ugly, but the model and the tokenizer are the same object in this library.
        return result, result

    def encode(self, string):
        if type(string) is str:
            string = string.encode()
        return self.model.tokenize(string)

    def generate(self, context, token_count, temperature, top_p, top_k, repetition_penalty, mirostat_mode, callback=None):
        if type(context) is str:
            context = context.encode()
        tokens = self.model.tokenize(context)

        output = b""
        count = 0
        for token in self.model.generate(tokens, top_p=top_p, top_k=top_k, temp=temperature, repeat_penalty=repetition_penalty, mirostat_mode=mirostat_mode):
            text = self.model.detokenize([token])
            yield text.decode()
            # print(text.decode())
            output += text
            if callback:
                callback(text.decode())

            count += 1
            if count >= token_count or (token == self.model.token_eos()):
                break
