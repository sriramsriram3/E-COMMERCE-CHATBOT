from langchain_astradb import AstraDBVectorStore
from uuid import uuid4
from src.model import embedding_model
from src.data_ingestion import data_ingest
from src.data_conversion import dataconverter
from dotenv import load_dotenv
load_dotenv()
import os

ASTRA_DB_APPLICATION_TOKEN=os.getenv('ASTRA_DB_APPLICATION_TOKEN')
ASTRA_DB_API_ENDPOINT=os.getenv('ASTRA_DB_API_ENDPOINT')
data=data_ingest()
docs=dataconverter()
embeddings=embedding_model()
def connect_vectorstore():
    vector_store = AstraDBVectorStore(
    collection_name="FLIPKART_RECOMMENDATION",
    embedding=embeddings,
    api_endpoint=ASTRA_DB_API_ENDPOINT,
    token=ASTRA_DB_APPLICATION_TOKEN)

    return vector_store

vector_store=connect_vectorstore()

uuids = [str(uuid4()) for _ in range(len(docs))]
vector_store.add_documents(documents=docs, ids=uuids)