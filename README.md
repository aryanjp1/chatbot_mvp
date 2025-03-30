# Chatbot MVP

A conversational AI chatbot built to answer questions based on pre-loaded PDF or text documents. This Minimum Viable Product (MVP) was developed within a 24-hour timeframe as an assignment, showcasing a production-ready application with a ChatGPT-like interface. It leverages Retrieval-Augmented Generation (RAG) to provide context-aware responses from documents stored in a `data/` folder.

## Live Demo
- **URL**: [https://chatbotmvp-ucmsosyju7jimzbiuyqugi.streamlit.app/](https://chatbotmvp-ucmsosyju7jimzbiuyqugi.streamlit.app/)
- Test it by asking questions like "What's in the PDF?" or "Summarize the document" based on the sample PDF included.

## Features
- **Conversational UI**: ChatGPT-like interface with chat history and a clear chat option.
- **Document-Based Q&A**: Answers questions using content from PDF/TXT files in the `data/` folder.
- **Error Handling**: Robust logging and user-friendly error messages.
- **Modular Design**: Backend logic separated for maintainability.
- **Deployment**: Hosted on Streamlit Community Cloud with secrets management.

## Project Structure

```
chatbot-mvp/
├── app.py               # Streamlit frontend with conversational UI
├── backend/
│   ├── __init__.py      # Makes backend a package
│   ├── config.py        # Configuration (API keys, settings)
│   ├── document_loader.py # Loads and splits documents from data/
│   ├── vector_store.py   # FAISS-based vector storage
│   └── rag_chain.py      # RAG pipeline with OpenAI LLM
├── data/
│   └── L-G-0003513485-0006753845.pdf  # Sample PDF for testing
├── logs/                # Log files (created at runtime, ignored by Git)
├── requirements.txt     # Dependencies
├── .gitignore           # Ignores unnecessary files
├── .env                 # Local environment variables (not tracked)
└── README.md            # Project documentation
```

## Tech Stack
- **Frontend**: 
  - **Streamlit (1.32.0)**: Provides a simple, interactive web interface with chat functionality.
- **Backend**: 
  - **Python (3.10)**: Core programming language.
  - **LangChain (0.1.13)**: Framework for RAG and document processing.
  - **LangChain-OpenAI (0.1.1)**: Integrates OpenAI embeddings and LLM.
  - **LangChain-Community (0.0.29)**: Document loaders (PyPDF, Text).
  - **FAISS (1.8.0)**: Lightweight, in-memory vector store for similarity search.
  - **Python-dotenv (1.0.1)**: Manages environment variables securely.
- **APIs**: 
  - **OpenAI API**: Powers embeddings (`text-embedding-ada-002`) and LLM (`gpt-3.5-turbo`).
- **Deployment**: 
  - **Streamlit Community Cloud**: Hosts the app with GitHub integration.
  - **GitHub**: Version control and code hosting.

## Why It's Production-Ready
- **Modularity**: Code is split into frontend (`app.py`) and backend modules (`backend/`), making it easy to maintain and extend.
- **Error Handling**: Comprehensive try-except blocks with user-facing error messages and detailed logging (`logs/chatbot.log`).
- **Secrets Management**: OpenAI API key is stored securely in Streamlit Cloud's secrets (TOML format) and locally in `.env` (ignored by Git).
- **Scalable Design**: Uses FAISS for in-memory vector storage, avoiding persistent storage issues on cloud platforms.
- **Conversational UI**: Chat history persists in session state, with a clear option, enhancing user experience.
- **Dependency Management**: All dependencies are pinned in `requirements.txt` for consistent deployment.
- **Deployment**: Successfully hosted on Streamlit Cloud, accessible via a public URL, with automated dependency installation.

## Setup (Local)
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/aryanjp1/chatbot_mvp.git
   cd chatbot_mvp
   ```

2. **Create a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Add OpenAI API Key**:
   - Create a `.env` file in the root directory:
     ```
     OPENAI_API_KEY=your-api-key-here
     ```
   - Replace `your-api-key-here` with your OpenAI API key.

5. **Add Documents**:
   - Place PDF or TXT files in the `data/` folder (e.g., the included L-G-0003513485-0006753845.pdf).

6. **Run the App**:
   ```bash
   streamlit run app.py
   ```
   - Open http://localhost:8501 in your browser.

## Deployment (Streamlit Cloud)
- **GitHub Repository**: Code is hosted at https://github.com/aryanjp1/chatbot_mvp.

- **Streamlit Cloud Setup**:
  - Connected to aryanjp1/chatbot_mvp, branch main, entry point app.py.
  - Secrets added in TOML format:
    ```toml
    OPENAI_API_KEY = " "
    ```
  - Live Link: https://chatbotmvp-ucmsosyju7jimzbiuyqugi.streamlit.app/

## Usage
1. Open the live link or run locally.
2. Type a question in the chat input (e.g., "What's the main topic of the PDF?").
3. View responses and chat history; use the "Clear Chat" button to reset.

## Development Notes
- **Timeframe**: Built in ~24 hours as an assignment.
- **Challenges**: Overcame sqlite3 compatibility issues on Streamlit Cloud by switching from ChromaDB to FAISS.
- **Future Improvements**: Add persistent storage, support for more file types, and enhanced UI styling.

## License
This project is for educational purposes and does not include a formal license.

Developed by aryanjp1 with assistance from Grok (xAI).
