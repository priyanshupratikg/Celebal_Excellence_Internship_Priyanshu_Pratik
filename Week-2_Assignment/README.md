# End-to-End Machine Learning Pipeline on Tesla Deliveries & Production Data (2015–2025)

## Overview

This project was developed as part of the **Celebal Technologies Data Science Internship – Week 2 Assignment**. The objective was to build a complete end-to-end Machine Learning pipeline using Tesla's deliveries and production dataset (2015–2025). The project covers the entire ML workflow, including data preprocessing, exploratory data analysis (EDA), feature engineering, regression modeling, hyperparameter tuning, time series forecasting, model evaluation, and model persistence.

---

## Dataset

**Dataset:** Tesla Deliveries and Production Data (2015–2025)

The dataset contains information related to Tesla's:
- Estimated Deliveries
- Production Units
- Average Vehicle Price
- Battery Capacity
- Driving Range
- CO₂ Saved
- Charging Stations
- Vehicle Models
- Geographic Regions
- Source Type

---

## Project Workflow

The project follows a complete machine learning pipeline:

1. Data Loading
2. Data Understanding
3. Data Preprocessing
4. Exploratory Data Analysis (EDA)
5. Feature Engineering
6. Regression Modeling
7. Hyperparameter Tuning
8. Time Series Forecasting
9. Model Evaluation
10. Model Saving

---

## Exploratory Data Analysis

The EDA phase includes multiple visualizations to understand the dataset:

- Distribution plots
- Boxplots
- Correlation Heatmap
- Pairplot
- Line Charts
- Bar Charts
- Scatter Plots
- Feature Relationship Analysis

---

## Feature Engineering

Several new features were created to improve model performance, including:

- Delivery Efficiency
- Price per Kilometer
- CO₂ Saved per Delivery
- Charging Stations per Delivery
- Battery Efficiency

---

## Machine Learning Models

The following regression algorithms were implemented and compared:

- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor
- Gradient Boosting Regressor

The best-performing model was selected based on evaluation metrics.

---

## Hyperparameter Tuning

The Gradient Boosting Regressor was optimized using **GridSearchCV** to obtain the best combination of hyperparameters.

**Best Parameters**

- Learning Rate: 0.1
- Max Depth: 3
- Number of Estimators: 200
- Subsample: 0.8

---

## Model Performance

| Metric | Value |
|---------|-------|
| Best Model | Gradient Boosting Regressor |
| R² Score | 0.9995 |
| RMSE | 89.79 |
| MAE | 67.22 |

The Gradient Boosting model achieved excellent predictive performance with an R² score of approximately **99.95%**.

---

## Time Series Forecasting

Time series forecasting was performed using the **ARIMA** model to estimate Tesla's future deliveries.

Forecasts were generated for:

- 2026
- 2027
- 2028

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Statsmodels
- Joblib
- Google Colab

---

## Repository Structure

```
Week-2/
│
├── Week2_End_to_End_ML_Pipeline_Tesla_Deliveries.ipynb
├── tesla_deliveries_dataset_2015_2025.csv
├── best_gradient_boosting_model.pkl
└── README.md
```

---

## How to Run

1. Clone the repository.

```bash
git clone <repository-url>
```

2. Navigate to the Week-2 folder.

3. Install the required libraries.

```bash
pip install pandas numpy matplotlib seaborn scikit-learn statsmodels joblib
```

4. Open the notebook in Google Colab or Jupyter Notebook.

5. Run all cells sequentially.

---

## Results

- Successfully implemented an end-to-end Machine Learning pipeline.
- Performed comprehensive exploratory data analysis.
- Built and compared multiple regression models.
- Optimized the best model using GridSearchCV.
- Forecasted future deliveries using ARIMA.
- Saved the trained model for future inference.

---
## Dataset

The dataset used in this project is publicly available on Kaggle.

Dataset Link:
https://www.kaggle.com/datasets/nalisha/tesla-ea-deliveries-and-production-data20152025
## Author

**Priyanshu Pratik**

B.Tech Computer Science & Engineering (AI & ML)

ITER, Siksha 'O' Anusandhan University

