import streamlit as st
import pickle
import numpy as np

# Load trained model
model = load("results.csv)

st.set_page_config(page_title="Exam Result Prediction", page_icon="📘")

st.title("📘 Exam Result Prediction")
st.write("Predict whether a student will **PASS or FAIL**")

st.markdown("---")

# Input fields
hindi = st.number_input("📖 Hindi Marks", min_value=0.0, max_value=100.0, step=1.0)
english = st.number_input("📖 English Marks", min_value=0.0, max_value=100.0, step=1.0)
maths = st.number_input("📖 Maths Marks", min_value=0.0, max_value=100.0, step=1.0)
history = st.number_input("📖 History Marks", min_value=0.0, max_value=100.0, step=1.0)

# Predict button
if st.button("🔍 Predict Result"):
    input_data = np.array([[hindi, english, maths, history]])
    prediction = model.predict(input_data)

    if prediction[0] == 1 or prediction[0] == "Pass":
        st.success("🎉 Prediction: PASS")
    else:
        st.error("❌ Prediction: FAIL")

