import os
import google.generativeai as genai
from dotenv import load_dotenv

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

# Load API key
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Load embedding model
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Load FAISS vector database
vector_db = FAISS.load_local(
    "vector_db",
    embeddings,
    allow_dangerous_deserialization=True
)

print("✅ RAG system ready!")

# Initialize Gemini model
model = genai.GenerativeModel("gemini-flash-latest")

while True:
    query = input("\nAsk a question (type 'exit' to quit): ")

    if query.lower() == "exit":
        print("👋 Goodbye!")
        break

    # Retrieve relevant documents
    docs = vector_db.similarity_search(query, k=3)

    context = "\n\n".join([doc.page_content for doc in docs])

    prompt = f"""
You are an AI assistant.

Answer ONLY using the information provided below.

Context:
{context}

Question:
{query}

Answer:
"""

    try:
        response = model.generate_content(prompt)

        print("\n==============================")
        print("Answer:\n")
        print(response.text)
        print("==============================")

    except Exception as e:
        print("\n❌ Error:")
        print(e)