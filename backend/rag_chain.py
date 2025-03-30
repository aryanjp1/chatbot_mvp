import logging
import os
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from backend.config import OPENAI_API_KEY
from backend.vector_store import VectorStore

# Ensure logs directory exists and setup logging
os.makedirs("logs", exist_ok=True)
logging.basicConfig(filename="logs/chatbot.log", level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")

class RAGChain:
    def __init__(self, vector_store):
        """Initialize the RAG chain with OpenAI LLM and vector store."""
        try:
            self.llm = ChatOpenAI(
                openai_api_key=OPENAI_API_KEY,
                model="gpt-3.5-turbo",
                temperature=0.3,
                max_tokens=150
            )
            self.vector_store = vector_store
            self.prompt_template = PromptTemplate(
                input_variables=["context", "question"],
                template="Context: {context}\nQuestion: {question}\nAnswer:"
            )
            self.qa_chain = RetrievalQA.from_chain_type(
                llm=self.llm,
                chain_type="stuff",
                retriever=self.vector_store.vector_store.as_retriever(search_kwargs={"k": 3}),
                return_source_documents=False,
                chain_type_kwargs={"prompt": self.prompt_template}
            )
            logging.info("Initialized RAG chain")
        except Exception as e:
            logging.error(f"Error initializing RAG chain: {e}")
            raise

    def answer_question(self, question):
        """Generate an answer based on the question and retrieved context."""
        try:
            response = self.qa_chain.invoke({"query": question})
            answer = response["result"]
            logging.info(f"Generated answer for question: {question}")
            return answer
        except Exception as e:
            logging.error(f"Error answering question: {e}")
            raise