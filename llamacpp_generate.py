from llama_cpp import Llama, LlamaCache


class LlamaCppModel:
    def __init__(self, use_cache, **params):
        # Initialize the model with the given parameters
        self.model: Llama = Llama(**params)
        if use_cache:
            print('--- LLama.cpp cache:', use_cache)
            cache = LlamaCache()
            self.model.set_cache(cache)

    @classmethod
    def from_pretrained(cls, use_cache, params):
        # Create an instance of the class from a pretrained model
        return cls(use_cache, **params)

    def generate(self, context, **kwargs):
        # Generate text from a given context and optional keyword arguments
        response = self.model.create_completion(context, **kwargs)
        reply = response['choices'][0]['text']
        return reply

    def generate_with_streaming(self, context, **kwargs):
        # Generate text from a given context and optional keyword arguments in a streaming fashion
        for response in self.model.create_completion(context, stream=True, **kwargs):
            reply = response['choices'][0]['text']
            yield reply
