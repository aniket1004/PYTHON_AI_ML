from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_absolute_error

#--------------------------------------------------------------
# Dataset
# [Experience, Education Score, Skill Rating, Certificates]
#--------------------------------------------------------------

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
y = [22000,26000, 32000,40000,47000, 54000,62000,70000,85000,78000]

#--------------------------------------------------------------
# Split data
#--------------------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

#--------------------------------------------------------------
# Scaling
#--------------------------------------------------------------

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

#--------------------------------------------------------------
# Create FNN Model
#--------------------------------------------------------------

model = MLPRegressor(
    hidden_layer_sizes=(6,),
    activation='relu',
    solver='adam',
    max_iter=2000,
    random_state=42
)

#--------------------------------------------------------------
# Train Model
#--------------------------------------------------------------

model.fit(X_train, y_train)


#--------------------------------------------------------------
# Predict
#--------------------------------------------------------------

predictions = model.predict(X_test)

print("Actual Salaries :", y_test)
print("Predicted Salaries :", predictions)

# Error
error = mean_absolute_error(y_test, predictions)
print("\nAverage Error :", error)


#--------------------------------------------------------------
# New Employee Prediction
# Experience = 5 years
# Education = 8
# Skills = 9
# Certifications = 3
#--------------------------------------------------------------

new_emp = [[5,8,9,3]]
new_emp_scaled = scaler.transform(new_emp)

salary = model.predict(new_emp_scaled)

print("\n Predicted Salary for New Employee :", int(salary[0]))