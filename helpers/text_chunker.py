import os

from langchain.text_splitter import CharacterTextSplitter


output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "out",)
text_filename = os.path.join(output_dir, "NiftyBridge.txt")
with open(text_filename) as f:
    state_of_the_union = f.read()

text_splitter = CharacterTextSplitter.from_tiktoken_encoder(chunk_size=100, chunk_overlap=0)
texts = text_splitter.split_text(state_of_the_union)

print(texts[0])
