from dotenv import load_dotenv
from langchain.llms import OpenAI


load_dotenv()
open_ai_3_5_turbo_llm = OpenAI(model_name="gpt-3.5-turbo", n=2, best_of=2)

