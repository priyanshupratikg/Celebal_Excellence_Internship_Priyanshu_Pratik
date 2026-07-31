# 📄 Week 7 Assignment – Retrieval-Augmented Generation (RAG) Document Question Answering System

## 📌 Overview

This project implements a **Retrieval-Augmented Generation (RAG)** based Document Question Answering System using **Google Gemini**, **LangChain**, **FAISS**, **HuggingFace Embeddings**, and **Streamlit**.

The application enables users to ask natural language questions about an uploaded PDF document. Instead of answering from general knowledge, the system retrieves the most relevant information from the document using semantic search and generates context-aware responses with Google Gemini.

---

# 🎯 Objectives

- Load and process a PDF document.
- Convert document text into semantic embeddings.
- Store embeddings in a FAISS vector database.
- Retrieve relevant document chunks based on user queries.
- Generate accurate answers using Google's Gemini LLM.
- Build an interactive Streamlit web application.

---

# 🚀 Features

- 📄 PDF Document Processing
- ✂️ Intelligent Text Chunking
- 🤖 HuggingFace Sentence Embeddings
- ⚡ FAISS Vector Database
- 🔍 Semantic Similarity Search
- 🧠 Google Gemini LLM Integration
- 💬 Interactive Streamlit User Interface
- 📚 Retrieval-Augmented Generation (RAG)
- ⚠️ Error Handling and User-Friendly Messages

---

# 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| Streamlit | Web Application |
| Google Gemini API | Large Language Model |
| LangChain | RAG Pipeline |
| FAISS | Vector Database |
| HuggingFace Embeddings | Text Embeddings |
| Sentence Transformers | Embedding Model |
| PyPDFLoader | PDF Processing |
| python-dotenv | Environment Variable Management |

---

# 📂 Project Structure

```
Week-7_Assignment/
│
├── .streamlit/
│   └── config.toml
│      └── Streamlit configuration file for application settings.
│
├── data/
│   └── NoSQL.pdf
│      └── Source PDF document used for question answering.
│
├── vector_db/
│   ├── index.faiss
│   └── index.pkl
│      └── FAISS vector database storing document embeddings.
│
├── app.py
│   └── Streamlit web application for user interaction.
│
├── create_vector_db.py
│   └── Creates embeddings and builds the FAISS vector database.
│
├── rag.py
│   └── Command-line RAG application for testing.
│
├── requirements.txt
│   └── Python project dependencies.
│
├── README.md
│   └── Project documentation.
│
└── .gitignore
    └── Excludes unnecessary files from Git.
```

---

# ⚙️ Installation

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/<your-username>/<repository-name>.git

cd Week-7_Assignment
```

---

## 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

Activate the environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Configure API Key

Create a `.env` file in the project root.

```env
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
```

---

## 5️⃣ Create Vector Database

```bash
python create_vector_db.py
```

This will:

- Load the PDF
- Split the document into chunks
- Generate embeddings
- Create the FAISS vector database

---

## 6️⃣ Run Command-Line RAG

```bash
python rag.py
```

Example

```
Ask a question:
What is NoSQL?

Answer:
NoSQL is a non-relational database designed for scalability and distributed data storage.
```

---

## 7️⃣ Run Streamlit Application

```bash
streamlit run app.py
```

Open your browser

```
http://localhost:8501
```

---

# 🔄 Workflow

```
PDF Document
      │
      ▼
Load Document
      │
      ▼
Text Chunking
      │
      ▼
Generate Embeddings
      │
      ▼
Store in FAISS
      │
      ▼
User Question
      │
      ▼
Semantic Search
      │
      ▼
Retrieve Relevant Chunks
      │
      ▼
Google Gemini
      │
      ▼
Generated Answer
```

---

# 🧠 RAG Pipeline

### Step 1

Load the PDF document.

### Step 2

Split the document into smaller chunks.

### Step 3

Generate vector embeddings using HuggingFace Sentence Transformers.

### Step 4

Store embeddings inside the FAISS vector database.

### Step 5

Accept the user's question.

### Step 6

Perform semantic similarity search.

### Step 7

Retrieve the most relevant document chunks.

### Step 8

Send the retrieved context and question to Google Gemini.

### Step 9

Display the generated answer.

---

# 💡 Sample Questions

- What is NoSQL?
- What are the advantages of document databases?
- Explain horizontal scaling.
- What is sharding?
- What are the features of NoSQL databases?
- Compare SQL and NoSQL.
- Why is NoSQL suitable for Big Data?
- Explain replication in NoSQL.

---

# 📸 Output

The Streamlit application provides:

- Clean and interactive interface
- Question input field
- Loading spinner during processing
- Success notification
- AI-generated context-aware answer

---

# 📈 Future Improvements

- Multiple PDF support
- Upload custom documents
- Conversation memory
- Chat interface
- Source citation for retrieved chunks
- Hybrid search (BM25 + Vector Search)
- Support for multiple document formats
- Persistent database management

---

# 🎓 Learning Outcomes

Through this project, the following concepts were implemented:

- Retrieval-Augmented Generation (RAG)
- Semantic Search
- Vector Databases
- Text Embeddings
- Large Language Models (LLMs)
- LangChain Framework
- FAISS
- Streamlit Deployment
- Google Gemini API Integration

---

# 👨‍💻 Author

**Priyanshu Pratik**

**Data Science Intern**  
**Celebal Technologies**

---

# 📜 License

This project is developed for educational purposes as part of the **Celebal Technologies Data Science Internship – Week 7 Assignment**.
