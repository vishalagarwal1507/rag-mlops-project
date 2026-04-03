from langchain_community.vectorstores import FAISS
from src.core.embeddings import get_embeddings
import yaml

def load_config():
    with open("src/config/config.yaml") as f:
        return yaml.safe_load(f)

def get_retriever():
    config = load_config()

    embeddings = get_embeddings()

    vectorstore = FAISS.load_local(
        config["paths"]["vectorstore"],
        embeddings,
        allow_dangerous_deserialization=True
    )

    retriever = vectorstore.as_retriever(
        search_kwargs={"k": config["retriever"]["top_k"]}
    )

    return retriever
