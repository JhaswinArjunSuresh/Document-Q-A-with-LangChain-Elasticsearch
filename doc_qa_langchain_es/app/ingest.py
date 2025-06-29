from elasticsearch import Elasticsearch
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter

class Ingestor:
    def __init__(self):
        self.client = Elasticsearch("http://localhost:9200")
        self.embeddings = OpenAIEmbeddings()
        self.splitter = RecursiveCharacterTextSplitter(chunk_size=200, chunk_overlap=20)

    def index_docs(self):
        with open("data/docs.txt", "r") as f:
            text = f.read()
        
        chunks = self.splitter.split_text(text)
        for i, chunk in enumerate(chunks):
            vector = self.embeddings.embed_query(chunk)
            doc = {
                "content": chunk,
                "vector": vector
            }
            self.client.index(index="docs", id=f"doc_{i}", body=doc)

