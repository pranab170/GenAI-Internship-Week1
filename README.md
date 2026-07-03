# AI-Powered Student Performance Prediction System

## 1. Project Overview
This project is developed as part of the **Gen AI & ML Internship (Week 1)**. The primary objective is to build an end-to-end Machine Learning pipeline that predicts whether a student will pass or fail their exams based on their socioeconomic and academic background.

## 2. Dataset Information
- **Source:** Kaggle "Students Performance in Exams" dataset.
- **Data Description:** The dataset contains information about students including:
    - Gender, Race/Ethnicity, Parental Level of Education, Lunch type, and Test Preparation Course.
    - Scores for Math, Reading, and Writing.
- **Target Variable:** `target_pass` (Binary classification: `1` for Pass, `0` for Fail).
  - *Definition:* A student is considered "Pass" if their average score across all subjects is ≥ 60.

## 3. Exploratory Data Analysis (EDA)
To understand the underlying patterns in the data, we performed the following:
- **Statistical Summary:** Used `.describe()` to identify mean, median, and spread of scores.
- **Visualizations:**
    - **Histograms:** To visualize the distribution density of Math, Reading, and Writing scores.
    - **Box Plots:** To identify potential outliers in student performance.
    - **Correlation Heatmap:** To visualize relationships between numerical features and identify collinearity.

## 4. Preprocessing Pipeline
- **Cleaning:** Dropped target-leaking columns (original score columns) to ensure model generalization.
- **Encoding:** Used One-Hot Encoding (`pd.get_dummies`) to convert categorical variables into numerical format.
- **Scaling:** Applied `StandardScaler` to normalize feature values, ensuring stable model training.

## 5. Modeling & Evaluation
Two models were implemented and rigorously evaluated:
1. **Logistic Regression** (Baseline model)
2. **Random Forest Classifier** (Ensemble method)

**Evaluation Metrics:**
- **Accuracy Score:** Overall prediction success.
- **Classification Report:** Detailed view of Precision, Recall, and F1-Score for both 'Pass' and 'Fail' classes.
- **Confusion Matrix:** Heatmaps were plotted to visualize True Positives, True Negatives, False Positives, and False Negatives.

## 6. How to Run
1. **Install Dependencies:**
   ```bash
   pip install pandas numpy scikit-learn matplotlib seaborn
   ```
1. **Execute:**
    - Ensure the `students.csv` file is in the root directory.
    - Open `mini_project.ipynb` in VS Code.
    - Click "Run All" to execute the pipeline and generate results.

## 7. Results Summary
The Random Forest classifier provided a more robust evaluation on the test set, effectively distinguishing between students at-risk of failing and those likely to pass based on the provided features.
