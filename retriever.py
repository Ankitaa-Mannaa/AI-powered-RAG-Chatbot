import os
import pickle
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer
from utils import clean_text, chunk_sentences
import fitz 

EMBEDDING_MODEL = "all-MiniLM-L6-v2"
embedder = SentenceTransformer(EMBEDDING_MODEL)

def build_faiss_index(doc_path="documents/AI Training Document.pdf", save_dir="vector_store"):
    raw_text = extract_text_from_pdf(doc_path)
    cleaned = clean_text(raw_text)
    chunks = chunk_sentences(cleaned)

    embeddings = embedder.encode(chunks, show_progress_bar=True).astype("float32")
    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(embeddings)

    os.makedirs(save_dir, exist_ok=True)
    faiss.write_index(index, f"{save_dir}/document_index.faiss")
    with open(f"{save_dir}/doc_chunks.pkl", "wb") as f:
        pickle.dump(chunks, f)

def load_index():
    index = faiss.read_index("vector_store/document_index.faiss")
    with open("vector_store/doc_chunks.pkl", "rb") as f:
        chunks = pickle.load(f)
    return index, chunks

def retrieve_top_k_chunks(query, k=4):
    index, chunks = load_index()
    query_embedding = embedder.encode([query]).astype("float32")
    D, I = index.search(query_embedding, k)
    return [chunks[i] for i in I[0]]

def get_document_stats():
    _, chunks = load_index()
    return 1, len(chunks)

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = "\n".join(page.get_text() for page in doc)
    return text
