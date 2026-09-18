import streamlit as st
import pandas as pd
import joblib
from sklearn.preprocessing import PolynomialFeatures

poly = joblib.load("poly.pkl")

model = joblib.load("model.pkl")
st.title("Electrical_Bill AC Price Prediction")

ac_units = st.number_input(
    "Enter AC Units : ",
    min_value=0.0,
    max_value=150.0,
    value=100.0
)
fan_units = st.number_input(
    "Enter AC Units : ",
    min_value=0.0,
    max_value=150.0,
    value=100.0
)


if st.button("Predict"):
  valid = True
  if ac_units< 0 or ac_units > 150:
    st.error("Ac Units should be between 0 and 150")
    valid = False
  if fan_units< 0 or fan_units > 150:
    st.error(" Fan Units should be between 0 and 150")
    valid = False
  if valid:
    input_data = pd.DataFrame({
            "AC_Units": [ac_units],
            "Fan_Units": [fan_units]
        })
    poly = PolynomialFeatures(degree=2)
    input_data_poly = poly.fit_transform(input_data)
    prediction = model.predict(input_data_poly)
    pred = prediction[0]
    st.success(f"Predicted Price: ₹{pred:.2f} Rs")
