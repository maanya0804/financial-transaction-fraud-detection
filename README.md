# 🛡️ Financial Transaction Fraud Detection Pipeline

An end-to-end data science and risk analytics project that identifies fraudulent transactions using machine learning, evaluates performance via Precision-Recall AUC, and optimizes operating thresholds based on a custom business cost matrix.

---

## 📊 Project Architecture

1. **Exploratory Data Analysis & SQL Burst Detection (`01_eda_and_sql_analysis.ipynb`)**
   - Visualized transaction patterns and distributions across 284,807 transactions.
   - Executed SQL queries using `sqlite3` to flag high-frequency and high-value transaction bursts per account.

2. **Machine Learning & Threshold Optimization (`02_ml_model_and_threshold_optimization.ipynb`)**
   - **Class Imbalance Handling:** Applied **SMOTE** (Synthetic Minority Over-sampling Technique) to rebalance the training set (~0.17% fraud baseline).
   - **Model:** Trained a **Random Forest Classifier** focused on probability prediction.
   - **Evaluation Metric:** Used **Precision-Recall AUC (PR-AUC)** rather than accuracy due to extreme class imbalance.
   - **Business Cost Optimization:** Developed a financial cost matrix ($20 per false positive alert vs. $250 per missed fraud case) to select an optimal decision threshold of **0.33**, reducing total operational loss.

3. **Interactive Fraud Monitoring Dashboard (`app.py`)**
   - Built a **Streamlit** dashboard featuring live risk metrics, alert volume tracking, top flagged accounts, and an interactive decision-threshold slider.

---

## 🚀 How to Run

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/MaanyaSaikia/financial-transaction-fraud-detection.git](https://github.com/MaanyaSaikia/financial-transaction-fraud-detection.git)
   cd financial-transaction-fraud-detection