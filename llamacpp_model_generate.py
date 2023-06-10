from llama_cpp import Llama


class LlamaCppModel:
    def __init__(self, **params):
        # Initialize the model with the given parameters
        self.model = Llama(**params)

    @classmethod
    def from_pretrained(cls, params):
        # Create an instance of the class from a pretrained model
        return cls(**params)

    def generate(self, context, **kwargs):
        # Generate text from a given context and optional keyword arguments
        response = self.model.create_completion(context, **kwargs)
        reply = response['choices'][0]['text']
        return reply

    def generate_with_streaming(self, context, **kwargs):
        print(context)
        # Generate text from a given context and optional keyword arguments in a streaming fashion
        for response in self.model.create_completion(context, stream=True, **kwargs):
            reply = response['choices'][0]['text']
            yield reply
