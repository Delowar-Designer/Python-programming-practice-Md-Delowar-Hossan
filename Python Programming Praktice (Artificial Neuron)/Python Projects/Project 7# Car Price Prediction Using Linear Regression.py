import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Dataset import section
dataset = pd.read_csv('CarPrice_Assignment.csv')

# Encoding categorical variables
categorical_cols = ['CarName', 'fuelsystem', 'cylindernumber', 'enginetype', 
                    'enginelocation', 'drivewheel', 'carbody', 'doornumber', 
                    'aspiration', 'fueltype']
encoder = LabelEncoder()
for col in categorical_cols:
    dataset[col] = encoder.fit_transform(dataset[col])

# Splitting dataset into train set and test set
x = dataset.drop(columns=['price'])
y = dataset['price']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=7)

# Feature scaling
scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(x_train)
x_test_scaled = scaler.transform(x_test)

# Model fitting
regressor = LinearRegression()
regressor.fit(x_train_scaled, y_train)

# Model evaluation
y_train_pred = regressor.predict(x_train_scaled)
y_test_pred = regressor.predict(x_test_scaled)

train_mse = mean_squared_error(y_train, y_train_pred)
test_mse = mean_squared_error(y_test, y_test_pred)
train_r2 = r2_score(y_train, y_train_pred)
test_r2 = r2_score(y_test, y_test_pred)

print("Train MSE:", train_mse)
print("Test MSE:", test_mse)
print("Train R^2 Score:", train_r2)
print("Test R^2 Score:", test_r2)
