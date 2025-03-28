# HealthInsight: Stroke Risk Prediction

## Introduction
HealthInsight is a machine learning project aimed at predicting the likelihood of a stroke based on various health indicators. The project follows the complete ML lifecycle—from data preprocessing to model deployment—to create a reliable stroke risk prediction system.

## Problem Statement
The goal of this project is to predict whether an individual is at risk of a stroke based on features such as age, gender, smoking status, BMI, glucose levels, and medical history. Stroke is a leading cause of death worldwide, and early detection can save lives. The dataset used contains 12 attributes with over 5,000 records, presenting an imbalanced target variable (only 5% stroke cases).

## Data Collection & Cleaning
- **Dataset:** Sourced from Kaggle.
- **Cleaning Steps:**
  - Checked and found no duplicates.
  - Handled missing values in BMI (~4% missing) using median imputation.
  - Dropped irrelevant columns ('id', 'gender', 'residence_type').
  - Outlier detection and treatment using the 3-sigma rule for BMI.
  - Conducted feature correlation analysis using the Chi-squared test.

## Exploratory Data Analysis (EDA)
- Age is a significant predictor—people over 60 have a higher stroke risk.
- High glucose levels (above 200) correlate with strokes.
- Individuals with hypertension and heart disease have an elevated stroke risk (12-17%).
- Weak correlation was observed with BMI and smoking status.
- Addressed target imbalance as part of preprocessing.

## Feature Engineering & Preprocessing
- Applied **OneHotEncoding** for categorical variables.
- Used **PowerTransformer** for normalizing skewed numerical features.
- Standardized numerical features with **StandardScaler**.
- Addressed class imbalance using **RandomOverSampler** and **SMOTE**.
- Checked for multicollinearity using correlation heatmaps and **VIF** analysis.

## Model Training & Evaluation
- Models trained: **Random Forest, XGBoost, Logistic Regression, KNN**.
- Used an 80-20 train-test split.
- Evaluated with **accuracy, F1-score, precision, recall, ROC-AUC**, prioritizing recall.
- Hyperparameter tuning with **RandomizedSearchCV**.
- **Final Model:** Random Forest with 92% accuracy and 0.90 F1-score.
- **Deployment:** Saved the model as a pipeline using **Joblib**.

## Results & Deployment
- The model predicts stroke risk effectively based on input features.
- Deployed as a reusable pipeline, ready for integration into healthcare applications.

## Additional Implementation: Disease Diagnosis
In addition to stroke prediction, I have implemented a general **disease diagnosis model** using ML techniques, aiming to classify and predict various health conditions based on patient data.

## Learnings & Key Takeaways
- Handling imbalanced datasets significantly improves real-world model performance.
- Statistical tests like the **Chi-squared test** help in feature selection.
- Optimizing recall ensures that high-risk patients are correctly identified.
- Machine learning can provide impactful healthcare solutions.

---
### Resources
- **Dataset:** [Kaggle Stroke Prediction Dataset](https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset)
- **Libraries Used:** Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn, Imbalanced-learn

Feel free to explore, contribute, or reach out for discussions on improving healthcare AI solutions! 🚀

### Deployed on Streamlit Cloud [here](https://healthinsinght.streamlit.app/heart_stroke))
