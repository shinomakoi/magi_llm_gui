from llama_cpp import Llama, LlamaCache


class LlamaCppModel:
    def __init__(self, use_cache, **params):
        # Initialize the model with the given parameters
        self.model: Llama = Llama(**params)
        
        self.max_context = params["n_ctx"]

        if use_cache:
            print('--- LLama.cpp cache:', use_cache)
            cache = LlamaCache()
            self.model.set_cache(cache)

    @classmethod
    def from_pretrained(cls, use_cache, params):
        # Create an instance of the class from a pretrained model
        return cls(use_cache, **params)

    # Check if exceeded context limit and if so prune it from the start
    def check_token_count(self, context, max_tokens):

        encoded_string = context.encode()
        token_count = len(self.model.tokenize(encoded_string))

        if token_count >= (self.max_context / 2):
            print('--- Context size:', token_count)
        if token_count >= self.max_context:
            print('Context limit reached. Trimming')

            amount_to_trim = (token_count - self.max_context) + max_tokens
            trimmed = self.model.tokenize(encoded_string)[amount_to_trim:]
            trimmed_context = self.model.detokenize(trimmed).decode()

            return trimmed_context
        else:
            return context

    # Generate text from a given context and optional keyword arguments
    def generate(self, context, **kwargs):

        # Check token count
        context = self.check_token_count(context, kwargs["max_tokens"])

        response = self.model.create_completion(context, **kwargs)
        reply = response['choices'][0]['text']
        return reply

    # Generate text from a given context and optional keyword arguments
    def generate_with_streaming(self, context, **kwargs):

        # Check token count
        context = self.check_token_count(context, kwargs["max_tokens"])

        # Generate text from a given context and optional keyword arguments in a streaming fashion
        for response in self.model.create_completion(context, stream=True, **kwargs):
            reply = response['choices'][0]['text']
            yield reply
