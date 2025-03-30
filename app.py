import streamlit as st
import logging
import os
from backend.document_loader import load_and_split_files
from backend.vector_store import VectorStore
from backend.rag_chain import RAGChain
from backend.config import DATA_DIR

# Ensure logs directory exists and setup logging
os.makedirs("logs", exist_ok=True)
logging.basicConfig(filename="logs/chatbot.log", level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")

# Initialize components and load documents at startup
@st.cache_resource
def initialize_chatbot():
    try:
        vector_store = VectorStore()
        chunks = load_and_split_files()
        vector_store.store_documents(chunks)
        rag_chain = RAGChain(vector_store)
        return rag_chain
    except Exception as e:
        logging.error(f"Initialization error: {e}")
        raise

# Set up the Streamlit page
st.title("Chatbot MVP")
st.write(f"A conversational AI based on documents in the `{DATA_DIR}/` folder.")

# Initialize chat history in session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Load the chatbot
try:
    rag_chain = initialize_chatbot()
except Exception as e:
    st.error(f"Failed to initialize chatbot: {e}")
    st.stop()

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Ask a question..."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate and display bot response
    try:
        answer = rag_chain.answer_question(prompt)
        st.session_state.messages.append({"role": "assistant", "content": answer})
        with st.chat_message("assistant"):
            st.markdown(answer)
    except Exception as e:
        error_msg = f"Error answering question: {e}"
        st.session_state.messages.append({"role": "assistant", "content": error_msg})
        with st.chat_message("assistant"):
            st.markdown(error_msg)
        logging.error(f"Question answering error: {e}")

# Add a clear chat button
if st.button("Clear Chat"):
    st.session_state.messages = []
    st.rerun()  # Rerun to refresh the UI

# Optional: Add some basic styling via CSS
st.markdown("""
    <style>
    .user-message {
        background-color: #DCF8C6;
        padding: 10px;
        border-radius: 5px;
        margin: 5px 0;
    }
    .assistant-message {
        background-color: #ECECEC;
        padding: 10px;
        border-radius: 5px;
        margin: 5px 0;
    }
    </style>
""", unsafe_allow_html=True)