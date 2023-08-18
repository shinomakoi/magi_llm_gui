import sys
from pathlib import Path

sys.path.insert(0, str(Path("rwkvcpp/rwkv")))

import rwkv_cpp_model
import rwkv_cpp_shared_library
import sampling
from rwkv_tokenizer import get_tokenizer
from pathlib import Path
import time


def load_model(rwkv_cpp_model_params):
    # Load the shared library and print system info
    library = rwkv_cpp_shared_library.load_rwkv_shared_library()
    print(f"System info: {library.rwkv_get_system_info_string()}")

    # Get the model path from the parameters
    model_path = rwkv_cpp_model_params["model_path"]

    # Load the RWKV model
    model = rwkv_cpp_model.RWKVModel(
        library,
        model_path,
        thread_count=rwkv_cpp_model_params["n_threads"],
        gpu_layers_count=rwkv_cpp_model_params["n_gpu_layers"],
    )
    return model


def generate(prompt, model, rwkv_cpp_params):
    # Set generation parameters
    generation_count = 1
    tokens_per_generation = rwkv_cpp_params["max_tokens"]
    temperature = rwkv_cpp_params["temperature"]
    top_p = rwkv_cpp_params["top_p"]

    # Check that the prompt is not empty
    assert prompt != "", "Prompt must not be empty"
    # Get the tokenizer functions
    tokenizer_decode, tokenizer_encode = get_tokenizer("20B")
    # Encode the prompt into tokens
    prompt_tokens = tokenizer_encode(prompt)
    init_logits, init_state = None, None

    # Get stop tokens from string. Quick hack for RWKV-Instruct
    stop = tokenizer_encode("User:")

    # Evaluate the initial logits and state for each token in the prompt
    for token in prompt_tokens:
        init_logits, init_state = model.eval(token, init_state, init_state, init_logits)

    # Generate text for each generation
    for generation in range(generation_count):
        # print(f'\n--- Generation {generation} ---\n')
        # print(prompt, end='')
        start = time.time()
        logits, state = init_logits.clone(), init_state.clone()

        # Generate tokens and decode them into text
        for i in range(tokens_per_generation):
            token = sampling.sample_logits(logits, temperature, top_p)
            if token == stop[0]:
                print("--- Hit stop token")
                yield ""
                break
            response = tokenizer_decode([token])
            yield response
            logits, state = model.eval(token, state, state, logits)

        delay = time.time() - start
        print(
            "\n\nTook %.3f sec, %d ms per token"
            % (delay, delay / tokens_per_generation * 1000)
        )
