# 🧹 Week 6 Assignment - Image Denoising using Deep Learning Autoencoders

> **Celebal Technologies – Data Science Internship (Week 6)**

Developed a Deep Learning based Image Denoising System using Autoencoders on the MNIST dataset. The project focuses on reconstructing clean handwritten digit images from noisy inputs while comparing multiple autoencoder architectures and evaluating their performance using quantitative and qualitative metrics.

---

# 📌 Project Overview

Image denoising is a fundamental computer vision task that aims to recover clean images from corrupted or noisy observations. In this project, convolutional autoencoders are trained to learn compact latent representations of handwritten digits and reconstruct noise-free images.

The project begins with a baseline CNN Autoencoder and further extends to an enhanced Deep CNN Autoencoder incorporating Batch Normalization, Early Stopping, Learning Rate Scheduling, and advanced performance evaluation.

---

# 🎯 Objectives

- Build a Convolutional Autoencoder for image denoising.
- Generate noisy MNIST images using Gaussian Noise.
- Learn compressed latent representations of images.
- Reconstruct high-quality denoised images.
- Compare Basic and Deep CNN Autoencoders.
- Evaluate reconstruction quality using multiple metrics.
- Visualize learned feature representations and latent space.

---

# 📂 Dataset

**Dataset:** MNIST PNG Dataset

- 60,000 Training Images
- 10,000 Testing Images
- Image Size: **28 × 28**
- Grayscale Images
- 10 Digit Classes (0–9)

The dataset is included in this repository as:

```
mnist_png.zip
```

Directory Structure

```
mnist_png/
│
├── training/
│   ├── 0
│   ├── 1
│   ├── ...
│   └── 9
│
└── testing/
    ├── 0
    ├── ...
    └── 9
```

---

# ⚙️ Technologies Used

- Python
- TensorFlow
- Keras
- NumPy
- Matplotlib
- Scikit-Learn
- Scikit-Image
- Google Colab

---

# 🧠 Deep Learning Architectures

## 1️⃣ Basic CNN Autoencoder

Architecture

```
Input Image
      │
Conv2D (32)
      │
MaxPooling
      │
Conv2D (32)
      │
MaxPooling
      │
Latent Space
      │
Conv2D
      │
UpSampling
      │
Conv2D
      │
UpSampling
      │
Output Image
```

---

## 2️⃣ Deep CNN Autoencoder

Enhanced Architecture

- Additional Convolution Layers
- Batch Normalization
- Larger Feature Representation
- Better Reconstruction Quality

Architecture

```
Input
 │
Conv2D (32)
 │
Batch Normalization
 │
Conv2D (32)
 │
MaxPooling
 │
Conv2D (64)
 │
Batch Normalization
 │
Conv2D (64)
 │
MaxPooling
 │
Latent Space
 │
Conv2D (64)
 │
Batch Normalization
 │
UpSampling
 │
Conv2D (32)
 │
Batch Normalization
 │
UpSampling
 │
Output Image
```

---

# 🔄 Project Workflow

```
MNIST Dataset
        │
        ▼
Image Loading
        │
        ▼
Image Normalization
        │
        ▼
Gaussian Noise Injection
        │
        ▼
CNN Autoencoder
        │
        ▼
Deep CNN Autoencoder
        │
        ▼
Model Training
        │
        ▼
Image Reconstruction
        │
        ▼
Performance Evaluation
        │
        ▼
Visualization & Comparison
```

---

# 🚀 Advanced Features Implemented

✅ Basic CNN Autoencoder

✅ Deep CNN Autoencoder

✅ Batch Normalization

✅ Early Stopping

✅ Reduce Learning Rate on Plateau

✅ Model Checkpoint

✅ Feature Map Visualization

✅ Latent Space Visualization (PCA)

✅ Multiple Noise Level Analysis

✅ Model Comparison

---

# 📊 Evaluation Metrics

The reconstruction performance is evaluated using:

- Mean Squared Error (MSE)
- Peak Signal-to-Noise Ratio (PSNR)
- Structural Similarity Index (SSIM)

These metrics provide both numerical and perceptual assessment of image reconstruction quality.

---

# 📈 Visualizations

The notebook includes:

- Original Images
- Noisy Images
- Reconstructed Images
- Training & Validation Loss Curves
- Basic vs Deep Autoencoder Comparison
- Feature Map Visualization
- Latent Space Projection using PCA
- Noise Robustness Analysis
- Performance Bar Charts

---

# 📁 Project Structure

```
Week-6_Assignment/
│
├── week6_assignment_Priyanshu_Pratik_ITER_SOA University.ipynb
├── mnist_png.zip
├── README.md
```

---

# 💡 Key Learnings

- Working with Image Denoising using Deep Learning.
- Understanding Encoder-Decoder Architectures.
- Feature Extraction using CNNs.
- Latent Space Representation.
- Image Reconstruction Techniques.
- Performance Evaluation using MSE, PSNR and SSIM.
- Hyperparameter Optimization using Early Stopping and Learning Rate Scheduling.

---

# 🔮 Future Improvements

- Residual Autoencoders
- U-Net Based Denoising
- Variational Autoencoders (VAE)
- Color Image Denoising
- Real-world Noise Removal
- Diffusion-based Image Restoration

---

# 📚 References

- TensorFlow Documentation
- Keras Documentation
- MNIST Dataset
- Celebal Technologies Internship Resources

---

# 👨‍💻 Author

**Priyanshu Pratik**

**Data Science Intern**

**Celebal Technologies**
