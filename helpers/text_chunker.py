import nltk


def chunk_text_file(text_filename: str) -> list[str]:
    with open(text_filename) as f:
        state_of_the_union = f.read()

    tokenizer = nltk.tokenize.punkt.PunktSentenceTokenizer()
    text_chunks = tokenizer.tokenize(state_of_the_union)
    return text_chunks
