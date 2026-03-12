# ML Projects and Concepts

A structured collection of Machine Learning projects demonstrating end-to-end workflows using Python and industry-standard libraries.

This repository covers:

- Data preprocessing & feature engineering  
- Model building (Regression & Classification)  
- Cross-validation techniques  
- Hyperparameter tuning  
- Model evaluation & visualization  
- Performance stability analysis  

---

## 📌 1. Loan Approval Prediction

**Type:** Classification  
**Objective:** Predict loan approval status based on applicant features.

**Key Concepts:**
- Data cleaning & preprocessing  
- Handling missing values  
- Encoding categorical variables  
- Model training & evaluation  

---

## 📌 2. Logistic Regression (Drug Classification)

**Type:** Classification  
**Dataset:** `drug200.csv`  
**Objective:** Predict drug type based on patient attributes.

**Key Concepts:**
- ColumnTransformer & Pipeline  
- One-Hot Encoding  
- Feature scaling (StandardScaler)  
- Train-test split  
- Confusion Matrix & Classification Report  

---

## 📌 3. Naive Bayes Classification (Diabetes Prediction)

**Type:** Classification  
**Dataset:** `Naive-Bayes-Classification-Data.csv`  
**Objective:** Predict whether a patient has diabetes based on medical indicators such as glucose level and blood pressure.

**Key Concepts:**
- Gaussian Naive Bayes  
- Probabilistic classification using Bayes theorem  
- Train-test split  
- Model evaluation using Accuracy and Classification Report  
- Confusion Matrix visualization  

---

## 📌 4. K-Nearest Neighbors (KNN)

**Type:** Classification  
**Dataset:** `drug200.csv`

### Implementations:
- KNN with K-Fold Cross Validation  
- KNN with Stratified K-Fold  
- Hyperparameter tuning using GridSearchCV  

**Key Concepts:**
- Distance-based learning  
- Model stability (Mean & Std of accuracy)  
- Class balance handling  
- Cross-validation visualization  

---

## 📌 5. Decision Tree Classification (Breast Cancer Prediction)

**Type:** Classification  
**Dataset:** `cancer_classification.csv`  
**Objective:** Predict whether a tumor is **Benign (0)** or **Malignant (1)** using medical diagnostic features.

**Key Concepts:**
- Decision Tree modeling  
- Tree depth control to prevent overfitting  
- Feature importance analysis  
- Confusion Matrix visualization  
- Decision Tree visualization using `plot_tree()`  

---

## 📌 6. Decision Tree Regression (Student Performance Prediction)

**Type:** Regression  
**Dataset:** `Student_Performance.csv`  
**Objective:** Predict a student's **Performance Index** based on study hours, sleep hours, previous scores, extracurricular activities, and other academic factors.

**Key Concepts:**
- Decision Tree Regressor modeling  
- Handling categorical variables (Yes/No → 1/0 encoding)  
- Train-test split for regression tasks  
- Model evaluation using **R² Score** and **Mean Squared Error (MSE)**  
- Feature importance visualization  
- Decision Tree regression visualization using `plot_tree()`  

---

## 📌 7. Linear Regression (Salary Prediction)

**Type:** Regression  
**Dataset:** `Salary_dataset.csv`

**Key Concepts:**
- Train-test split  
- R² Score & Mean Squared Error (MSE)  
- Regression visualization  

---

## 📌 8. Multiple Linear Regression (Student Performance)

**Type:** Regression  
**Dataset:** `Student_Performance.csv`

**Key Concepts:**
- Multi-feature modeling  
- Coefficient interpretation  
- Model evaluation  

---

## 📌 9. Polynomial Regression

**Type:** Non-linear Regression  

**Key Concepts:**
- Polynomial feature transformation  
- Curve fitting  
- Overfitting vs Underfitting analysis  

---

## 📌 10. Linear Regression using Gradient Descent

**Type:** Regression  

**Key Concepts:**
- Cost function minimization  
- Learning rate tuning  
- Convergence analysis  
- SGDRegressor implementation  

---

# 🔑 Core Machine Learning Concepts Covered

- Data Cleaning & Preprocessing  
- Feature Engineering  
- Encoding Techniques  
- Feature Scaling  
- Train-Test Split  
- K-Fold & Stratified K-Fold Cross Validation  
- Hyperparameter Tuning (GridSearchCV)  
- Model Evaluation (Accuracy, R², MSE, Precision, Recall, F1-score)  
- Decision Tree Modeling & Visualization  
- Probabilistic Modeling with Naive Bayes  
- Model Stability & Bias-Variance Tradeoff  

---

This repository reflects practical implementations of fundamental Machine Learning algorithms with structured experimentation, evaluation strategies, and visualization techniques.