# 📚 AskMyDocs – RAG Document Question Answering System

A Retrieval-Augmented Generation (RAG) based AI application that allows users to ask natural language questions about a document and receive accurate answers using **Google Gemini**, **FAISS**, **LangChain**, and **HuggingFace Embeddings**.

The application retrieves the most relevant document chunks using semantic search and generates context-aware answers powered by Google's Gemini Flash model.

---

## 🌐 Live Demo

### 🚀 Streamlit App
https://askmydocs-rag.streamlit.app

### 💻 GitHub Repository
https://github.com/priyanshupratikg/Celebal_Excellence_Internship_Priyanshu_Pratik

---

## 📖 Project Overview

Traditional Large Language Models answer questions using their pretrained knowledge. However, they cannot reliably answer questions from private or custom documents.

This project implements a **Retrieval-Augmented Generation (RAG)** pipeline where:

1. A PDF document is converted into vector embeddings.
2. The embeddings are stored inside a FAISS vector database.
3. User questions are converted into embeddings.
4. The most relevant document chunks are retrieved.
5. Retrieved context is sent to Gemini Flash.
6. Gemini generates an answer strictly based on the retrieved document.

This ensures that answers are grounded in the uploaded document rather than relying solely on the LLM's general knowledge.

---

# 🚀 Features

- 📄 Ask questions about PDF documents
- 🤖 Google Gemini Flash integration
- 🔍 Semantic search using FAISS
- 🧠 HuggingFace Sentence Transformers
- ⚡ Fast document retrieval
- 💬 Natural language interaction
- ☁️ Fully deployed on Streamlit Cloud
- 🎨 Clean and responsive Streamlit interface
- ⌨️ Supports both button click and Enter key submission

---

# 🏗️ Project Architecture

```
                  User Question
                        │
                        ▼
             Sentence Transformer
             (Query Embedding)
                        │
                        ▼
               FAISS Vector Store
        Retrieve Top Relevant Chunks
                        │
                        ▼
             Google Gemini Flash
          (Context + User Question)
                        │
                        ▼
               AI Generated Answer
```

---

# 📂 Project Structure

```
Week-7_Assignment/
│
├── .streamlit/
│   └── config.toml              # Streamlit configuration
│
├── data/
│   └── NoSQL.pdf                # Source PDF document
│
├── vector_db/
│   ├── index.faiss              # FAISS vector index
│   └── index.pkl                # Metadata for vector database
│
├── app.py                       # Main Streamlit application
├── create_vector_db.py          # Generates FAISS vector database
├── rag.py                       # RAG helper functions
├── requirements.txt             # Python dependencies
├── README.md                    # Project documentation
├── .gitignore                   # Ignored files
└── .env                         # Local environment variables (not uploaded)
```

---

# ⚙️ Technologies Used

| Technology | Purpose |
|------------|----------|
| Python | Programming Language |
| Streamlit | Web Application |
| Google Gemini Flash | Large Language Model |
| LangChain | RAG Framework |
| HuggingFace | Text Embeddings |
| Sentence Transformers | Semantic Embeddings |
| FAISS | Vector Database |
| dotenv | Environment Variables |

---

# 🔄 Workflow

### Step 1

Load the PDF document.

↓

### Step 2

Split the document into manageable chunks.

↓

### Step 3

Generate embeddings using

```
sentence-transformers/all-MiniLM-L6-v2
```

↓

### Step 4

Store embeddings inside a FAISS Vector Database.

↓

### Step 5

User asks a question.

↓

### Step 6

Retrieve top matching document chunks.

↓

### Step 7

Provide retrieved context to Gemini Flash.

↓

### Step 8

Generate the final answer.

---

# 📦 Installation

Clone the repository

```bash
git clone https://github.com/priyanshupratikg/Celebal_Excellence_Internship_Priyanshu_Pratik.git

cd Celebal_Excellence_Internship_Priyanshu_Pratik/Week-7_Assignment
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file in the project directory.

```env
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
```

---

# ▶️ Running the Application

Generate the vector database (only once)

```bash
python create_vector_db.py
```

Run Streamlit

```bash
streamlit run app.py
```

---

# 💬 Example Questions

- What is NoSQL?
- What are the advantages of NoSQL databases?
- Explain the CAP theorem.
- What are the types of NoSQL databases?
- What is horizontal scaling?
- Difference between SQL and NoSQL.
- Explain consistency in NoSQL databases.

---

# 📸 Application Preview

### Home Page

Users can type natural language questions related to the uploaded document.

### AI Response

The application retrieves relevant information from the document and generates accurate responses using Gemini Flash.

---

# 🌍 Public Access

The application is deployed on **Streamlit Community Cloud**.

Anyone with the following link can access the application without installing anything:

## 🔗 https://askmydocs-rag.streamlit.app

Simply open the link in a browser and start asking questions.

---

# 📈 Future Improvements

- Multiple PDF support
- PDF upload functionality
- Chat history
- Conversation memory
- Citation highlighting
- Source page references
- Authentication
- Docker deployment
- Azure / AWS deployment

---

# 👨‍💻 Author

**Priyanshu Pratik**

Data Science Intern  
Celebal Technologies

---

# 🙏 Acknowledgements

- Google Gemini
- HuggingFace
- LangChain
- FAISS
- Streamlit
- Celebal Technologies

---

## ⭐ If you found this project useful, consider giving the repository a star!
