from langchain.text_splitter import TokenTextSplitter


def chunk_text_file(text_filename: str) -> list[str]:
    with open(text_filename) as f:
        state_of_the_union = f.read()

    text_splitter = TokenTextSplitter.from_tiktoken_encoder(chunk_size=128, chunk_overlap=0)
    text_chunks = text_splitter.split_text(state_of_the_union)
    return text_chunks
