from elasticsearch import Elasticsearch
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA
from langchain.vectorstores.elasticsearch import ElasticsearchStore

class QAService:
    def __init__(self):
        self.client = Elasticsearch("http://localhost:9200")
        self.embeddings = OpenAIEmbeddings()
        self.vector_store = ElasticsearchStore(
            es_connection=self.client,
            index_name="docs",
            embedding=self.embeddings
        )
        self.llm = OpenAI(temperature=0)
        self.qa_chain = RetrievalQA.from_chain_type(
            llm=self.llm,
            retriever=self.vector_store.as_retriever()
        )

    def answer(self, question):
        return self.qa_chain.run(question)

