# Парсер данных
import os
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from qdrant_client import QdrantClient

class KnowledgeBase:
    def __init__(self):
        self.client = QdrantClient("localhost", port=6333)
        self.embedder = OpenAIEmbeddings()
        self.collection = "norilsk_knowledge"
    
    def load_pdfs(self, folder="data/pdfs/"):
        docs = []
        for file in os.listdir(folder):
            if file.endswith('.pdf'):
                loader = PyPDFLoader(f"{folder}/{file}")
                docs.extend(loader.load())
        return docs
    
    def index_documents(self, docs):
        splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
        chunks = splitter.split_documents(docs)
        texts = [chunk.page_content for chunk in chunks]
        # Здесь будет загрузка в Qdrant
        return texts
    
    def search(self, query, limit=5):
        # Здесь будет поиск
        return f"Результаты поиска по запросу: {query}"
