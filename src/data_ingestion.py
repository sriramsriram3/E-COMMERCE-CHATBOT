import pandas as pd
def data_ingest():
    path='C:/GENAI/FLIPKART-RECOMENDATION/data/flipkart_reviews_dataset.csv'
    data=pd.read_csv(path)
    Data = data[["product_title", "review"]]
    return Data