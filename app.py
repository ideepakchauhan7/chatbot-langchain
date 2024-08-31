from flask import Flask, request, jsonify
from sentence_transformers import SentenceTransformer
from langchain_community.vectorstores import FAISS
import pickle
import os

app = Flask(__name__)

model = SentenceTransformer('all-MiniLM-L6-v2')

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
    data = request.get_json(force=True, silent=True)
    
    print(data)
    if not data or 'message' not in data:
        return jsonify({"error": "No message provided"}), 400
    
    user_input = data['message']

    if vector_store is None:
        return jsonify({"error": "Vector store not initialized"}), 500
        
    user_embedding = model.encode([user_input])[0] 

    docs = vector_store.similarity_search_by_vector(user_embedding, k=1)

    if docs:
        response = docs[0].page_content
    else:
        response = "Sorry, I couldn't find any relevant information."

    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
