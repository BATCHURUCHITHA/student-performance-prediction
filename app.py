import streamlit as st
import pandas as pd
import pickle

# Load trained model
model = pickle.load(open("model.pkl", "rb"))

st.title("🎓 Student Performance Predictor")

st.write("Enter student details to predict the exam score.")

# Input fields
gender = st.selectbox("Gender", ["Male", "Female"])
study_hours = st.slider("Study Hours per Day", 0, 12, 5)
attendance = st.slider("Attendance (%)", 0, 100, 75)
previous_score = st.number_input("Previous Exam Score", 0, 100, 50)

# Convert categorical values
if gender == "Male":
    gender = 1
else:
    gender = 0

# Create dataframe
input_data = pd.DataFrame({
    "gender": [gender],
    "study_hours": [study_hours],
    "attendance": [attendance],
    "previous_score": [previous_score]
})

# Prediction
if st.button("Predict Performance"):
    prediction = model.predict(input_data)
    st.success(f"Predicted Score: {prediction[0]:.2f}")
