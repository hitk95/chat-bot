from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import subprocess
import os
import pickle

model = SentenceTransformer("all-MiniLM-L6-v2")

def load_chunks_and_index():
    with open("data/chunks.pkl", "rb") as f:
        chunks = pickle.load(f)
    index = faiss.read_index("data/index.faiss")
    return chunks, index

def search_chunks(query, chunks, index):
    q_embedding = model.encode([query])
    D, I = index.search(np.array(q_embedding), k=3)
    return [chunks[i] for i in I[0]]

def run_ollama(prompt):
    result = subprocess.run(
        ["ollama", "run", "mistral"],
        input=prompt.encode(),
        capture_output=True
    )
    return result.stdout.decode()

def get_response(query):
    chunks, index = load_chunks_and_index()
    relevant_chunks = search_chunks(query, chunks, index)
    context = "\n".join(relevant_chunks)
    prompt = f"Answer the question based on the following context:\n{context}\nQuestion: {query}"
    return run_ollama(prompt)
