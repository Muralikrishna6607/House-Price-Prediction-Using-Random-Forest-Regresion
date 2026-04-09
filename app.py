import streamlit as st
import pandas as pd
import pickle

# Load trained model
with open("RndmF.pkl", "rb") as f:
    model = pickle.load(f)
with open("test_data.pkl", "rb") as f: 
    X_test, y_test = pickle.load(f)
# App title
st.title("House Price Prediction")
st.info("Predicting based on Size (sqft), Bedrooms, Age, Location Score")

# form input
with st.form("price_prediction_form"):
    sqft = st.number_input("Enter Size (sqft):", min_value=0, step=10)
    bedrooms = st.number_input("Enter Number of Bedrooms:", min_value=0, step=1)
    age = st.number_input("Enter Age of the House:", min_value=0, step=1)
    location_score = st.number_input("Enter Location Score:", min_value=0, step=1)

    btn = st.form_submit_button("Predict")

# Prediction
if btn:
    #  Column names match training data
    new_data = pd.DataFrame(
        [[sqft, bedrooms, age, location_score]],
        columns=["Size", "Bedrooms", "Age", "Locationscore"]
    )

    prediction = model.predict(new_data)

    st.success(f"Predicted House Price: {round(prediction[0], 2)}")
