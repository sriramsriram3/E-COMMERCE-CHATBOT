from flask import Flask, render_template, request
from src.data_ingestion import data_ingest
from src.data_conversion import dataconverter
from src.model import llm_model
from src.retrieval_generation import rag_pipeline
from vector_store.astradb import connect_vectorstore


data=data_ingest()
docs=dataconverter(data)
vector_store=connect_vectorstore()
model=llm_model()
chain=rag_pipeline()

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")



@app.route("/get", methods = ["POST", "GET"])
def chat():
   
   if request.method == "POST":
      msg = request.form["msg"]
      input = msg

      result = chain.invoke(
         {"input": input},
    config={
        "configurable": {"session_id": "dhruv"}
    },
)["answer"]

      return str(result)

if __name__ == '__main__':
    
    app.run(host="0.0.0.0", port=5000, debug= True)