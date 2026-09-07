import os
from langchain_chroma import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document

CHROMA_DIR = "vector_db"
COLLECTION_NAME = "meeting_transcript"
EMBEDDING_MODEL = "all-MiniLm-L6-v2"

def get_embeddings():
    return HuggingFaceEmbeddings(
        model = EMBEDDING_MODEL,
        mode_kwargs = {"device": 'cpu'}
    )
    
def build_vector_store(transcript:str)-> Chroma:
    print("Building vector store")
    splitter = RecursiveCharacterTextSplitter(
        chunks_size = 500,
        chunk_overlap = 50
    )
    chunks = splitter.split_text(transcript)
    
    docs = [
        Document(page_content= chunk, metadata = {"chunk_index": i})
        for i,chunk in enumerate(chunks)
    ]
    
    embeddings = get_embeddings()
    vector_db = Chroma.from_documents(
        documents= docs,
        embedding= embeddings,
        collection_name= COLLECTION_NAME,
        persist_directory= CHROMA_DIR
    )
    return vector_db

# load vector store fun

def load_vector_store()-> Chroma:
    embeddings = get_embeddings()
    vectore_store = Chroma(
        collection_name= COLLECTION_NAME,
        persist_directory= CHROMA_DIR,
        embedding_function= embeddings
    )
    return vectore_store

# retrieve the loaded vector

def get_retriever(vector_store: Chroma, k: int = 4):
    return vector_store.as_retriever(
        search_type = 'similarity',
        search_kwargs = {'k':k}
    )
    

