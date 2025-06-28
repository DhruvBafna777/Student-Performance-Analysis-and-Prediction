import streamlit as st
import numpy as np
import pickle
import pandas as pd

model = pickle.load(open('student_model.pkl',"rb"))

st.set_page_config(page_title="Student Score Predictor", page_icon="🎓")
st.title("🎓 Student Final Grade Predictor")
st.markdown("Made with ❤️ by Dhruv Bafna")
st.markdown("Enter the student's details below to predict their final exam score (G3).")

G1 = st.slider("📘 G1 Score (First Term)",0,20,10)
G2 = st.slider("📘 G2 Score (Second Term)",0,20,10)
studytime = st.selectbox("⏳ Study Time Level",[1,2,3,4])
failures = st.selectbox("❌ Past Class Failures", [0, 1, 2, 3])
absences = st.slider("🚫 Total Absences", 0, 50, 5)

if st.button("🎯 Predict Final Grade (G3)"):
    features = np.array([[G1,G2,studytime,failures,absences]])
    prediction = model.predict(features)[0]
    st.success(f"Predicted Final Grade : {round(prediction,2)} / 20")
    
    if prediction  < 10:
        st.warning("⚠️ Student may need extra support or coaching.")
    elif prediction >= 10:
        st.success("Good! The student is performing Average.")
    else:
        st.balloons()
        st.info("🎉 Excellent! The student is performing very well.")
        
        
        
st.title("Upload a CSV File")
file_upload = st.file_uploader("Upload a CSV file with columns: G1, G2, studytime, failures, absences")

if file_upload is not None:
    try:
        new_data = pd.read_csv(file_upload,sep=";")
        required_col = ["G1","G2","studytime","failures","absences"]
        
        if all(col in new_data.columns for col in required_col):
            predictions = model.predict(new_data[required_col])
            new_data["Predicted_G3"] = predictions
            st.success("Predictions Completed ✅") 
            
            st.write("Prediction Result")
            st.dataframe(new_data)
            
            csv = new_data.to_csv(index=False).encode('utf-8')
            st.download_button("⬇️ Download Results", csv, "predicted_students.csv", "text/csv")
        else:
            st.warning(f"❗ CSV must contain columns: {required_col}")
            
    except Exception as e:
        st.error(f"Error: {e}")
        
