**House Price Prediction using Random Forest & Streamlit**

**Project Overview**

This project demonstrates a **House Price Prediction system** built
using **Machine Learning (Random Forest Regressor)** and deployed with a
**Streamlit web application**.

The model predicts house prices based on:

-   Size (in square feet)

-   Number of bedrooms

-   Age of the house

-   Location score

**Features**

-   Train a Random Forest Regression model using synthetic data

-   Save and load the trained model using pickle

-   Interactive UI built with Streamlit

-   Real-time house price prediction

**Tech Stack**

-   Python

-   Pandas

-   NumPy

-   Scikit-learn

-   Streamlit

-   Pickle

**Project Structure**

├── model.py \# Model training script

├── app.py \# Streamlit web app

├── RndmF.pkl \# Saved trained model

├── README.md \# Project documentation

**Model Training**

The model is trained using randomly generated sample data:

**Formula Used:**

Price = (Size \* 50) + (Bedrooms \* 10000) - (Age \* 2000) +
(Locationscore \* 5000)

**Explanation:**

-   Larger houses → higher price

-   More bedrooms → increases price significantly

-   Older houses → decrease in price

-   Better location → increases price

**Algorithm Used**

**Random Forest Regressor**

-   Ensemble learning method

-   Uses multiple decision trees

-   Provides better accuracy and avoids overfitting

**How to Run the Project**

**1. Clone the repository**

git clone https://github.com/Muralikrishna6607/House-Price-Prediction-Using-Random-Forest-Regresion.git

cd house-price-prediction

**2. Install dependencies**

pip install pandas numpy scikit-learn streamlit

**3. Train the model**

python model.py

**4. Run the Streamlit app**

streamlit run app.py

**Input Parameters**

  -----------------------------------------------------------------------
  **Feature**                  **Description**
  ---------------------------- ------------------------------------------
  Size                         Area in square feet

  Bedrooms                     Number of bedrooms

  Age                          Age of the house (years)

  Location Score               Rating of the location
  -----------------------------------------------------------------------

**Output**

-   Predicted house price based on given inputs

**Example**

**Input:**

-   Size = 2000

-   Bedrooms = 3

-   Age = 5

-   Location Score = 7

**Output:**

-   Predicted Price ≈ ₹ (calculated value)

**Note**

-   This project uses **synthetic data**, not real-world housing data

-   Predictions are for learning/demo purposes only

**Future Improvements**

-   Use real housing datasets

-   Add model evaluation metrics (R², MAE, RMSE)

-   Improve UI design

-   Deploy on cloud (AWS / Streamlit Cloud)

**Author**

K.Murali Krishna
