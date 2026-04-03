from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from src.core.embeddings import get_embeddings

loader = PyPDFLoader("data/sample.pdf")
docs = loader.load()

splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = splitter.split_documents(docs)

embeddings = get_embeddings()

vectorstore = FAISS.from_documents(chunks, embeddings)
vectorstore.save_local("artifacts/vectorstore/faiss_index")