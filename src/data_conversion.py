import pandas as pd
from langchain_core.documents import Document
from src.data_ingestion import data_ingest

data=data_ingest()

def dataconverter(data):
    
    product_list = []

    ## Itrate over the rows of the DataFrame

    for index, row in data.iterrows():
        object = {
            "product_name": row["product_title"],
            "review": row["review"]
        }

    ## Append the object to the product list
    product_list.append(object)
    docs = []
    for entry in product_list:
        metadata = {"product_name": entry['product_name']}
        doc = Document(page_content= entry['review'], metadata= metadata)
        docs.append(doc)    
    return docs

