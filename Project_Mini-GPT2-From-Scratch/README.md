
# 🧠 Mini GPT-2 From Scratch

### A Decoder-Only Transformer Language Model Built and Trained from Scratch

A complete implementation of a small GPT-2-style decoder-only Transformer language model built using **PyTorch** and trained from scratch on the **Tiny Shakespeare dataset**.

The project demonstrates the core architecture and training principles behind modern autoregressive Large Language Models (LLMs), without relying on a pretrained GPT model.

---

## 📌 Project Overview

Large Language Models such as GPT generate text by predicting the **next token** based on the tokens that have already been seen.

This project implements the same fundamental idea on a smaller scale by building a GPT-2-style Transformer from scratch.

The model learns the vocabulary, character patterns, sentence structures, formatting, and Shakespearean writing style present in the Tiny Shakespeare dataset.

The project begins with a simple **Bigram Language Model** as a baseline and progressively develops into a complete decoder-only Transformer architecture.

### Project Progression

```text
Tiny Shakespeare Dataset
        ↓
Character-Level Tokenization
        ↓
Character Encoding
        ↓
Train / Validation Split
        ↓
Batch Generation
        ↓
Bigram Language Model
        ↓
Baseline Training
        ↓
Causal Self-Attention
        ↓
Multi-Head Attention
        ↓
Feed-Forward Network
        ↓
Transformer Blocks
        ↓
GPT-2-Style Decoder-Only Transformer
        ↓
Next-Token Prediction
        ↓
Autoregressive Text Generation
        ↓
Model Checkpointing
        ↓
Interactive Gradio Interface
````

---

## 🎯 Objectives

The main objectives of this project are:

* Understand how GPT-style language models work internally
* Implement a Transformer architecture without using a pretrained LLM
* Understand tokenization and vocabulary creation
* Implement token and positional embeddings
* Implement causal self-attention
* Implement multi-head self-attention
* Build Transformer blocks
* Train the model using next-token prediction
* Implement autoregressive text generation
* Save and reload trained model checkpoints
* Create an interactive interface for text generation

---

## 🏗️ Model Architecture

The final model is a **decoder-only Transformer**, inspired by the architecture used in GPT-style language models.

### Architecture Configuration

| Component          |            Configuration |
| ------------------ | -----------------------: |
| Transformer Blocks |                        4 |
| Attention Heads    |                        4 |
| Parameters         |                    ~824K |
| Architecture       | Decoder-Only Transformer |
| Framework          |                  PyTorch |
| Dataset            |         Tiny Shakespeare |
| Tokenization       |          Character-Level |
| Training Objective |    Next-Token Prediction |
| Optimizer          |                    AdamW |

---

## 🔤 Character-Level Tokenization

Instead of using a pretrained tokenizer, this project creates its vocabulary directly from the Tiny Shakespeare dataset.

Every unique character in the dataset is assigned an integer ID.

For example:

```text
Input:
ROMEO:

Encoded:
[...integer token IDs...]
```

Two mappings are created:

* `stoi` — string/character to integer
* `itos` — integer to string/character

This allows the neural network to process text numerically and convert generated token IDs back into readable text.

---

## 🧩 Token Embeddings

The encoded tokens are passed through a trainable embedding layer.

The embedding layer converts each token ID into a dense numerical vector.

```text
Token ID
   ↓
Embedding Layer
   ↓
Dense Vector Representation
```

These vectors are then processed by the Transformer blocks.

---

## 📍 Positional Embeddings

Transformers do not inherently understand the order of tokens.

Therefore, positional embeddings are added to token embeddings.

```text
Token Embedding
       +
Position Embedding
       ↓
Transformer Input
```

This provides information about the position of each character within the sequence.

---

## 🔐 Causal Self-Attention

The model uses **causal self-attention**, which prevents the model from looking at future tokens while predicting the current token.

For example:

```text
R → O
R O → M
R O M → E
R O M E → O
```

The model can only use information that appeared before the token being predicted.

A lower-triangular attention mask is used to enforce this restriction.

This is a fundamental property of decoder-only GPT-style architectures.

---

## 🧠 Multi-Head Self-Attention

Multiple attention heads are used so the model can learn different relationships between tokens.

The architecture uses:

```text
4 Attention Heads
```

Each attention head independently calculates:

* Query
* Key
* Value

The outputs of all attention heads are concatenated and projected back into the model embedding dimension.

```text
Input
  ↓
 ┌────────┬────────┬────────┬────────┐
 │ Head 1 │ Head 2 │ Head 3 │ Head 4 │
 └────────┴────────┴────────┴────────┘
          ↓
      Concatenate
          ↓
    Linear Projection
          ↓
        Output
```

---

## 🔄 Feed-Forward Network

Each Transformer block contains a position-wise feed-forward neural network.

The network expands the embedding dimension and then projects it back.

```text
Input
  ↓
Linear Layer
  ↓
4 × Embedding Dimension
  ↓
ReLU
  ↓
Linear Layer
  ↓
