# 💰 Income Prediction Using Machine Learning

## 📖 What Is This Project About? (Simple Explanation)

This project predicts whether a person earns more than $50,000 per year based on information like:

- Age
- Education
- Work type
- Working hours per week
- Marital status
- Occupation

In simple terms:

👉 The model looks at a person's details and predicts if their income is high or low.

This kind of problem is useful in:
- Financial risk analysis
- Market segmentation
- Business decision making
- Demographic research

---

## 🎯 Project Goal

To build a machine learning model that can accurately classify income into:

- **>50K (High Income)**
- **≤50K (Low Income)**

---

## 📊 Dataset Information

- Dataset: Adult Census Income Dataset
- Type: Structured tabular dataset
- Target variable: Income category
- Rows: ~32,000 records
- Features: Demographic & employment-related attributes

---

## ⚙️ How the Project Was Built

### 1️⃣ Data Cleaning
- Replaced missing values (including '?' entries)
- Handled null values properly
- Checked for low-variance features

### 2️⃣ Data Preparation
- Converted categorical data into numerical format (One-Hot Encoding)
- Scaled numerical features for better model performance
- Split data into training and testing sets (80% / 20%)

### 3️⃣ Model Training
I trained and compared multiple machine learning models:

- Logistic Regression
- K-Nearest Neighbors (KNN)
- Decision Tree
- Random Forest

### 4️⃣ Model Optimization
- Applied Hyperparameter Tuning using GridSearchCV
- Selected the best performing model

---

## 📈 Results

| Model              | Accuracy |
|--------------------|----------|
| Logistic Regression| 84%      |
| KNN                | 81%      |
| Decision Tree      | 79%      |
| Random Forest      | 83%      |

🏆 Best Accuracy Achieved: **84%**

---

## 📉 Model Evaluation

Evaluation was done using:

- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix

The model performs well overall and shows strong predictive capability for income classification.

---

## 🧠 Key Learning Outcomes

Through this project, I learned:

- How to preprocess real-world datasets
- Handling missing and categorical data
- Comparing multiple ML algorithms
- Hyperparameter tuning
- Evaluating classification models properly

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn

---
