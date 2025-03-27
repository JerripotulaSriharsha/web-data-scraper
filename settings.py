import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Model settings
GPT_MODEL = "gpt-4"
MAX_TOKENS = 100000

# API Keys
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
LLAMA_API_KEY = os.getenv("LLAMA_API_KEY")