Embedding Dimension
```

This allows the Transformer to learn nonlinear transformations of the representations produced by attention.

---

## 🧱 Transformer Block

Each Transformer block contains:

1. Layer Normalization
2. Multi-Head Self-Attention
3. Residual Connection
4. Layer Normalization
5. Feed-Forward Network
6. Residual Connection

Conceptually:

```text
Input
  │
  ├───────────────┐
  ↓               │
LayerNorm         │
  ↓               │
Multi-Head        │
Attention         │
  ↓               │
  └─── + ─────────┘
        │
        ↓
   LayerNorm
        ↓
Feed-Forward
        ↓
  ┌──── + ────────┐
  │               │
  └───────────────┘
        ↓
      Output
```

Multiple Transformer blocks are stacked to form the complete language model.

---

## 🤖 GPT Language Model

The final model consists of:

```text
Token Embedding
       +
Position Embedding
       ↓
Transformer Block 1
       ↓
Transformer Block 2
       ↓
Transformer Block 3
       ↓
Transformer Block 4
       ↓
Layer Normalization
       ↓
Language Model Head
       ↓
Vocabulary Logits
```

The language-model head produces a score for every possible character in the vocabulary.

The model then uses these scores to predict the next character.

---

## 🎯 Training Objective

The model is trained using **next-token prediction**.

Given a sequence:

```text
ROMEO:
```

the model learns to predict the next character based on the preceding context.

During training:

```text
Input:
ROMEO

Target:
OMEO:
```

More generally:

```text
Previous Tokens
       ↓
Transformer
       ↓
Probability Distribution
       ↓
Next Token
```

The training objective is to minimize **cross-entropy loss** between the predicted next token and the actual next token.

---

## ⚙️ Training Process

The dataset is divided into training and validation portions.

Batches of sequences are generated and provided to the model.

The training process follows:

```text
Dataset
   ↓
Tokenization
   ↓
Batch Generation
   ↓
Forward Pass
   ↓
Next-Token Predictions
   ↓
Cross-Entropy Loss
   ↓
Backpropagation
   ↓
AdamW Optimizer
   ↓
Parameter Updates
```

The model is trained iteratively to improve its ability to predict the next character.

---

## 📊 Bigram Baseline

Before implementing the Transformer, a simple **Bigram Language Model** is used as a baseline.

A Bigram model predicts the next token primarily from the immediately preceding token.

```text
Current Token
      ↓
Bigram Model
      ↓
Next Token
```

The Transformer improves upon this approach by allowing the model to use a much larger context through self-attention.

The final Transformer achieved approximately **57.6% lower validation loss than the Bigram baseline** in the project experiment.

---

## ✍️ Autoregressive Text Generation

After training, the model can generate text one character at a time.

The generation process is:

```text
Prompt
  ↓
Encode Prompt
  ↓
Transformer
  ↓
Predict Next Character
  ↓
Append Character
  ↓
Use Updated Context
  ↓
Predict Next Character
  ↓
Repeat
```

For example:

```text
Prompt:
ROMEO:
```

The model can generate Shakespeare-style text based on patterns learned from the training dataset.

---

## 🌡️ Temperature

The generation process includes a temperature parameter that controls the randomness of generated text.

### Lower Temperature

Produces more predictable and conservative outputs.

```text
Lower Temperature
       ↓
Less Randomness
       ↓
More Predictable Text
```

### Higher Temperature

Produces more diverse and unpredictable outputs.

```text
Higher Temperature
       ↓
More Randomness
       ↓
More Diverse Text
```

The interactive application allows the temperature to be adjusted dynamically.

---

## 💾 Model Checkpointing

After training, the trained model parameters and configuration are stored in a checkpoint file:

```text
mini_gpt2_shakespeare.pt
```

The checkpoint contains information required to reconstruct and use the trained model, including:

* Vocabulary size
* Embedding dimension
* Number of attention heads
* Number of Transformer layers
* Block size
* Dropout configuration
* Character-to-index mapping
* Index-to-character mapping
* Trained model parameters

This allows the trained model to be loaded later without retraining it from scratch.

---

## 🖥️ Interactive Gradio Application

The project includes an interactive **Gradio** interface for text generation.

The application provides controls for:

* Prompt
* Temperature
* Maximum generated characters
* Generate Text button

### Application Workflow

```text
User enters prompt
        ↓
Gradio Interface
        ↓
Generation Function
        ↓
Trained Mini GPT-2
        ↓
Autoregressive Generation
        ↓
Generated Shakespeare-style Text
```

The interface makes the trained Transformer accessible without requiring users to interact directly with the Python implementation.

---

## 🛠️ Technologies Used

| Technology          | Purpose                             |
| ------------------- | ----------------------------------- |
| Python              | Programming Language                |
| PyTorch             | Deep Learning Framework             |
| Torch.nn            | Neural Network Architecture         |
| Torch.nn.functional | Attention and activation operations |
| Gradio              | Interactive Web Interface           |
| Jupyter Notebook    | Development and experimentation     |
| Tiny Shakespeare    | Training Dataset                    |
| Git                 | Version Control                     |
| GitHub              | Source Code Repository              |

---

## 📁 Project Structure

```text
Project-Mini-GPT2-From-Scratch/
│
├── Mini_GPT2_From_Scratch_Priyanshu_Pratik_ITER_SOA_University.ipynb
│       └── Complete development and training notebook
│
├── model.py
│       └── GPT-2-style Transformer architecture
│
├── app.py
│       └── Gradio application for text generation
│
├── mini_gpt2_shakespeare.pt
│       └── Trained model checkpoint
│
├── requirements.txt
│       └── Python dependencies
│
└── .gitignore
        └── Git ignored files and folders
