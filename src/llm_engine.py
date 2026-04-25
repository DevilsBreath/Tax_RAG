from llama_cpp import Llama
from src import config

class LLMEngine:
    def __init__(self):
        print(f"Loading LLM from {config.LLM_MODEL_DIR}...")
        self.model = Llama(
            model_path=str(config.LLM_MODEL_DIR),
            n_ctx=4096,
            n_gpu_layers=-1,   # offload all layers to RTX 4050
            verbose=False
        )


    def generate(self, messages: list, max_tokens: int = 160, temperature: float = 0.0):
        output = self.model.create_chat_completion(
            messages=messages,
            max_tokens=max_tokens,
            temperature=temperature
        )
        return output["choices"][0]["message"]["content"].strip()

# pip uninstall llama-cpp-python -y
# CMAKE_ARGS="-DGGML_CUDA=on" pip install llama-cpp-python --force-reinstall --no-cache-dir
# pip install llama-cpp-python --extra-index-url https://abetlen.github.io/llama-cpp-python/whl/cu121
