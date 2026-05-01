# Student Pass/Fail Prediction using Feedforward Neural Network

# Import required libraries
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, classification_report

# ------------------------------------------------------------
# Step 1: Prepare the dataset
# Each row contains:
# [Study Hours, Attendance, Assignment Score]
# Output:
# 0 = Fail
# 1 = Pass
# ------------------------------------------------------------

X = [
    [1, 40, 30],
    [2, 50, 35],
    [3, 60, 40],
    [4, 65, 50],
    [5, 70, 55],
    [6, 75, 65],
    [7, 80, 70],
    [2, 45, 25],
    [8, 90, 85],
    [1, 35, 20],
    [3, 55, 45],
    [4, 68, 52],
    [5, 72, 58],
    [6, 78, 62],
    [7, 85, 75]
]

y = [0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1]

# ------------------------------------------------------------
# Step 2: Split dataset into training and testing data
# Training data is used to teach the model
# Testing data is used to check performance
# ------------------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# ------------------------------------------------------------
# Step 3: Create the Feedforward Neural Network model
# hidden_layer_sizes=(5,) means 1 hidden layer with 5 neurons
# activation='relu' is used in hidden layer
# max_iter=1000 means training runs up to 1000 times if needed
# ------------------------------------------------------------

model = MLPClassifier(
    hidden_layer_sizes=(5,),
    activation='relu',
    solver='adam',
    max_iter=1000,
    random_state=42
)

# ------------------------------------------------------------
# Step 4: Train the model
# The model learns patterns from training data
# ------------------------------------------------------------

model.fit(X_train, y_train)

# ------------------------------------------------------------
# Step 5: Predict using test data
# ------------------------------------------------------------

y_pred = model.predict(X_test)

# ------------------------------------------------------------
# Step 6: Check model accuracy
# ------------------------------------------------------------

print("Actual Output   :", y_test)
print("Predicted Output:", y_pred.tolist())

accuracy = accuracy_score(y_test, y_pred)
print("\nAccuracy of model:", accuracy)

# Detailed report
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# ------------------------------------------------------------
# Step 7: Test with new student data
# Example:
# Study Hours = 5
# Attendance = 75
# Assignment Score = 60
# ------------------------------------------------------------

new_student = [[5, 75, 60]]
prediction = model.predict(new_student)

if prediction[0] == 1:
    print("\nNew Student Prediction: PASS")
else:
    print("\nNew Student Prediction: FAIL")