```

---

## 📓 Notebook

The Jupyter Notebook contains the development process of the project, including:

1. Dataset loading
2. Character-level tokenization
3. Vocabulary construction
4. Encoding and decoding
5. Train-validation split
6. Batch generation
7. Bigram baseline
8. Baseline training
9. Self-attention implementation
10. Multi-head attention
11. Feed-forward network
12. Transformer block
13. GPT-style language model
14. Training
15. Loss evaluation
16. Text generation
17. Model checkpointing

The notebook provides the complete learning and implementation progression from a simple language model to a Transformer.

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/priyanshupratikg/Celebal_Excellence_Internship_Priyanshu_Pratik.git
```

Navigate to the project directory:

```bash
cd Celebal_Excellence_Internship_Priyanshu_Pratik/Project-Mini-GPT2-From-Scratch
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Application

Run the Gradio application:

```bash
python app.py
```

The application will start a local Gradio server.

Open the displayed local URL in a browser and enter a prompt such as:

```text
ROMEO:
```

Adjust the temperature and maximum generation length, then select:

```text
✨ Generate Text
```

The trained Mini GPT-2 model will generate text based on the learned Shakespearean patterns.

---

## 🧪 Example Prompts

Example prompts that can be used with the model:

```text
ROMEO:
```

```text
JULIET:
```

```text
KING:
```

```text
What light
```

```text
O, my love
```

The quality and coherence of generated text depend on the small model size and the limited Tiny Shakespeare training dataset.

---

## 🔬 Key Concepts Demonstrated

This project provides an implementation-level understanding of several important concepts in modern NLP and Deep Learning:

* Language Modeling
* Character-Level Tokenization
* Vocabulary Encoding
* Token Embeddings
* Positional Embeddings
* Causal Attention
* Self-Attention
* Query, Key and Value representations
* Multi-Head Attention
* Feed-Forward Neural Networks
* Residual Connections
* Layer Normalization
* Dropout
* Transformer Blocks
* Decoder-Only Transformers
* Next-Token Prediction
* Cross-Entropy Loss
* AdamW Optimization
* Autoregressive Generation
* Temperature-Based Sampling
* Model Checkpointing
* PyTorch Model Serialization
* Interactive Model Deployment

---

## 📈 Model Limitations

This is an educational and experimental implementation of a GPT-style language model rather than a production-scale LLM.

The model has:

* A relatively small number of parameters
* Character-level tokenization
* A limited training dataset
* Limited context length
* Limited training compute
* No instruction tuning
* No reinforcement learning
* No large-scale pretraining corpus

Therefore, the generated text is intended to demonstrate the mechanics of autoregressive Transformer language modeling rather than compete with modern production LLMs.

---

## 🔮 Future Improvements

Possible extensions include:

* Larger Transformer architecture
* Larger and more diverse datasets
* Subword tokenization such as BPE
* Longer context windows
* More attention heads
* More Transformer layers
* Improved training schedules
* Learning-rate warmup
* Cosine learning-rate decay
* Better sampling strategies
* Top-k sampling
* Top-p sampling
* Larger model checkpoints
* GPU-optimized inference
* Improved web interface
* Public cloud deployment
* Model evaluation with additional language-model metrics

---

## 📚 Learning Outcome

This project provides an end-to-end understanding of how a GPT-style decoder-only Transformer can be constructed from fundamental components.

Instead of using a pretrained Transformer, the architecture is explicitly implemented using PyTorch, allowing each major component of the model to be studied and understood independently.

The project demonstrates the progression:

```text
Simple Language Model
        ↓
Attention
        ↓
Multi-Head Attention
        ↓
Transformer Blocks
        ↓
Decoder-Only Transformer
        ↓
GPT-Style Language Model
        ↓
Autoregressive Text Generation
        ↓
Interactive Application
```

---

## 👨‍💻 Author

**Priyanshu Pratik**

Data Science Intern
Celebal Technologies

B.Tech – Computer Science & Engineering
Specialization: Artificial Intelligence & Machine Learning
ITER, SOA University, Bhubaneswar

---

## 🙏 Acknowledgements

* PyTorch
* Gradio
* Tiny Shakespeare Dataset
* Transformer architecture and GPT-style language modeling research
* Celebal Technologies

---

## ⭐ Project

If you found this project useful or informative, consider giving the repository a ⭐ on GitHub.

**Built from scratch with PyTorch to understand the foundations of GPT-style Transformer language models.**

```
```
