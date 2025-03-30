import logging
import os
from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from backend.config import CHUNK_SIZE, CHUNK_OVERLAP, DATA_DIR

# Ensure logs directory exists and setup logging
os.makedirs("logs", exist_ok=True)
logging.basicConfig(filename="logs/chatbot.log", level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")

def load_and_split_files():
    """
    Load all PDF/TXT files from the data/ folder and split them into chunks.
    Returns:
        list: List of document chunks.
    """
    try:
        if not os.path.exists(DATA_DIR):
            os.makedirs(DATA_DIR)
            logging.warning(f"Created empty {DATA_DIR} folder")
            return []

        chunks = []
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=CHUNK_SIZE,
            chunk_overlap=CHUNK_OVERLAP
        )

        for filename in os.listdir(DATA_DIR):
            file_path = os.path.join(DATA_DIR, filename)
            if filename.endswith(".pdf"):
                loader = PyPDFLoader(file_path)
                logging.info(f"Loaded PDF file: {file_path}")
            elif filename.endswith(".txt"):
                loader = TextLoader(file_path)
                logging.info(f"Loaded text file: {file_path}")
            else:
                logging.warning(f"Skipping unsupported file: {file_path}")
                continue

            documents = loader.load()
            file_chunks = text_splitter.split_documents(documents)
            chunks.extend(file_chunks)
            logging.info(f"Split {file_path} into {len(file_chunks)} chunks")

        if not chunks:
            logging.warning(f"No valid files found in {DATA_DIR}")
        else:
            logging.info(f"Total chunks loaded: {len(chunks)}")
        return chunks

    except Exception as e:
        logging.error(f"Error loading/splitting files: {e}")
        raise