import os

from dotenv import load_dotenv

from core.settings import PDF_PATH
from helpers.pdf_parser import convert_pdf_to_text
from helpers.text_chunker import chunk_text_file
from helpers.embeddings_generator import generate_embeddings_from_chunks, generate_response

output_file_location = os.path.join(os.path.dirname(os.path.abspath(__file__)), "helpers", "out", )
text_filename = os.path.join(output_file_location, "NiftyBridge.txt")
load_dotenv()


if __name__ == "__main__":
    if not os.path.exists(text_filename):
        convert_pdf_to_text(PDF_PATH)

    text_chunks = chunk_text_file(text_filename)
    rds = generate_embeddings_from_chunks(text_chunks)

    check_query = "shitty useless message"

    response = generate_response(check_query, rds[0])
    print(response)
