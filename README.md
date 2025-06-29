# 📄 Document Q&A with LangChain + Elasticsearch

Ask questions grounded on your indexed documents.

## Endpoints
- `POST /ingest` — splits docs.txt, embeds & stores in Elasticsearch.
- `POST /ask` with `{ "question": "Where is the Eiffel Tower?" }`
- `GET /health`

## Setup
- Start Elasticsearch (on localhost:9200)
- Then run:
```bash
pip install -r requirements.txt
export OPENAI_API_KEY=your_key_here
uvicorn app.main:app --reload

