from fastapi import FastAPI
from pydantic import BaseModel
from .qa import QAService
from .ingest import Ingestor

app = FastAPI()
qa_service = QAService()

@app.post("/ask")
def ask(query: dict):
    question = query.get("question")
    answer = qa_service.answer(question)
    return {"question": question, "answer": answer}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/ingest")
def ingest():
    ingestor = Ingestor()
    ingestor.index_docs()
    return {"status": "documents indexed"}

