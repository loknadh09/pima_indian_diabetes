
import streamlit as st
import joblib
import numpy as np

st.title("🩺 PIMA Diabetes Predictor")
model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")

inputs = {
    feat: st.sidebar.number_input(feat, value=0.0)
    for feat in ["Pregnancies", "Glucose", "BloodPressure",
                 "SkinThickness", "Insulin", "BMI",
                 "DiabetesPedigreeFunction", "Age"]
}

if st.button("Predict"):
    X = np.array([list(inputs.values())])
    X_scaled = scaler.transform(X)
    prob = model.predict_proba(X_scaled)[0, 1]
    st.metric("Probability of Diabetes", f"{prob:.2%}")
    st.success("**Diabetic**" if prob > 0.5 else "**Not Diabetic**")
