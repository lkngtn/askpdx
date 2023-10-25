# AskPDX 

## Description

Ask PDX is an implementation of [retrieval-augmented generation (RAG)](https://python.langchain.com/docs/use_cases/question_answering/) applied to Portland Oregon's Charter, City Code, and Policy documents. 

## Usage

### Scrape PDX Charter, City Code, and Policy Documents

To scrape the documents, run the following command:

```bash 
python scrape_documents.py --sitemap 'pdx_charter_code_policies_urls.xml'
```

This will create a `docs.pkl` and `metadatas.pkl` in the current directory which we will be used to create embeddings in the next step. 

### Create embeddings 

We are using Open AI to create embeddings for the documents. Before we do we must first export our OpenAI API key as an environment variable. 

```bash 
export OPENAI_API_KEY=<your key here>
```

Then we can run the following command to create embeddings for the documents:

```bash
python create_embeddings.py 
```

This will create a `faiss_store.pkl` in the current directory which is used for retrieval when we ask questions. 

### Ask Questions

To ask questions, run the following command:

```bash
python ask_question.py "Who becomes mayor if the mayor dies in office?"
```