from data_extraction import courses
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
import pickle

def create_embeddings_and_store(courses):

    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    texts = [f"{course['title']}\n{course['description']}" for course in courses]

    vectorstore = FAISS.from_texts(texts, embeddings)

    with open("faiss_store.pkl", "wb") as f:
        pickle.dump(vectorstore, f)

    print("Vector store created and saved")

create_embeddings_and_store(courses)
