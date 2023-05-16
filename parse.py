from core.settings import PDF_PATH
from helpers.pdf_parser import convert_pdf_to_text


if __name__ == "__main__":
    convert_pdf_to_text(PDF_PATH)
