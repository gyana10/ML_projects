# ML Projects and Concepts

A curated collection of Machine Learning projects and fundamental concepts implemented using Python and industry-standard libraries.

This repository demonstrates end-to-end Machine Learning workflows including:
- Data preprocessing
- Feature engineering
- Model training
- Model evaluation
- Cross-validation
- Hyperparameter tuning
- Visualization
- Model stability analysis

---

## 📌 1. Loan Approval Prediction (Project)

**Type:** Classification  
**Objective:** Predict whether a loan application will be approved based on applicant features.

### Concepts Covered:
- Data cleaning and preprocessing
- Handling missing values
- Feature engineering
- Encoding categorical variables
- Model training and evaluation

### Tools & Libraries:
Python, Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn

---

## 📌 2. Logistic Regression (Drug Classification)

**Type:** Classification  
**Algorithm:** Logistic Regression  
**Objective:** Predict the appropriate drug type for patients based on medical attributes.

### Concepts Covered:
- Data preprocessing using ColumnTransformer
- One-Hot Encoding
- Feature scaling using StandardScaler
- Train-test split
- Confusion Matrix visualization
- Classification Report (Precision, Recall, F1-score)

### Dataset:
- `drug200.csv`

---

## 📌 3. K-Nearest Neighbors (KNN) with K-Fold Cross Validation

**Type:** Classification  
**Algorithm:** K-Nearest Neighbors (KNN)  
**Objective:** Classify drug types using distance-based learning and evaluate performance using K-Fold Cross Validation.

### Concepts Covered:
- Pipeline integration
- ColumnTransformer
- Feature scaling
- K-Fold Cross Validation
- Accuracy per fold evaluation
- Mean Accuracy and Standard Deviation
- Cross-validation visualization (Bar plot, Boxplot)

### Dataset:
- `drug200.csv`

---

## 📌 4. KNN with Stratified K-Fold Cross Validation (Advanced Evaluation)

**Type:** Classification  
**Algorithm:** KNN with StratifiedKFold  
**Objective:** Maintain class balance across folds for reliable classification evaluation.

### Concepts Covered:
- StratifiedKFold (class distribution preservation)
- Model stability measurement
- Accuracy variance analysis
- Confusion Matrix visualization
- Cross-validation performance visualization

### Why StratifiedKFold?
Ensures each fold maintains the same class distribution as the original dataset, leading to more reliable performance estimates in classification tasks.

---

## 📌 5. KNN Hyperparameter Tuning (GridSearchCV)

**Type:** Classification Optimization  
**Objective:** Improve model accuracy by tuning hyperparameters.

### Concepts Covered:
- GridSearchCV
- Tuning:
  - n_neighbors
  - distance metric (Euclidean / Manhattan)
  - weight type (uniform / distance)
- Best parameter selection
- Improved cross-validation accuracy

---

## 📌 6. Linear Regression (Salary Prediction)

**Type:** Regression  
**Algorithm:** Simple Linear Regression  

### Concepts Covered:
- Train-test split
- Model fitting
- R² Score
- Mean Squared Error (MSE)

### Dataset:
- `Salary_dataset.csv`

---

## 📌 7. Multiple Linear Regression (Student Performance)

**Type:** Regression  
**Algorithm:** Multiple Linear Regression  

### Concepts Covered:
- Multiple feature modeling
- Coefficient interpretation
- Model evaluation

### Dataset:
- `Student_Performance.csv`

---

## 📌 8. Polynomial Regression

**Type:** Non-linear Regression  
**Algorithm:** Polynomial Regression  

### Concepts Covered:
- Polynomial feature transformation
- Curve fitting
- Overfitting vs Underfitting

---

## 📌 9. Linear Regression using Gradient Descent

**Type:** Regression  
**Algorithm:** Linear Regression (Gradient Descent / SGDRegressor)

### Concepts Covered:
- Cost function
- Gradient updates
- Learning rate tuning
- Convergence analysis

