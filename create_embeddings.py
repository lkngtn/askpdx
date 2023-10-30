import pickle
#import pinecone
#from langchain.vectorstores import Pinecone
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings

if __name__ == '__main__':

# Load docs, metadata 
    with open("docs.pkl", "rb") as f:
        docs = pickle.load(f)
    with open("metadatas.pkl", "rb") as f:
        metadatas = pickle.load(f)    

    embeddings = OpenAIEmbeddings(chunk_size=250, max_retries=10) # try smaller chunk size and more retries to avoid rate limit
    store = FAISS.from_texts(docs, embeddings, metadatas=metadatas)

    with open("faiss_store.pkl", "wb") as f:
        pickle.dump(store, f)

# Pinecone

## TODO: Use streamlit env to get API key and ENV
# find API key in console at app.pinecone.io
#PINECONE_API_KEY = input("Pinecone API Key: ")
# find ENV (cloud region) next to API key in console
#PINECONE_ENV = input("Pinecone environment: ")

#index_name= "askpdx-charter-code-policy"
# pinecone.init(
#     api_key=PINECONE_API_KEY,
#     environment=PINECONE_ENV, 
# )

# embeddings = OpenAIEmbeddings(chunk_size=250, max_retries=10)

# if index_name not in pinecone.list_indexes():
#     # we create a new index
#     pinecone.create_index(
#         name=index_name,
#         metric='cosine',
#         dimension=1536  # 1536 dim of text-embedding-ada-002
#     )

# docsearch = Pinecone.from_texts(texts=docs, embedding=embeddings, index_name=index_name, metadatas=metadatas)
