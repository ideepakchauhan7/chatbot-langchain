from flask import Flask, request, jsonify
from sentence_transformers import SentenceTransformer
from langchain_community.vectorstores import FAISS
import pickle
import os

app = Flask(__name__)

# Load the SentenceTransformer model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Load the vector store
vector_store_path = 'faiss_store.pkl'
if os.path.exists(vector_store_path):
    with open(vector_store_path, 'rb') as f:
        vector_store = pickle.load(f)
else:
    print(f"Warning: {vector_store_path} not found. Make sure to create and save the FAISS index first.")
    vector_store = None

@app.errorhandler(404)
def not_found(e):
    return jsonify({"error": "Resource not found"}), 404

@app.route("/") 
def index(): 
    return "hello"

@app.route('/chat', methods = ['POST'])
def chat():
    # Attempt to parse the JSON data from the request
    data = request.get_json(force=True, silent=True)
    
    print(data)
    if not data or 'message' not in data:
        return jsonify({"error": "No message provided"}), 400
    
    user_input = data['message']

    if vector_store is None:
        return jsonify({"error": "Vector store not initialized"}), 500

    # Generate embedding for the user query
    user_embedding = model.encode([user_input])[0]  # Get the first (and only) embedding

    # Retrieve the most relevant document
    docs = vector_store.similarity_search_by_vector(user_embedding, k=1)

    # Prepare the response based on retrieved documents
    if docs:
        response = docs[0].page_content
    else:
        response = "Sorry, I couldn't find any relevant information."

    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)