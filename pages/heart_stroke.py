import joblib
import numpy as np
import pandas as pd
import streamlit as st
from config import doctor_search
# Function to load model and make predictions
def predict_health_status(age, hypertension, heart_disease, ever_married, work_type, avg_glucose_level, bmi, smoking_status):
    model = joblib.load(r'models\random_forest_pipeline.pkl')  # Load your saved Random Forest model pipeline
    
    # Prepare the input data as a DataFrame to match the model's expected format
    input_data = pd.DataFrame({
        'age': [age],
        'hypertension': [hypertension],
        'heart_disease': [heart_disease],
        'ever_married': [ever_married],
        'work_type': [work_type],
        'avg_glucose_level': [avg_glucose_level],
        'bmi': [bmi],
        'smoking_status': [smoking_status]
    })
    
    prediction = model.predict(input_data)
    return prediction

# Streamlit app
def health_app():
    st.set_page_config(
        page_title="Heart stroke - Risk Assessment",
        page_icon="🏥",
    )
    st.markdown(
        f"<h1 style='text-align: center; color: black;'>Heart stroke risk Prediction</h1>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "<h4 style='text-align: center; color: black;'>Enter patient details to assess heart risk</h4>",
        unsafe_allow_html=True,
    )

    # Input sliders and options for patient data
    age = st.slider("Age", min_value=1, max_value=100, value=45)
    hypertension = st.selectbox("Hypertension", options=[0, 1], format_func=lambda x: 'No' if x == 0 else 'Yes')
    heart_disease = st.selectbox("Heart Disease", options=[0, 1], format_func=lambda x: 'No' if x == 0 else 'Yes')
    ever_married = st.selectbox("Ever Married", options=['Yes', 'No'])
    work_type = st.selectbox("Work Type", options=['Private', 'Self-employed', 'Govt job', 'Children', 'Never worked'])
    avg_glucose_level = st.slider("Average Glucose Level", min_value=50.0, max_value=300.0, value=110.0)
    bmi = st.slider("BMI", min_value=10.0, max_value=100.0, value=25.0)
    smoking_status = st.selectbox("Smoking Status", options=['never smoked', 'formerly smoked', 'smokes'])

    result = None
    if st.button("Predict"):
        result = predict_health_status(
            age, hypertension, heart_disease, ever_married, work_type, avg_glucose_level, bmi, smoking_status
        )
        
        if result == 1:
            st.subheader("The patient is at high risk of health issues 😔")
            st.markdown("---")
            st.error(
                "Consult with one of the following specialists immediately"
            )
            pcp = doctor_search("Primary Care Provider")
            infec = doctor_search("Cardiologist")
            st.markdown(f"- [Primary Care Doctor]({pcp}) 👨‍⚕")
            st.markdown(f"- [Cardiologist]({infec}) 👨‍⚕")
            st.markdown("---")
        else:
            st.subheader("The patient appears to be at low risk 😄")

if __name__ == "__main__":
    health_app()
