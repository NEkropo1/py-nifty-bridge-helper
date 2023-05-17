import os

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, Header
from langchain.vectorstores import Redis

from core.settings import PDF_PATH
from helpers.pdf_parser import convert_pdf_to_text
from helpers.text_chunker import chunk_text_file
from helpers.embeddings_generator import generate_embeddings_from_chunks, generate_response
from schemas import MessageRequest, MessageResponse

output_file_location = os.path.join(os.path.dirname(os.path.abspath(__file__)), "helpers", "out", )
text_filename = os.path.join(output_file_location, "NiftyBridge.txt")
load_dotenv()


app = FastAPI()


def get_rds() -> Redis:
    return rds[0]


@app.on_event("startup")
def startup_event():
    if not os.path.exists(text_filename):
        convert_pdf_to_text(PDF_PATH)
    global text_chunks, rds
    text_chunks = chunk_text_file(text_filename)
    rds = generate_embeddings_from_chunks(text_chunks)


@app.post("/api/send")
def send_message(request: MessageRequest = None, x_api_key_token: str = Header(default=None)):
    if x_api_key_token != os.getenv("X_API_KEY_TOKEN"):
        raise HTTPException(status_code=401, detail="Invalid API key")

    response = generate_response(request.message, rds[0])

    return MessageResponse(response=response)
