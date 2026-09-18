import streamlit as st
import pandas as pd
import joblib

model = joblib.load("model.pkl")
st.title("Electrical_Bill AC Price Prediction")

units = st.number_input(
    "Enter AC Units : ",
    min_value=0.0,
    max_value=10000.0,
    value=100.0
)


if st.button("Predict"):
        input_data = pd.DataFrame({
            "AC_Units": [units],
        })
        prediction = model.predict(input_data)
        pred = prediction[0]
        st.success(f"Predicted Price: ₹{pred:.2f} Rs")
