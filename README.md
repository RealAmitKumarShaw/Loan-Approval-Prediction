# 🏦 Loan Approval Prediction

### IBM SkillsBuild Data Analytics with AI Internship 2026

**Author:** Amit Kumar Shaw  
**Internship ID:** IBMUEDA1168  
**Trainer:** Mr. Kartik Hooda  
**Institution:** Centurion University of Technology & Management  
**Domain:** Data Analytics / Machine Learning


## Project Overview
This project analyzes loan application data and builds machine learning classification models to predict whether a loan application will be **Approved** or **Rejected**.

**Workflow:** Data Understanding → Data Cleaning → EDA → Visualization → Feature Engineering → Model Training → Evaluation → Prediction → Streamlit Application

## Internship Project Context

This project was developed as part of the **IBM SkillsBuild Data Analytics with AI Internship 2026**. The project applies data analytics, exploratory data analysis, predictive analytics, machine learning, and interactive visualization concepts to a loan approval classification problem.

## Problem Statement
The objective is to analyze applicant and financial characteristics and develop a machine learning model that classifies loan applications as Approved or Rejected.

## Objectives
- Understand the dataset and data quality.
- Check missing values and duplicates.
- Perform exploratory data analysis and visualization.
- Analyze relationships among numerical features.
- Train and compare classification models.
- Evaluate models using Accuracy, Precision, Recall, and F1 Score.
- Identify important predictive features.
- Build an interactive Streamlit prediction application.

## Dataset
**Dataset:** Loan Approval Prediction Dataset  
**Source:** Kaggle  
**Dataset link:** https://www.kaggle.com/datasets/architsharma01/loan-approval-prediction-dataset

The dataset contains **4,269 loan applications and 13 columns**.

### Target
`loan_status` — Approved / Rejected

### Main Features
`loan_id`, `no_of_dependents`, `education`, `self_employed`, `income_annum`, `loan_amount`, `loan_term`, `cibil_score`, `residential_assets_value`, `commercial_assets_value`, `luxury_assets_value`, `bank_asset_value`

## Exploratory Data Analysis
The notebook includes dataset inspection, missing-value and duplicate checks, target distribution, numerical distributions, categorical comparisons, and correlation analysis.

## Machine Learning Models
1. Logistic Regression
2. Decision Tree
3. Random Forest

### Model Performance

| Model | Accuracy | Precision | Recall | F1 Score |
|---|---:|---:|---:|---:|
| Logistic Regression | 91.33% | 92.08% | 94.16% | 93.11% |
| Decision Tree | 98.36% | 98.32% | 99.06% | 98.67% |
| Random Forest | 98.13% | 98.31% | 98.68% | 98.50% |

On the current train-test split, Decision Tree achieved the highest scores among the evaluated models and was selected for the prediction demonstration.

## Feature Importance
The Decision Tree identified CIBIL score as the most influential feature (approximately 0.815), followed by loan term, loan amount, and annual income. Feature importance describes model behavior and does not establish causation.

## Streamlit Application
Run:

```bash
pip install -r requirements.txt
streamlit run app.py
```

The application uses:
- `Models/loan_approval_model.pkl`
- `Models/feature_names.pkl`

## ⚙️ Installation & Setup

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the Streamlit application

```bash
streamlit run app.py
```

## Project Structure

```text
IBM project/
├── Data/
│   └── loan_approval_dataset.csv
├── Models/
│   ├── feature_names.pkl
│   └── loan_approval_model.pkl
├── Notebooks/
│   └── Loan_Approval_Prediction.ipynb
├── Loan_Approval_Project_Report.docx
├── app.py
├── README.md
├── requirements.txt
└── .gitignore
```

## Key Insights
1. The dataset contains 4,269 applications, with approximately 62.22% approved and 37.78% rejected.
2. Approved applications generally show higher CIBIL scores than rejected applications.
3. Annual income and loan amount show a strong positive relationship.
4. Several asset-related variables are strongly correlated with income and loan amount.
5. CIBIL score was the most influential feature in the trained Decision Tree model.
6. Decision Tree achieved the highest scores among the three evaluated models on the current test set.

## Limitations
- Evaluation is based on a single train-test split.
- Performance may differ on new or real-world data.
- The dataset may not represent the complete criteria used by real financial institutions.
- Model probabilities are not guaranteed real-world approval probabilities.
- The system is a project-level decision-support demonstration, not a replacement for a real lending process.

## Future Scope
- Cross-validation and hyperparameter tuning.
- ROC-AUC and Precision-Recall analysis.
- Model explainability.
- Improved input validation.
- Cloud deployment.
- Evaluation on additional datasets.

## 👨‍💻 Author

**Amit Kumar Shaw**

- **Internship:** IBM SkillsBuild Data Analytics with AI Internship 2026
- **Internship ID:** IBMUEDA1168
- **Trainer:** Mr. Kartik Hooda
- **Institution:** Centurion University of Technology & Management
- **Domain:** Data Analytics / Machine Learning
