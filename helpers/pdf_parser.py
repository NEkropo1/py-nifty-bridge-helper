import os

import PyPDF2


def convert_pdf_to_text(pdf: str) -> None:
    output_dir = os.path.join(os.path.dirname(pdf), "..", "out")
    os.makedirs(output_dir, exist_ok=True)

    with open(pdf, "rb") as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)
        num_pages = len(reader.pages)

        text_filename = os.path.join(output_dir, os.path.basename(pdf)[:-4] + ".txt")
        with open(text_filename, "w", encoding="utf-8") as text_file:
            for page_num in range(num_pages):
                page = reader.pages[page_num]
                text = page.extract_text()

                text_file.write(text)
