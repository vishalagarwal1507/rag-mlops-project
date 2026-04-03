from transformers import pipeline
from langchain_huggingface.llms import HuggingFacePipeline
import yaml

def load_config():
    with open("src/config/config.yaml") as f:
        return yaml.safe_load(f)

def get_llm():
    config = load_config()

    pipe = pipeline(
        "text2text-generation",
        model=config["llm"]["model_name"],
        max_new_tokens=config["llm"]["max_tokens"]
    )

    return HuggingFacePipeline(pipeline=pipe)
