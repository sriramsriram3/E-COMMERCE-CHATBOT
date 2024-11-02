import os
from pathlib import Path

list_of_files=[
    "src/__init__.py",
    "src/helper.py",
    "src/prompt.py",
    "notebook/__init__.py",
    "notebook/test.ipynb",
    "requirements.txt",
    "setup.py",
    ".env",
    "templates/__init__.py",
    "templates/index.py",
    "static/__init__.py",
    "static/style.css",
    ".github/workflows",
    "data/__init__.py",
    "app.py"

]


for path in list_of_files:
    file_path=Path(path)
    folder,file=os.path.split(path)
    if folder != "":
        os.makedirs(folder,exist_ok=True)

    if not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
        with open(path,"w") as f:
            pass