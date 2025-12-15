import streamlit as st
import pickle
import numpy as np

# Load trained model
model = pickle.load(open("exam_result_mode.pkl", "rb"))

st.set_page_config(page_title="Exam Result Prediction", page_icon="📘")

st.title("📘 Exam Result Prediction")
st.write("Predict whether a student will **PASS or FAIL** using Random Forest")

st.markdown("---")

# Input fields
study_hours = st.number_input("📖 Study Hours per Day", min_value=0.0, max_value=15.0, step=0.5)
attendance = st.number_input("🏫 Attendance Percentage", min_value=0.0, max_value=100.0, step=1.0)
internal_marks = st.number_input("📝 Internal Marks", min_value=0.0, max_value=100.0, step=1.0)

# Predict button
if st.button("🔍 Predict Result"):
    input_data = np.array([[study_hours, attendance, internal_marks]])
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.success("🎉 Prediction: PASS")
    else:
        st.error("❌ Prediction: FAIL")

