from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate

from src.core.llm import get_llm
from src.core.retriever import get_retriever
from src.core.prompts import load_prompt


def build_rag_chain():
    llm = get_llm()
    retriever = get_retriever()
    prompt = load_prompt()

    memory = ConversationBufferMemory(
        memory_key="chat_history",
        return_messages=True
    )

    qa_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=retriever,
        memory=memory,
        combine_docs_chain_kwargs={"prompt": prompt}
    )

    return qa_chain
