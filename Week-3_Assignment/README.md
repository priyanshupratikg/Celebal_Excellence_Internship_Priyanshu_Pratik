# Customer Intelligence System using Classification, Ensemble Learning & Clustering

## Celebal Technologies Data Science Internship – Week 3 Assignment

---

## Project Overview

This project was developed as part of the **Celebal Technologies Data Science Internship – Week 3 Assignment**. The objective is to build an end-to-end **Customer Intelligence System** using both **unsupervised** and **supervised** machine learning techniques.

The project performs customer segmentation using clustering algorithms and then trains ensemble classification models to accurately predict customer groups. The resulting system provides meaningful insights into customer behavior and enables data-driven decision-making.

---

## Objective

The primary objectives of this project are to:

* Perform exploratory data analysis on country-level socioeconomic indicators.
* Preprocess and standardize the dataset for machine learning.
* Segment countries into meaningful groups using clustering algorithms.
* Compare clustering techniques using K-Means and DBSCAN.
* Build classification models to predict customer (country) segments.
* Evaluate ensemble learning techniques such as Random Forest and XGBoost.
* Generate actionable intelligence from the discovered customer segments.

---

## Dataset

**Dataset Name:** Country Data

The dataset contains socioeconomic and demographic information for multiple countries. Although the original data represents countries, each country is treated as an individual customer entity for segmentation and intelligence analysis.

### Files Included

* `Country-data.csv` – Main dataset used for model development.
* `data-dictionary.csv` – Description of dataset features.
* `Customer_Intelligence_System.ipynb` – Google Colab notebook containing the complete implementation.

---

## Dataset Features

| Feature    | Description                             |
| ---------- | --------------------------------------- |
| country    | Country name                            |
| child_mort | Child mortality rate                    |
| exports    | Exports as percentage of GDP            |
| health     | Health expenditure as percentage of GDP |
| imports    | Imports as percentage of GDP            |
| income     | Net income per person                   |
| inflation  | Inflation rate                          |
| life_expec | Average life expectancy                 |
| total_fer  | Fertility rate                          |
| gdpp       | GDP per capita                          |

---

## Technologies Used

* Python
* Google Colab
* NumPy
* Pandas
* Matplotlib
* Seaborn
* Scikit-learn
* XGBoost

---

## Machine Learning Workflow

### 1. Data Collection

* Loaded the Country Data dataset.
* Verified dataset dimensions and structure.
* Checked missing values and data types.

---

### 2. Data Preprocessing

The preprocessing stage included:

* Removing non-numeric identifier columns.
* Feature scaling using **StandardScaler**.
* Preparing data for clustering and classification.

---

### 3. Exploratory Data Analysis (EDA)

Performed comprehensive data analysis including:

* Statistical summary
* Feature distributions
* Correlation heatmap
* Identification of relationships among variables

The analysis helped understand economic and demographic patterns before clustering.

---

## Clustering Techniques

### K-Means Clustering

K-Means clustering was used to group countries with similar socioeconomic characteristics.

Steps performed:

* Standardized all numerical features.
* Determined the optimal number of clusters using the **Silhouette Score**.
* Assigned each country to its nearest cluster.
* Visualized clusters using Principal Component Analysis (PCA).

### DBSCAN Clustering

Density-Based Spatial Clustering (DBSCAN) was implemented to compare with K-Means.

Benefits:

* Detects clusters of arbitrary shapes.
* Identifies noise and outliers.
* Does not require specifying the number of clusters beforehand.

---

## Feature Visualization

The project includes visualizations such as:

* Correlation Heatmap
* Feature Distributions
* Silhouette Score Plot
* PCA Cluster Visualization
* Feature Importance Plot
* Confusion Matrix

These visualizations improve interpretability and provide better understanding of the model outputs.

---

## Classification Models

After generating clusters, the cluster labels were treated as target classes for supervised learning.

### Random Forest Classifier

Random Forest is an ensemble learning algorithm that combines multiple decision trees.

Advantages:

* High accuracy
* Robust against overfitting
* Handles nonlinear relationships
* Provides feature importance scores

Evaluation Metrics:

* Accuracy
* Classification Report
* Feature Importance

---

### XGBoost Classifier

Extreme Gradient Boosting (XGBoost) is an optimized gradient boosting algorithm known for exceptional predictive performance.

Advantages:

* Faster training
* High accuracy
* Regularization support
* Excellent performance on structured datasets

Evaluation Metrics:

* Accuracy
* Precision
* Recall
* F1-Score
* Confusion Matrix

---

## Customer Intelligence Insights

The generated customer segments reveal countries with similar socioeconomic characteristics.

Typical insights include:

* High-income developed countries
* Emerging economies with balanced development
* Developing countries requiring economic improvement
* Countries with high inflation or child mortality
* Similar GDP and healthcare expenditure patterns

These insights can support:

* Customer segmentation
* Market analysis
* Resource allocation
* Policy planning
* Strategic decision-making

---

## Project Structure

```text
Week 3 Assignment/
│
├── Customer_Intelligence_System.ipynb
├── Country-data.csv
├── data-dictionary.csv
├── README.md
└── requirements.txt
```

---

## Requirements

Install the required Python libraries using:

```bash
pip install -r requirements.txt
```

Required packages:

* numpy
* pandas
* matplotlib
* seaborn
* scikit-learn
* xgboost

---

## How to Run the Project

1. Open **Google Colab**.
2. Upload the notebook.
3. Upload `Country-data.csv` when prompted.
4. Run all notebook cells sequentially.
5. Observe clustering results, classification performance, and generated customer intelligence insights.

---

## Results

The project successfully demonstrates:

* Data preprocessing and feature engineering
* Exploratory Data Analysis
* Customer segmentation using K-Means
* Density-based clustering using DBSCAN
* Ensemble classification using Random Forest
* Gradient boosting using XGBoost
* Cluster visualization with PCA
* Performance evaluation using multiple metrics
* Actionable customer intelligence insights

---

## Learning Outcomes

Through this project, the following concepts were implemented:

* Data preprocessing
* Feature scaling
* Exploratory Data Analysis
* Customer segmentation
* Unsupervised learning
* Ensemble learning
* Classification algorithms
* Model evaluation
* Feature importance analysis
* PCA visualization

---

## Future Enhancements

Possible improvements include:

* Hyperparameter tuning using GridSearchCV or RandomizedSearchCV.
* Implementation of Hierarchical Clustering.
* Addition of Gaussian Mixture Models (GMM).
* Interactive dashboards using Streamlit or Power BI.
* Deployment as a web application using Flask or FastAPI.
* Automated model retraining pipelines.

---

## Conclusion

This project demonstrates a complete end-to-end Customer Intelligence System by integrating unsupervised and supervised machine learning techniques. K-Means and DBSCAN effectively identify meaningful customer segments, while Random Forest and XGBoost accurately predict these segments. The combination of clustering, ensemble learning, and visualization provides valuable insights that can support data-driven business strategies and customer intelligence applications.

---

## Author

**Priyanshu Pratik**

B.Tech – Computer Science & Engineering (AI & ML)

ITER, Siksha 'O' Anusandhan University

**Celebal Technologies Data Science Internship – Week 3 Assignment**

