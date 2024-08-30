from flask import Flask, request, jsonify
from sentence_transformers import SentenceTransformer
from langchain_community.vectorstores import FAISS
import pickle

app = Flask(__name__)

# Load the SentenceTransformer model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Load the vector store
# Load the vector store from the pickle file
with open('faiss_store.pkl', 'rb') as f:
    vector_store = pickle.load(f)
    
@app.errorhandler(404)
def not_found(e):
    return jsonify({"error": "Resource not found"}), 404

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    if not user_input:
        return jsonify({"error": "No message provided"}), 400
    
    # Generate embedding for the user query
    user_embedding = model.encode([user_input])
    
    # Retrieve the most relevant document
    docs = vector_store.similarity_search_by_vector(user_embedding, k=1)
    
    # Prepare the response based on retrieved documents
    if docs:
        response = docs[0].page_content
    else:
        response = "Sorry, I couldn't find any relevant information."
    
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run()
