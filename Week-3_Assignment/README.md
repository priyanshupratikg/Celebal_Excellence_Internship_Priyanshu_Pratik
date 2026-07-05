# Customer Intelligence System using Classification, Ensemble Learning & Clustering

> **Celebal Technologies Data Science Internship – Week 3 Assignment**

---

# Overview

This project was developed as part of the **Celebal Technologies Data Science Internship – Week 3 Assignment**. The objective is to build an end-to-end **Customer Intelligence System** by combining **unsupervised learning**, **classification**, and **ensemble learning** techniques.

Using the **Country Development Dataset** provided by Kaggle, the project segments countries into meaningful groups based on socio-economic and health indicators. The discovered clusters are then used as target labels to train machine learning models capable of automatically predicting the development segment of unseen countries.

The project demonstrates the complete Machine Learning workflow, including data preprocessing, exploratory data analysis, clustering, feature engineering, supervised learning, model evaluation, visualization, and business insights.

---

# Problem Statement

HELP International, a humanitarian NGO, wants to identify countries that require immediate financial assistance and support. The organization has collected various socio-economic and health indicators for different countries.

The objective is to:

* Analyze the dataset
* Discover natural country segments
* Identify underdeveloped countries
* Build predictive models capable of classifying countries into the discovered development groups
* Generate actionable insights for better decision-making

---

# Dataset

**Dataset Name**

Country Data – Unsupervised Learning on Country Data

**Source**

Kaggle Dataset

