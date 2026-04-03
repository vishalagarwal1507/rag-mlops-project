from langchain_huggingface.embeddings import HuggingFaceEmbeddings
import yaml

def load_config():
    with open("src/config/config.yaml") as f:
        return yaml.safe_load(f)

def get_embeddings():
    config = load_config()
    return HuggingFaceEmbeddings(
        model_name=config["embedding"]["model_name"]
    )

