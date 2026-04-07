#importing required libraries for model building
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import pickle

#create sample data for model training
Size = np.random.randint(100, 3000, 1000)
Bedrooms = np.random.randint(1, 10, 1000)
Age = np.random.randint(1, 10, 1000)
Locationscore = np.random.randint(1, 10, 1000)
Price = (Size * 50) + (Bedrooms * 10000) - (Age * 2000) + (Locationscore * 5000)
#convert sample data into dataframe
data = pd.DataFrame({
    "Size": Size,
    "Bedrooms": Bedrooms,
    "Age": Age,
    "Locationscore": Locationscore,
    "Price": Price
})
#separate input features and output feature to feed data for model
X = data[["Size", "Bedrooms", "Age", "Locationscore"]]
y = data["Price"]
#divide the data for training and testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)
#create the model and train
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
with open("RndmF.pkl", "wb") as f:
    pickle.dump(model, f)


print("Random Forest model trained and saved successfully!")