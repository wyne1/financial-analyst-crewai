from dotenv import load_dotenv
import os

def set_environment_variables():
    # Load environment variables from .env file
    load_dotenv()
    
    # Set environment variables for the application
    os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
    os.environ["OPENAI_MODEL_NAME"] = 'gpt-3.5-turbo'
    os.environ["SERPER_API_KEY"] = os.getenv("SERPER_API_KEY")