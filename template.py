import os
from pathlib import Path

list_of_files=[
    "src/__init__.py",
    "src/data_ingestion.py",
    "src/data_conversion.py",
    "src/retrieval_generation.py",
    "notebook/test.ipynb",
    "requirements.txt",
    "setup.py",
    ".env",
    "templates/index.py",
    "static/style.css",
    ".github/workflows",
    "app.py",
    "vector_store/__init__.py",
    "vector_store/astradb.py"

]


for path in list_of_files:
    file_path=Path(path)
    folder,file=os.path.split(path)
    if folder != "":
        os.makedirs(folder,exist_ok=True)

    if not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
        with open(path,"w") as f:
            pass