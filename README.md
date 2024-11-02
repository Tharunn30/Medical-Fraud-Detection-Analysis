Medical Fraud Detection Analysis

## 1. Problem Overview  
Healthcare fraud is a significant issue in the United States, costing tens of billions of dollars annually. As the FBI highlights, this crime isn’t harmless—it increases insurance premiums, exposes patients to unnecessary treatments, and raises taxes. In this project, the goal is to predict potentially fraudulent healthcare providers based on their claim patterns. The dataset used for analysis is available on [Kaggle](https://www.kaggle.com/datasets/rohitrox/healthcare-provider-fraud-detection-analysis/data), containing detailed claim and beneficiary information for several providers.

---

## 2. Exploratory Data Analysis (EDA)  
The data is heavily **imbalanced**, with only 506 out of 5410 providers labeled as potentially fraudulent, a ratio of 9:1. 

- **Beneficiary Information:**  
  - Most beneficiaries had continuous 12-month coverage.  
  - A significant proportion had chronic conditions.

- **Claims Data:**  
  - Procedure and diagnosis codes were analyzed for both inpatient and outpatient claims.  
  - The **top 100 most frequent diagnosis codes** were identified as important features.  
  - Below is a word cloud visualizing outpatient diagnosis codes:

  <img title="Outpatient Diagnosis Codes" alt="Alt text" src="/images/ClaimsDiagnosisOutpatient.png" width="100%">

- **Hospital Stay Analysis:**  
  - Length of hospital stay could be an essential feature in identifying fraudulent providers. The graph below shows the distribution of hospital stay durations for inpatient claims:

  <img title="Days in Hospital" alt="Alt text" src="/images/DaysInHospital.png" width="100%">

---

## 3. Data Preparation and Cleaning  
Since the dataset contains categorical variables, these were converted from strings into categorical values. Patient condition data was transformed into **Boolean features** to facilitate machine learning algorithms. 

Key steps in data preparation:  
- Extracted the **top 100 diagnosis and procedure codes** for inpatient and outpatient claims.  
- Joined the **beneficiary and claims data** to generate aggregated data at the **provider level**.  
- Grouped the data by providers to derive meaningful features for classification.

---

## 4. Modeling and Hyperparameter Optimization  
The dataset was split into **training and test sets**, and the following machine learning models were applied:  
1. Linear Support Vector Machine (SVM)  
2. Logistic Regression  
3. Random Forest  
4. XGBoost  
5. CatBoost  
6. K-Nearest Neighbors (KNN)  

To fine-tune these models, **grid search** or **randomized search** with cross-validation was used. The final model with the optimal hyperparameters was saved for further evaluation.

---

## 5. Model Evaluation  
The performance of each model was evaluated on the test set using metrics like **accuracy, precision, recall, F1-score**, and **AUC (Area Under the Curve)** for the ROC curve. Both **ROC** and **Precision-Recall** curves for all classifiers are shown below:  

<img title="ROC Curves" alt="ROC" src="/images/ROCCurve.png" width="100%">  
<img title="Precision-Recall Curves" alt="PR" src="/images/PRCurve.png" width="100%">

### Model Performance Summary:  

|           Model        | F1 Score | Precision |  Recall  | Accuracy |    AUC   |
|------------------------|----------|-----------|----------|----------|----------|
| Linear SVM             | 0.564885 | 0.860465  | 0.420455 | 0.943170 | 0.875534 |
| Logistic Regression    | 0.438889 | 0.290441  | 0.897727 | 0.798604 | 0.913736 |
| Random Forest          | 0.577778 | 0.829787  | 0.443182 | 0.943170 | 0.960463 |
| XGBoost                | 0.597403 | 0.696970  | 0.522727 | 0.938185 | 0.952931 |
| **CatBoost**           | **0.697368** | **0.828125** | **0.602273** | **0.954138** | **0.958594** |
| K-Nearest Neighbors    | 0.560000 | 0.945946  | 0.397727 | 0.945165 | 0.951465 |

Based on these metrics, **CatBoost** achieved the best balance between precision and recall, making it the ideal model for deployment.

---

## 6. Deployment  
The CatBoost model initially utilized hundreds of features. However, for deployment, a simpler version using only the **top 5 most important features** was created. The **feature importance scores** are shown in the following plot:

<img title="Feature Importance" alt="Feature Importance" src="/images/FeatureImportance.png" width="100%">

### Top 5 Features  
The distributions of the top 5 features are shown below:

<img title="Top 5 Features" alt="Top 5" src="/images/Top5Features.png" width="100%">

A new CatBoost model was trained using only these five features to reduce complexity. The ROC and Precision-Recall curves for this optimized model are displayed below:

<img title="Optimized CatBoost Curves" alt="Optimized Curves" src="/images/CatBoost5.png" width="100%">

### Streamlit App  
The simplified CatBoost model has been deployed as a **Streamlit web application**. Users can input provider features and receive predictions on whether a provider is likely fraudulent. Below is a screenshot of the application:

[<img title="App GUI" alt="App GUI" src="/images/AppGUI.png" width="100%">]

Try the app here: [Provider Fraud Detection App](https://medical-fraud-detection-analysis-pradlanka.streamlit.app).

---

## Summary  
This project successfully identifies potentially fraudulent providers using claims data and employs various machine learning models to optimize predictions. **CatBoost** emerged as the most effective model, and a simpler version using only five key features has been deployed to **Streamlit** for public use.

---

