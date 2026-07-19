# Deep Learning Text Generation using Vanilla RNN, LSTM, and GRU

## 📌 Project Overview

This project implements and compares three Recurrent Neural Network (RNN) architectures—**Vanilla RNN, Long Short-Term Memory (LSTM), and Gated Recurrent Unit (GRU)**—for the task of text generation. The models learn the sequential structure, grammar, and contextual dependencies of a text corpus to predict the next word and generate meaningful text.

The project also includes hyperparameter tuning, model comparison, and performance analysis using training loss, accuracy, generated text quality, and model complexity.

---

## 🎯 Objectives

- Build text generation models using Vanilla RNN, LSTM, and GRU.
- Learn text preprocessing and sequence generation techniques.
- Compare the performance of different recurrent neural network architectures.
- Generate coherent text using trained models.
- Analyze training loss, accuracy, and model complexity.
- Understand the impact of hyperparameter tuning on model performance.

---

## 🛠️ Technologies Used

- Python
- TensorFlow
- Keras
- NumPy
- Pandas
- Matplotlib

---

## 📚 Concepts Covered

- Natural Language Processing (NLP)
- Text Tokenization
- Word Embeddings
- Sequence Modeling
- Next Word Prediction
- Text Generation
- Vanilla RNN
- Long Short-Term Memory (LSTM)
- Gated Recurrent Unit (GRU)
- Hyperparameter Tuning
- Model Evaluation

---

## 📂 Project Workflow

### 1. Load Text Corpus
A custom AI and Machine Learning-based text corpus is used to train the models.

### 2. Data Preprocessing
- Tokenization
- Vocabulary Creation
- N-gram Sequence Generation
- Sequence Padding
- Input and Output Preparation

### 3. Model Building

Three different neural network architectures were implemented:

- Vanilla RNN
- LSTM
- GRU

Each model consists of:

- Embedding Layer
- Recurrent Layer
- Dense Output Layer

### 4. Model Training

All models were trained using:

- Optimizer: Adam
- Loss Function: Sparse Categorical Crossentropy
- Metric: Accuracy

### 5. Model Evaluation

The models were compared using:

- Training Loss
- Training Accuracy
- Generated Text Quality
- Number of Parameters
- Hyperparameter Comparison

---

## ⚙️ Hyperparameters Used

| Parameter | Value |
|-----------|--------|
| Embedding Dimension | 64 |
| Hidden Units | 128 |
| Epochs | 200 |
| Optimizer | Adam |
| Loss Function | Sparse Categorical Crossentropy |
| Activation Function | Softmax |

---

## ✨ Enhancements Implemented

The original notebook was enhanced by:

- Using a larger custom text corpus.
- Increasing embedding dimension from **32 to 64**.
- Increasing hidden units from **64 to 128**.
- Increasing training epochs from **100 to 200**.
- Generating longer text sequences (10 words).
- Testing the models with multiple seed sentences.
- Comparing training accuracy using visualization.
- Comparing model parameter counts.
- Creating a hyperparameter comparison table.
- Adding experimental observations.

---

## 📊 Results

The following comparisons were performed:

- Training Loss Comparison
- Training Accuracy Comparison
- Generated Text Comparison
- Model Parameter Comparison
- Hyperparameter Comparison

---

## 📈 Key Observations

- A larger text corpus improved vocabulary coverage and text generation quality.
- Increasing embedding dimensions produced richer semantic representations.
- Increasing hidden units enabled better learning of sequential patterns.
- Training for 200 epochs improved convergence and prediction accuracy.
- Vanilla RNN learned faster but struggled with long-term dependencies.
- LSTM generated the most contextually meaningful text because of its memory cell architecture.
- GRU achieved performance close to LSTM while training more efficiently.
- GRU provided the best balance between computational efficiency and prediction performance.

---

## 📁 Project Structure

```
Text_Generation_RNN_LSTM_GRU/
│
├── Text_Generation_RNN_LSTM_GRU_Learning_Project.ipynb
├── README.md
```

---

## 🚀 Future Improvements

- Train using larger datasets such as Shakespeare or Wikipedia.
- Use pretrained word embeddings like Word2Vec or GloVe.
- Implement Bidirectional LSTM and Bidirectional GRU.
- Integrate Attention Mechanism.
- Compare with Transformer-based language models.
- Save and deploy trained models for inference.

---

## 🎓 Learning Outcomes

This project helped in understanding:

- Sequence modeling using recurrent neural networks.
- Differences between Vanilla RNN, LSTM, and GRU.
- Text preprocessing techniques for NLP.
- Word embedding and sequence generation.
- Next-word prediction.
- Hyperparameter tuning.
- Model evaluation and comparison.
- Deep learning workflow for text generation.

---

## ✅ Conclusion

This project successfully demonstrates text generation using **Vanilla RNN, LSTM, and GRU**. After training and evaluation, **LSTM produced the most coherent and context-aware text**, while **GRU achieved nearly similar performance with lower computational complexity**. The enhancements made through hyperparameter tuning, larger training corpus, and additional performance analysis provided a deeper understanding of recurrent neural networks and sequence modeling.

---

## 👨‍💻 Author

**Priyanshu Pratik**

**Data Science Intern**  
**Celebal Technologies**
