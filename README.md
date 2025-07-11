# 🧠 Legal Document Chatbot (RAG Pipeline with Mistral via OpenRouter)
A lightweight Retrieval-Augmented Generation (RAG) chatbot designed to answer queries based strictly on legal documents. This project combines document chunking, semantic search using FAISS, and OpenRouter’s mistral-7b-instruct model to deliver grounded, context-aware answers.

## 📌 How it works:
1. PDF document is parsed, cleaned, and broken into meaningful chunks.
2. Each chunk is converted to embeddings via all-MiniLM-L6-v2 and stored in a FAISS index.
3. At runtime, the user query is embedded and used to retrieve top relevant chunks.
4. A formatted prompt is created and sent to Mistral-7B via OpenRouter API.
5. The model replies based strictly on the retrieved chunks (RAG behavior).

## ⚙️ Setup Instructions
1. Install
- python -m venv venv
- source venv/bin/activate or venv\Scripts\activate on Windows
- pip install -r requirements.txt

2. Preprocessing & Embedding

Before running the chatbot, you need to preprocess and embed the document.

#Inside retriever.py

python -c "from retriever import build_faiss_index; build_faiss_index()"

This will:
- Extract text from documents/AI Training Document.pdf
- Clean and chunk it
- Generate embeddings using SentenceTransformers
- Build and save a FAISS index + chunk list to vector_store/

## 🤖 Running the Chatbot

Step-by-Step:

1. Make sure you have a valid OpenRouter API Key (https://openrouter.ai).
2. Add your key in generator.py
3. Launch the chatbot:streamlit run app.py
4. Go to http://localhost:8501 in your browser to chat with your legal assistant.

## 💡 Model and Embedding Choices

LLM: mistralai/mistral-7b-instruct via OpenRouter – optimized for instruction-following with low latency via API.

Embeddings: all-MiniLM-L6-v2 from sentence-transformers – lightweight and efficient for real-time semantic similarity.

## 🧪 Sample Queries & Responses
- Query: What is the purpose of AI training in legal compliance?

Response: Based on the document context, AI training ensures employees are aware of data protection regulations like GDPR, mitigating legal risk through awareness. [✓ Success]

- Query: xyz hello world?

Response: Gives a crafted legal answer even though the input is gibberish – shows hallucination tendency. [✗ Limitation]

## 🎥 Demo Video and Screenshots
🔗 Watch Demo link - https://drive.google.com/file/d/1Sc3deK3HDIlqsYiLs368Twkq3yXXiC4r/view?usp=sharing

![Chat UI](assets/01.png)
![Sample Query](assets/04.png)

