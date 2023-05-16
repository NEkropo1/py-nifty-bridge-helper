import os


APP_DIR = os.path.dirname(os.path.abspath(__file__))

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
PDF_PATH = os.path.join(APP_DIR, "../helpers/in/NiftyBridge.pdf")
