
# 🖼️ CIFAR-10 Image Classification using ANN & CNN
### Celebal Technologies Data Science Internship – Week 4 Assignment

## 📌 Project Overview

This project focuses on building and comparing **Artificial Neural Networks (ANN)** and **Convolutional Neural Networks (CNN)** for image classification using the **CIFAR-10** dataset. The objective is to understand the advantages of CNNs over traditional ANNs and analyze how different architectures and training strategies affect model performance.

In addition to implementing the baseline models, several experiments were conducted to evaluate the impact of different optimizers, CNN architectures, and data augmentation techniques.

---

# 🎯 Objectives

- Build an Artificial Neural Network (ANN) for image classification.
- Build a Convolutional Neural Network (CNN) for image classification.
- Compare ANN and CNN performance.
- Analyze the effect of different CNN architectures.
- Compare different optimization techniques.
- Study the impact of data augmentation.
- Evaluate models using multiple performance metrics.

---

# 📂 Dataset

**Dataset:** CIFAR-10

The CIFAR-10 dataset consists of **60,000 RGB images** of size **32 × 32 × 3** distributed across **10 classes**.

- Training Images: **50,000**
- Testing Images: **10,000**

### Classes

- ✈️ Airplane
- 🚗 Automobile
- 🐦 Bird
- 🐱 Cat
- 🦌 Deer
- 🐶 Dog
- 🐸 Frog
- 🐴 Horse
- 🚢 Ship
- 🚚 Truck

Dataset Source:
https://www.cs.toronto.edu/~kriz/cifar.html

---

# 🛠️ Technologies Used

- Python
- TensorFlow
- Keras
- NumPy
- Pandas
- Matplotlib
- Scikit-learn

---

# 📚 Deep Learning Concepts Covered

- Artificial Neural Networks (ANN)
- Convolutional Neural Networks (CNN)
- Forward Propagation
- Backpropagation
- Activation Functions (ReLU, Softmax)
- Convolution Layers
- Pooling Layers
- Batch Normalization
- Dropout
- Data Augmentation
- Model Evaluation
- Classification Report
- Confusion Matrix

---

# ⚙️ Project Workflow

## 1. Import Libraries

Imported all required deep learning and visualization libraries.

---

## 2. Load Dataset

Loaded the CIFAR-10 dataset directly from TensorFlow.

---

## 3. Data Visualization

Visualized sample images from different classes to understand the dataset.

---

## 4. Data Preprocessing

Performed normalization by scaling pixel values from **0–255** to **0–1**.

For ANN:
- Flattened images into one-dimensional vectors.

For CNN:
- Preserved the original image dimensions.

---

# 🤖 Model 1 – Artificial Neural Network (ANN)

### Architecture

- Input Layer (3072 neurons)
- Dense Layer (512)
- Dropout
- Dense Layer (256)
- Output Layer (10 neurons)

### Characteristics

- Images flattened into vectors.
- Does not preserve spatial information.
- Suitable as a baseline model.

---

# 🧠 Model 2 – Convolutional Neural Network (CNN)

### Architecture

- Conv2D
- Batch Normalization
- MaxPooling
- Conv2D
- Batch Normalization
- MaxPooling
- Conv2D
- Flatten
- Dense
- Dropout
- Output Layer

### Advantages

- Learns spatial relationships.
- Extracts edges and textures.
- Performs hierarchical feature extraction.
- Produces higher classification accuracy.

---

# 🔬 Additional Experiments

To satisfy the assignment requirement of analyzing different architectures and training strategies, additional experiments were conducted.

## Experiment 1 – Optimizer Comparison

Compared CNN performance using:

- Adam Optimizer
- SGD Optimizer

Observation:

- Adam converged faster.
- Adam achieved better accuracy.
- SGD required more iterations.

---

## Experiment 2 – CNN Architecture Comparison

Implemented a deeper CNN architecture by increasing convolutional layers.

Observation:

- Improved feature extraction.
- Better classification accuracy.
- More robust learning.

---

## Experiment 3 – Data Augmentation

Applied:

- Random Flip
- Random Rotation
- Random Zoom

Observation:

- Improved generalization.
- Reduced overfitting.
- Increased robustness.

---

# 📈 Performance Evaluation

Models were evaluated using:

- Test Accuracy
- Validation Accuracy
- Learning Curves
- Classification Report
- Confusion Matrix
- Sample Predictions

---

# 📊 Comparison

The notebook compares:

- ANN vs CNN
- Adam vs SGD
- Basic CNN vs Improved CNN
- CNN with vs without Data Augmentation

These comparisons demonstrate how architecture and training strategies influence model performance.

---

# 📋 Evaluation Metrics

- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix

---

# 🔍 Key Observations

### Artificial Neural Network (ANN)

- Converts images into flattened vectors.
- Ignores spatial relationships.
- Lower classification accuracy.

---

### Convolutional Neural Network (CNN)

- Preserves image structure.
- Learns edges and object features.
- Significantly higher accuracy.

---

### Optimizer Analysis

Adam optimizer:

- Faster convergence
- Better optimization
- Higher final accuracy

SGD optimizer:

- Slower convergence
- Lower accuracy compared to Adam

---

### Data Augmentation

Applying augmentation:

- Increased training diversity
- Improved generalization
- Reduced overfitting

---

### Improved CNN

Adding more convolution layers:

- Better feature extraction
- Improved classification performance
- Higher accuracy than the baseline CNN

---

# 📌 Results

The experiments demonstrate that:

- CNN significantly outperforms ANN.
- Adam optimizer performs better than SGD.
- Data augmentation improves model robustness.
- A deeper CNN architecture achieves better accuracy.
- CNN is the preferred architecture for image classification problems.

---

# 🚀 Future Improvements

Future enhancements may include:

- Early Stopping
- Learning Rate Scheduling
- Hyperparameter Tuning
- Transfer Learning
- ResNet50
- EfficientNet
- MobileNet
- DenseNet
- Xception

---

# 📖 Learning Outcomes

Through this project, the following concepts were learned:

- Image preprocessing
- ANN implementation
- CNN implementation
- Feature extraction
- Convolution and Pooling
- Batch Normalization
- Dropout
- Data Augmentation
- Model evaluation
- Architecture comparison
- Performance analysis

---

# ✅ Conclusion

This project successfully implemented both Artificial Neural Networks (ANN) and Convolutional Neural Networks (CNN) for image classification on the CIFAR-10 dataset.

The baseline ANN provided a simple benchmark, while the CNN demonstrated superior performance by effectively learning spatial features through convolutional operations.

Additional experiments involving optimizer comparison, CNN architecture improvements, and data augmentation further highlighted how different design choices and training strategies impact model performance.

Overall, this project provided hands-on experience with the complete deep learning workflow—from data preprocessing and model development to evaluation and performance analysis—while reinforcing why CNNs are the preferred choice for modern computer vision tasks.

---

## 👨‍💻 Author

**Priyanshu Pratik**

Data Science Intern  
Celebal Technologies
