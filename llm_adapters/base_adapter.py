class LLMChatAdapter:
    def __init__(self, model_name: str):
        self.model_name = model_name

    def set_model_name(self, model_name: str):
        self.model_name = model_name

    def chat(self, messages: list, stream: bool = False, **kwargs):
        raise NotImplementedError("Subclasses should implement this!")