from langchain.prompts import PromptTemplate

def load_prompt():
    with open("app/prompts/rag_prompt.txt") as f:
        template = f.read()

    prompt = PromptTemplate(
        template=template,
        input_variables=["context", "question", "chat_history"]
    )
    return prompt