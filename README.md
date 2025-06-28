# 🎓 Student Final Grade Predictor

This project is a **Machine Learning + Streamlit dashboard** that helps educational institutions predict a student's final grade (G3) based on behavior, study patterns, and past performance.

---

## 🚀 Features

- 🎯 Predict a student's final grade using:
  - G1 (1st term score)
  - G2 (2nd term score)
  - Study time
  - Failures
  - Absences


- 📥 Upload a CSV file to predict for an entire classroom
- 📈 Business insight: Identify weak students for early intervention
- 🧠 Powered by RandomForest Regressor (R² Score = 0.87)
- 🖥️ Built using Python, pandas, scikit-learn, and Streamlit

---

## 📌 Use-Case (Business Impact)

> This tool allows school/college administrators and teachers to:
- Proactively identify students at risk of failure
- Provide personalized coaching or interventions
- Improve pass rate and academic outcomes
- Help parents stay informed about performance

---

## 🧪 How to Use

### 🔹 Single Student Prediction
1. Enter 5 inputs via UI sliders (G1, G2, studytime, failures, absences)
2. Click on "🎯 Predict Final Grade"
3. Get prediction and guidance instantly

### 🔹 Bulk CSV Prediction
1. Prepare a CSV with 5 columns: G1, G2, studytime, failures , absences
2. Upload in the app
3. Get predictions + download results

📝 Sample CSV:
```csv
G1,G2,studytime,failures,absences
15,14,2,0,4
12,10,3,1,0
