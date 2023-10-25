import pickle
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings

if __name__ == '__main__':

# Load docs, metadata 
    with open("docs.pkl", "rb") as f:
        docs = pickle.load(f)
    with open("metadatas.pkl", "rb") as f:
        metadatas = pickle.load(f)    

# FAISS
    embeddings = OpenAIEmbeddings(chunk_size=250, max_retries=10) # try smaller chunk size and more retries to avoid rate limit
    store = FAISS.from_texts(docs, embeddings, metadatas=metadatas)

    with open("faiss_store.pkl", "wb") as f:
        pickle.dump(store, f)




