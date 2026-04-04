
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Load the dataset
data = pd.read_csv("data/Hospital_Staffing_dataset.csv")

# Check missing values BEFORE cleaning
print("\nMissing values per column:")
print(data.isnull().sum())

print("\nTotal missing values:")
print(data.isnull().sum().sum())

# Show the first five rows
print(data.head())

# SHow columns
print("\nColumns:")
print(data.columns)

# Show info
print("\nInfo:")
print(data.info())

#________
# 1. CLEAN DATA
# _______

# Drop Facility Number
data = data.drop(columns=["Facility Number"])

# Fill all missing values since ML can not handle missing values (Data Imputation)
data = data.fillna(0)

#_________
# 2. Convert Dates
#_________

# Convert date columns to datetime (ignore invalid values like 0)
data["Begin Date"] = pd.to_datetime(data["Begin Date"], errors='coerce')
data["End Date"] = pd.to_datetime(data["End Date"], errors='coerce')

# Create Duration column (difference in days)
data["Duration"] = (data["End Date"] - data["Begin Date"]).dt.days
# Fill missing duration values
data["Duration"] = data["Duration"].fillna(0)

# Drop Original Date Columns
data = data.drop(columns=["Begin Date", "End Date"])

#_________
# 3. Define Target and Features
#_________

# Target (predictions)
y = data["Productive Hours per Adjusted Patient Day"]

# Features
x = data.drop(columns=["Productive Hours per Adjusted Patient Day"])

#__________
# 4. Convert Categorical Data
#__________

# Convert text columns into numerical values
x = pd.get_dummies(x)

#____________
# 5. Split Data (Standard Default of Test Size 20%, Training Size 80%)
# Random State- A fixed random state used to ensure reproducibility of results.
#___________
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=3
)

#________
# 6. Train Model
#________

# Set n-estimators = 10 tp reduce the number of trees in Random Forest model to reduce computation time.
# model = RandomForestRegressor(random_state=3)
model = RandomForestRegressor(n_estimators=10, random_state=3)
model.fit(x_train, y_train)

#______
# Make Predictions
#______
predictions = model.predict(x_test)
print("\nSample Predictions: ")
print(predictions[:10])

#_______
#Model Evaluation
#__________
mse = mean_squared_error(y_test, predictions)
r2 = r2_score(y_test, predictions)
print("\nModel Evaluation: ", round(mse, 4))
print("MSE:", round(mse, 4))
print("R2:", round(mse, 4))
