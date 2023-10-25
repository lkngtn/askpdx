import pickle
import tiktoken
from tqdm import tqdm 

def num_tokens_from_string(string: str, encoding_name: str) -> int:
    """Returns the number of tokens in a text string."""
    encoding = tiktoken.get_encoding(encoding_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens

num_tokens_from_string("tiktoken is great!", "cl100k_base")

if __name__ == '__main__':
# Load docs, metadata 
    with open("docs.pkl", "rb") as f:
        docs = pickle.load(f)
    with open("metadatas.pkl", "rb") as f:
        metadatas = pickle.load(f)    

num_tokens = 0
for doc in tqdm(docs):
    tokens = num_tokens_from_string(doc, "cl100k_base")
    num_tokens += tokens

print("Total tokens in docs: ", num_tokens)
print("Estimated total cost = ", (num_tokens/1000)*0.0001)