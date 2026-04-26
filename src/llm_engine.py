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

    @staticmethod
    def _messages_to_prompt(messages: list) -> str:
        """Fallback prompt formatter for models without chat-template support."""
        lines = []
        for message in messages:
            role = str(message.get("role", "user")).strip().lower()
            content = str(message.get("content", "")).strip()
            if not content:
                continue

            if role == "system":
                lines.append(f"System:\n{content}")
            elif role == "assistant":
                lines.append(f"Assistant:\n{content}")
            else:
                lines.append(f"User:\n{content}")

        lines.append("Assistant:")
        return "\n\n".join(lines)


    def generate(self, messages: list, max_tokens: int = 160, temperature: float = 0.0):
        try:
            output = self.model.create_chat_completion(
                messages=messages,
                max_tokens=max_tokens,
                temperature=temperature
            )
            return output["choices"][0]["message"]["content"].strip()
        except Exception:
            prompt = self._messages_to_prompt(messages)
            output = self.model.create_completion(
                prompt=prompt,
                max_tokens=max_tokens,
                temperature=temperature
            )
            return output["choices"][0]["text"].strip()