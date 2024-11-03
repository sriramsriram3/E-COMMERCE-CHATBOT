from langchain_huggingface import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os
load_dotenv()
GROQ_API_KEY=os.getenv('GROQ_API_KEY')

def embedding_model():
    model_name="sentence-transformers/all-mpnet-base-v2"
    embeddings=HuggingFaceEmbeddings(model_name=model_name)
    return embeddings

def llm_model():
    model = ChatGroq(groq_api_key = GROQ_API_KEY, model="mixtral-8x7b-32768", temperature=0.5)
    return model
