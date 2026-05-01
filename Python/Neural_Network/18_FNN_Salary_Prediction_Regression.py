# Employee Salary Prediction using Feedforward Neural Network

from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_absolute_error
import numpy as np

# ----------------------------------------------------
# Dataset
# [Experience, Education Score, Skill Rating, Certificates]
# ----------------------------------------------------
X = [
    [1,5,4,0],
    [2,6,5,1],
    [3,6,6,1],
    [4,7,7,2],
    [5,7,8,2],
    [6,8,8,3],
    [7,8,9,3],
    [8,9,9,4],
    [10,9,10,5],
    [9,9,10,4]
]

# Salary Output
y = [22000,26000,32000,40000,47000,
     54000,62000,70000,85000,78000]

# Convert y into 2D form for scaling
y = np.array(y).reshape(-1, 1)

# ----------------------------------------------------
# Split data
# ----------------------------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

# ----------------------------------------------------
# Scaling Input and Output
# ----------------------------------------------------
scaler_X = StandardScaler()
scaler_y = StandardScaler()

X_train_scaled = scaler_X.fit_transform(X_train)
X_test_scaled  = scaler_X.transform(X_test)

y_train_scaled = scaler_y.fit_transform(y_train).ravel()
y_test_scaled  = scaler_y.transform(y_test).ravel()

# ----------------------------------------------------
# Create FNN Model
# ----------------------------------------------------
model = MLPRegressor(
    hidden_layer_sizes=(6,),
    activation='relu',
    solver='lbfgs',        # better for very small dataset
    max_iter=5000,
    random_state=42
)

# ----------------------------------------------------
# Train Model
# ----------------------------------------------------
model.fit(X_train_scaled, y_train_scaled)

# ----------------------------------------------------
# Predict on test data
# ----------------------------------------------------
pred_scaled = model.predict(X_test_scaled)

# Convert predictions back to original salary range
predictions = scaler_y.inverse_transform(pred_scaled.reshape(-1, 1)).ravel()

print("Actual Salaries   :", y_test.ravel())
print("Predicted Salary  :", predictions.astype(int))

# Error
error = mean_absolute_error(y_test.ravel(), predictions)
print("\nAverage Error:", error)

# ----------------------------------------------------
# New Employee Prediction
# Experience = 5 years
# Education = 8
# Skill = 9
# Certifications = 3
# ----------------------------------------------------
new_emp = [[5,8,9,0]]
new_emp_scaled = scaler_X.transform(new_emp)

salary_scaled = model.predict(new_emp_scaled)
salary = scaler_y.inverse_transform(salary_scaled.reshape(-1, 1))

print("\nPredicted Salary for New Employee:", int(salary[0][0]))