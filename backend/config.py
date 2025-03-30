import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY not found in .env file!")

# LangChain-specific settings
CHUNK_SIZE = 500
CHUNK_OVERLAP = 50
DATA_DIR = "data"  # Directory for pre-uploaded files