[https://www.kaggle.com/datasets/rohan0301/unsupervised-learning-on-country-data](https://www.kaggle.com/datasets/rohan0301/unsupervised-learning-on-country-data)

---

# Dataset Description

The dataset contains socio-economic and health indicators of **167 countries**.

Features include:

| Feature    | Description                                   |
| ---------- | --------------------------------------------- |
| country    | Country name                                  |
| child_mort | Deaths of children under five per 1000 births |
| exports    | Exports as % of GDP                           |
| health     | Health expenditure as % of GDP                |
| imports    | Imports as % of GDP                           |
| income     | Net income per person                         |
| inflation  | Inflation rate                                |
| life_expec | Average life expectancy                       |
| total_fer  | Fertility rate                                |
| gdpp       | GDP per capita                                |

---

# Objectives

* Clean and preprocess the dataset
* Perform Exploratory Data Analysis (EDA)
* Scale numerical features
* Apply K-Means Clustering
* Apply DBSCAN Clustering
* Visualize clusters using PCA
* Profile each cluster
* Convert clusters into class labels
* Train Random Forest Classifier
* Train XGBoost Classifier
* Compare model performance
* Generate actionable business insights

---

# Machine Learning Workflow

```
Dataset
      │
      ▼
Data Cleaning
      │
      ▼
Exploratory Data Analysis
      │
      ▼
Feature Scaling
      │
      ▼
K-Means Clustering
      │
      ▼
DBSCAN Clustering
      │
      ▼
PCA Visualization
      │
      ▼
Cluster Profiling
      │
      ▼
Create Target Labels
      │
      ▼
Train-Test Split
      │
      ▼
Random Forest
      │
      ▼
XGBoost
      │
      ▼
Model Evaluation
      │
      ▼
Business Insights
```

---

# Technologies Used

* Python
* Google Colab
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* XGBoost

---

# Machine Learning Algorithms

## Unsupervised Learning

### K-Means Clustering

Used to divide countries into different development groups based on similar socio-economic characteristics.

---

### DBSCAN

Density-based clustering algorithm used to identify dense regions and detect noise or outlier countries.

---

### PCA (Principal Component Analysis)

Used for reducing feature dimensions to two principal components for cluster visualization.

---

## Supervised Learning

### Random Forest Classifier

An ensemble learning algorithm consisting of multiple decision trees used to predict country segments.

---

### XGBoost Classifier

A gradient boosting ensemble algorithm that improves prediction accuracy through sequential tree learning.

---

# Data Preprocessing

The following preprocessing steps were performed:

* Loaded CSV dataset
* Checked dataset dimensions
* Verified missing values
* Removed duplicate records
* Converted numerical columns
* Filled missing values using median
* Standardized numerical features using StandardScaler

---

# Exploratory Data Analysis

Performed:

* Dataset summary
* Statistical description
* Correlation Heatmap
* Feature distribution
* Boxplots
* Outlier inspection

---

# Clustering

## K-Means

Performed using standardized numerical features.

Steps:

* Applied StandardScaler
* Used Elbow Method
* Selected optimal number of clusters
* Assigned cluster labels

---

## DBSCAN

Performed to compare density-based clustering with K-Means.

Benefits:

* Detects noise
* Identifies dense regions
* Does not require predefined clusters

---

# PCA Visualization

Principal Component Analysis reduced the dataset into two dimensions for visualization.

This allows easy interpretation of country clusters.

---

# Cluster Profiling

Average values of all numerical features were calculated for every cluster to understand characteristics such as:

* Child mortality
* Income
* GDP per capita
* Health expenditure
* Fertility rate
* Life expectancy

---

# Classification

The generated K-Means cluster labels were used as target classes.

A supervised learning pipeline was developed for predicting cluster membership.

---

# Ensemble Learning

## Random Forest

* Train/Test Split
* Model Training
* Prediction
* Accuracy Evaluation
* Classification Report
* Confusion Matrix

---

## XGBoost

* Model Training
* Prediction
* Accuracy Evaluation
* Classification Report
* Confusion Matrix

---

# Model Comparison

Both ensemble learning algorithms were evaluated using:

* Accuracy Score
* Classification Report
* Confusion Matrix

The comparison helps determine which model predicts country segments more effectively.

---

# Feature Importance

Random Forest Feature Importance was plotted to identify the most influential socio-economic indicators contributing to country segmentation.

Important features include:

* Income
* GDP per capita
* Child Mortality
* Life Expectancy
* Total Fertility

---

# Business Insights

The analysis revealed several meaningful insights:

* Countries were successfully grouped into distinct socio-economic development segments.
* High-income clusters exhibited greater GDP per capita and longer life expectancy.
* Underdeveloped clusters showed higher child mortality and fertility rates.
* DBSCAN identified dense clusters while highlighting potential outliers.
* Random Forest and XGBoost accurately predicted country development groups.
* The developed Customer Intelligence System enables data-driven policy formulation and resource allocation.

---

# Repository Structure

```
Customer-Intelligence-System/
│
├── Customer_Intelligence_System.ipynb
├── Country-data.csv
├── data-dictionary.csv
├── README.md
├── requirements.txt
└── images/
    ├── correlation_heatmap.png
    ├── elbow_method.png
    ├── pca_visualization.png
    ├── feature_importance.png
```

---

# Installation

Clone the repository:

```bash
git clone https://github.com/your-username/Customer-Intelligence-System.git
```

Navigate to the project directory:

```bash
cd Customer-Intelligence-System
```

Install required libraries:

```bash
pip install -r requirements.txt
```

---

# Requirements

```
pandas
numpy
matplotlib
seaborn
scikit-learn
xgboost
```

---

# Results

* Successfully clustered countries using K-Means and DBSCAN.
* Visualized clusters using PCA.
* Built Random Forest and XGBoost classification models.
* Compared ensemble learning performance.
* Generated interpretable country profiles and business insights.
* Developed a complete Customer Intelligence System integrating clustering, classification, and ensemble learning.

---

# Learning Outcomes

Through this project, the following concepts were implemented:

* Data Cleaning
* Exploratory Data Analysis
* Feature Scaling
* Unsupervised Learning
* K-Means Clustering
* DBSCAN Clustering
* PCA
* Cluster Profiling
* Classification
* Ensemble Learning
* Random Forest
* XGBoost
* Model Evaluation
* Feature Importance
* Business Intelligence

---

# Acknowledgements

* **Celebal Technologies** – Data Science Internship Program
* **Kaggle** – Country Development Dataset
* **Scikit-learn** – Machine Learning Library
* **XGBoost** – Gradient Boosting Framework
* **Google Colab** – Development Environment

---

## Author

**Priyanshu Pratik**
B.Tech CSE (AI & ML)
ITER, Siksha 'O' Anusandhan (SOA) University
Data Science Intern – Celebal Technologies
