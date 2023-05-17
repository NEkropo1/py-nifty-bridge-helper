import os
import sys


APP_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(APP_DIR)

# OPENAI DEPENDENCIES
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_MAX_TOKENS = 4096

# PDF PATH
PDF_PATH = os.path.join(APP_DIR, "helpers/in/NiftyBridge.pdf")

# REDIS DEPENDENCIES
REDIS_VECTOR_HOST = os.getenv("REDIS_VECTOR_HOST")
REDIS_VECTOR_PORT = os.getenv("REDIS_VECTOR_PORT")
REDIS_VECTOR_DB = os.getenv("REDIS_VECTOR_DB")

# X-API-KEY-Token
X_API_KEY_TOKEN = os.getenv("X_API_KEY_TOKEN")
