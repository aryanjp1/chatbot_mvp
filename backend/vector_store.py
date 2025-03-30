import logging
import os
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from backend.config import OPENAI_API_KEY

# Ensure logs directory exists and setup logging
os.makedirs("logs", exist_ok=True)
logging.basicConfig(filename="logs/chatbot.log", level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")

class VectorStore:
    def __init__(self):
        """Initialize the vector store with OpenAI embeddings and FAISS."""
        try:
            self.embeddings = OpenAIEmbeddings(
                openai_api_key=OPENAI_API_KEY,
                model="text-embedding-ada-002"
            )
            # FAISS will be initialized when documents are added
            self.vector_store = None
            logging.info("Initialized vector store with FAISS")
        except Exception as e:
            logging.error(f"Error initializing vector store: {e}")
            raise

    def store_documents(self, chunks):
        """Store document chunks in the vector store."""
        try:
            if chunks:
                self.vector_store = FAISS.from_documents(chunks, self.embeddings)
                logging.info(f"Stored {len(chunks)} document chunks in FAISS vector store")
            else:
                logging.warning("No chunks provided to store")
        except Exception as e:
            logging.error(f"Error storing documents: {e}")
            raise

    def query(self, question):
        """Query the vector store for relevant documents."""
        try:
            if self.vector_store is None:
                logging.warning("Vector store is empty; no documents to query")
                return ["No documents available."]
            results = self.vector_store.similarity_search(question, k=3)
            context = [doc.page_content for doc in results]
            logging.info(f"Queried vector store for: {question}")
            return context
        except Exception as e:
            logging.error(f"Error querying vector store: {e}")
            raise
