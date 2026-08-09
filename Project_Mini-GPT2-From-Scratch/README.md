# 🧠 Mini GPT-2 From Scratch

### A Decoder-Only Transformer Language Model Built and Trained from Scratch

A complete implementation of a **GPT-2-style decoder-only Transformer language model** built from scratch using **PyTorch**.

The project starts with a simple **Bigram Language Model** as a baseline and progressively develops into a complete Transformer architecture featuring:

- Character-level tokenization
- Token embeddings
- Positional embeddings
- Causal self-attention
- Multi-head self-attention
- Feed-forward neural networks
- Residual connections
- Layer normalization
- Dropout
- Next-token prediction
- Cross-entropy loss
- AdamW optimization
- Autoregressive text generation
- Model checkpointing
- Interactive Gradio interface

The final Transformer achieved approximately **57.6% lower validation loss** than the Bigram baseline.

---

## 📌 Project Overview

Large Language Models such as GPT generate text by predicting the next token based on previously seen tokens.

This project demonstrates the core idea behind GPT-style language models by implementing a small Transformer **without using a pretrained GPT model**.

The model was trained from scratch on the **Tiny Shakespeare** dataset and learned the structure, vocabulary, formatting, and stylistic patterns of Shakespearean text.

The project follows this progression:

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
GPT-Style Decoder-Only Transformer
        ↓
Training with Next-Token Prediction
        ↓
Autoregressive Text Generation
        ↓
Model Checkpoint
        ↓
Gradio Web Interface
