import google.generativeai as genai
from google.generativeai.types import StrictContentType
from .base_adapter import LLMChatAdapter
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')  # Get Gemini API key from .env file

class GeminiChatAdapter(LLMChatAdapter):
    def __init__(self, model_name: str = "gemini-pro"):
        super().__init__(model_name)
        genai.configure(api_key=GEMINI_API_KEY)  # Configure the API key for Gemini
        self.model_name = model_name
        self.chat_session = None

    def start_chat(self, history=None):
        """Starts a new chat session with the specified model."""
        model = genai.GenerativeModel(self.model_name)
        self.chat_session = model.start_chat(history=history)

    def _format_history(self, history):
        """Formats the chat history for the Gemini model."""
        if not history:
            return []
        formatted_history = []
        for message in history:
            formatted_message = self._format_message(message)
            formatted_history.append(formatted_message)
        return formatted_history

    def _format_message(self, message):
        """Formats a single message for the Gemini model."""
        role = message.get('role')
        content = message.get('content')
        parts = [{"text": content}]
        if role == 'assistant':
            role = 'model'  # Change 'assistant' to 'model' for Gemini
        return {"role": role, "parts": parts}

    def chat(self, messages: list, stream: bool = False, **kwargs):
        """Sends messages to the Gemini model and returns the response."""
        if self.chat_session is None:
            formatted_messages = self._format_history(history=messages)
            self.start_chat(history=formatted_messages)

        # Send the last message in the chat history
        if stream:
            response = self.chat_session.send_message(messages[-1]['content'], stream=True, **kwargs)
            return response  # Return the stream generator
        else:
            response = self.chat_session.send_message(messages[-1]['content'], **kwargs)
            return response.text  # Return the text response