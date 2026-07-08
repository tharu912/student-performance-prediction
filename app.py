import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("student_performance_model.pkl")

st.title("🎓 Student Performance Prediction")
import pandas as pd

scores = pd.DataFrame({
    "Model": ["Linear Regression", "Decision Tree", "Random Forest"],
    "R2 Score": [0.652, 0.662, 0.797]
})

st.subheader("Model Comparison")
st.bar_chart(scores.set_index("Model"))
importance_df = pd.DataFrame({
    "Feature": [
        "Attendance",
        "Past Scores",
        "Study Hours",
        "Activities",
        "Parent Masters",
        "Parent PhD"
    ],
    "Importance": [
        0.351,
        0.344,
        0.218,
        0.017,
        0.016,
        0.014
    ]
})

st.subheader("Feature Importance")
st.bar_chart(importance_df.set_index("Feature"))
st.write("""
This application predicts a student's final exam score
based on study habits, attendance, previous academic
performance and other educational factors.
""")

study_hours = st.number_input("Study Hours Per Week", 0, 50, 20)
attendance = st.number_input("Attendance Rate", 0.0, 100.0, 75.0)
past_score = st.number_input("Past Exam Score", 0, 100, 60)

gender = st.selectbox("Gender", ["Male", "Female"])

parent_education = st.selectbox(
    "Parental Education Level",
    ["Bachelors", "High School", "Masters", "PhD"]
)

internet = st.selectbox(
    "Internet Access At Home",
    ["Yes", "No"]
)

activity = st.selectbox(
    "Extracurricular Activities",
    ["Yes", "No"]
)
if st.button("Predict"):

    input_data = pd.DataFrame({
        "Study_Hours_per_Week":[study_hours],
        "Attendance_Rate":[attendance],
        "Past_Exam_Scores":[past_score],
        "Gender_Male":[1 if gender=="Male" else 0],
        "Parental_Education_Level_High School":[1 if parent_education=="High School" else 0],
        "Parental_Education_Level_Masters":[1 if parent_education=="Masters" else 0],
        "Parental_Education_Level_PhD":[1 if parent_education=="PhD" else 0],
        "Internet_Access_at_Home_Yes":[1 if internet=="Yes" else 0],
        "Extracurricular_Activities_Yes":[1 if activity=="Yes" else 0]
    })

    prediction = model.predict(input_data)

    st.metric(
        label="Predicted Final Exam Score",
        value=f"{prediction[0]:.2f}"
    )