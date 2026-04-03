from fastapi import FastAPI
from pydantic import BaseModel
from src.core.rag_chain import build_rag_chain

app = FastAPI()

qa_chain = build_rag_chain()


class Query(BaseModel):
    question: str


@app.post("/ask")
def ask_question(query: Query):
    result = qa_chain({"question": query.question})
    return {"answer": result["answer"]}
