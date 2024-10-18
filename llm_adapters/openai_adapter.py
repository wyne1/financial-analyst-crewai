import os
from langchain_openai import ChatOpenAI

class OpenAIAdapter:
    def __init__(self, model_name='gpt-4o'):
        self.model = ChatOpenAI(model=model_name, temperature=0.7)

    def generate_response(self, prompt):
        return self.model(prompt)