import os
import streamlit as st
import google.generativeai as genai

from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

# -----------------------------
# Load Environment Variables
# -----------------------------
load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Gemini Model
model = genai.GenerativeModel("gemini-flash-latest")

# -----------------------------
# Load Embedding Model
# -----------------------------
@st.cache_resource
def load_vector_db():
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    db = FAISS.load_local(
        "vector_db",
        embeddings,
        allow_dangerous_deserialization=True
    )

    return db

db = load_vector_db()

# -----------------------------
# Streamlit Page Settings
# -----------------------------
st.set_page_config(
    page_title="AskMyDocs",
    page_icon="📄",
    layout="centered"
)
st.markdown("""
<style>
.stButton > button{
    background:#4F46E5;
    color:white;
    border-radius:12px;
    height:48px;
    width:180px;
    font-weight:bold;
    border:none;
}

.stButton > button:hover{
    background:#4338CA;
}

h1{
    color:#1F2937;
}

.stTextInput input{
    border-radius:10px;
}
</style>
""", unsafe_allow_html=True)

st.title("📚 AskMyDocs")
st.markdown("""
### Intelligent AI Document Assistant

Ask natural language questions and get accurate answers from your uploaded documents using **Retrieval-Augmented Generation (RAG)**.
""")
# -----------------------------
# User Input
# -----------------------------
question = st.text_input(
    "💬 Ask your document anything",
    placeholder="Example: What are the advantages of NoSQL databases?"
)

# -----------------------------
# Generate Answer
# -----------------------------
if st.button("🔍 AskMyDocs"):

    if question.strip() == "":
        st.warning("⚠ Please enter a question.")
    else:

        with st.spinner("Searching document and generating answer..."):

            try:
                # Retrieve top 5 relevant chunks
                docs = db.similarity_search(question, k=5)

                context = "\n\n".join(
                    [doc.page_content for doc in docs]
                )

                prompt = f"""
You are a helpful AI assistant.

Answer ONLY using the information provided below.

If the answer is not present in the context, reply:

"I couldn't find the answer in the provided document."

Context:
{context}

Question:
{question}

Answer:
"""

                response = model.generate_content(prompt)

                st.success("✨ AskMyDocs found the answer!")

                st.markdown("## 📖 AI Response")
                st.write(response.text)

            except Exception as e:
                st.error(f"Error: {e}")

st.markdown("---")

st.caption(
    "🚀 AskMyDocs • Powered by Gemini Flash • FAISS • HuggingFace Embeddings"
)