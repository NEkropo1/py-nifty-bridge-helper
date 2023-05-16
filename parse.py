import os

from core.settings import PDF_PATH
from helpers.pdf_parser import convert_pdf_to_text
from helpers.text_chunker import chunk_text_file


output_file_location = os.path.join(os.path.dirname(os.path.abspath(__file__)), "helpers", "out", )
text_filename = os.path.join(output_file_location, "NiftyBridge.txt")

if __name__ == "__main__":
    convert_pdf_to_text(PDF_PATH)
    text_chunks = chunk_text_file(text_filename)
