import logging
import os
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
from backend.config import OPENAI_API_KEY

# Ensure logs directory exists and setup logging
os.makedirs("logs", exist_ok=True)
logging.basicConfig(filename="logs/chatbot.log", level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")

class VectorStore:
    def __init__(self):
        """Initialize the vector store with OpenAI embeddings and in-memory Chroma."""
        try:
            self.embeddings = OpenAIEmbeddings(
                openai_api_key=OPENAI_API_KEY,
                model="text-embedding-ada-002"
            )
            self.vector_store = Chroma(
                collection_name="documents",
                embedding_function=self.embeddings
                # Removed persist_directory to use in-memory storage
            )
            logging.info("Initialized in-memory vector store with ChromaDB")
        except Exception as e:
            logging.error(f"Error initializing vector store: {e}")
            raise

    def store_documents(self, chunks):
        """Store document chunks in the vector store."""
        try:
            if chunks:
                self.vector_store.add_documents(chunks)
                logging.info(f"Stored {len(chunks)} document chunks in vector store")
            else:
                logging.warning("No chunks provided to store")
        except Exception as e:
            logging.error(f"Error storing documents: {e}")
            raise

    def query(self, question):
        """Query the vector store for relevant documents."""
        try:
            results = self.vector_store.similarity_search(question, k=3)
            context = [doc.page_content for doc in results]
            logging.info(f"Queried vector store for: {question}")
            return context
        except Exception as e:
            logging.error(f"Error querying vector store: {e}")
            raise
