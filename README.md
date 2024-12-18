 # Flipkart Chat Bot 

### This project implements a Flipkart chatbot with the capability to handle complex product-related queries and store chat history and memory for more personalized responses. The chatbot uses a Retrieval-Augmented Generation (RAG) pipeline with the Mistral model running on GROQ for fast inference, AstraDB for vector storage, and Flask as the backend framework.

## Features

###### RAG Pipeline: 
Utilizes the Retrieval-Augmented Generation approach for handling large, contextually rich data.

###### Chat History and Memory: 
Allows the bot to store past interactions for enhanced personalized responses.

###### LLM Model: 
Mistral model on GROQ for optimized and cost-effective language model inference.

###### Vector Storage: 
AstraDB provides efficient and scalable vector storage.

###### Web API: 
Exposes an API built with Flask for easy integration with front-end applications.

## Requirements

Python 3.8+
Flask
GROQ SDK
AstraDB (for Vector Storage)
Mistral Model (LLM)
Dependencies: Listed in requirements.txt


##Installation

### If you don't have anaconda download from here
```bash 
https://www.anaconda.com/download/success 
```
### Create a Conda environment:

```bash
conda create -p <env_name> python=3.10 -y
```
### Activate your conda environment

```bash
conda activate <env_path>
```
- If activating on bash terminal use this command:

```bash
source activate ./<env_name> 
```
ELSE
```bash
conda activate <env_path>
```

### Create a requirement.txt file and install it

```bash
pip install -r requirements.txt
```
### Create a .env file for keeping your environment variable.
- GROQ_API_KEY = "xxxxxxxxxxxxxxxxxxxxxx"
- ASTRA_DB_API_ENDPOINT = "https://xxxxxxxxxxxxxxxxxxxx-us-east-2.apps.astra.datastax.com"
- ASTRA_DB_APPLICATION_TOKEN = "AstraCS:xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
- ASTRA_DB_KEYSPACE = "default_keyspace"


### Use setup.py for installing your local package.

- <either mention -e . inside your requirements.txt Or run python setup.py install >


## How It Works

<img width="373" alt="Screenshot 2024-11-03 223741-rag" src="https://github.com/user-attachments/assets/201da001-aec5-4d82-92c8-0e1e8edf2dda">

![Screenshot 2024-11-13 113536](https://github.com/user-attachments/assets/fbd4f99b-fc72-487e-a59b-4178f4cab73e)

###### User Query: 
The user sends a query to the bot through the /chat endpoint.

###### Retrieval: 
Relevant product data is retrieved from AstraDB using vector similarity search.

###### Generation: 
The Mistral model on GROQ generates a response using the retrieved data.

###### Chat History & Memory: 
Past conversations and chat history are managed to provide contextual responses.

## Sample output

<img width="470" alt="Screenshot 2024-11-04 142808-app" src="https://github.com/user-attachments/assets/2cd5135c-2d54-4efb-b74f-d32fb9bc6a30">

## Customization

#### To customize the bot for other domains:

###### Modify Retrieval Data:
Update the dataset used in AstraDB to relevant information.

###### Fine-Tune Model:
Fine-tune the Mistral model if necessary.

###### Add More Endpoints: 

Extend the Flask app for additional functionalities as needed.

## Contributing

Feel free to fork the repository, make enhancements, and submit a pull request. We welcome contributions!

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments

GROQ for efficient model deployment.

AstraDB for robust vector storage capabilities.

Mistral Model for natural language processing and generation.

