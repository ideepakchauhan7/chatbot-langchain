# Flask Chatbot API

This project is a simple RESTful API built with Flask that serves as a chatbot interface. The API leverages embeddings generated using SentenceTransformers and stores them in a FAISS vector store. The vector store is saved as a pickle file (`.pkl`) and loaded by the API to handle user queries.

## Features

- **Chatbot Interface**: Allows users to interact with a chatbot by sending POST requests.
- **Vector Store**: Uses FAISS to store embeddings for quick retrieval.
- **Custom 404 Error Handling**: Returns a JSON response when a resource is not found.
- **Open-Source and Free**: Built using open-source libraries like Flask, FAISS, and SentenceTransformers.

## Installation

### Prerequisites

- Python 3.6 or higher
- `pip` package manager

### Clone the Repository

```bash
git clone https://github.com/your-username/flask-chatbot-api.git
cd flask-chatbot-api
```
### Install Dependencies

```bash
pip install -r requirements.txt
```


