import requests
from bs4 import BeautifulSoup
import pickle
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import os

def scrape(url):
    html = requests.get(url).text
    soup = BeautifulSoup(html, "html.parser")
    return soup.get_text()

def prepare_chunks(text, chunk_size=500):
    return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

def create_index(chunks):
    model = SentenceTransformer("all-MiniLM-L6-v2")
    embeddings = model.encode(chunks)
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(np.array(embeddings))
    return index, embeddings

if __name__ == "__main__":
    url = input("Enter a URL to scrape: ")
    text = scrape(url)
    chunks = prepare_chunks(text)

    index, embeddings = create_index(chunks)

    os.makedirs("data", exist_ok=True)
    with open("data/chunks.pkl", "wb") as f:
        pickle.dump(chunks, f)
    faiss.write_index(index, "data/index.faiss")

    print("Scraping and indexing complete.")
