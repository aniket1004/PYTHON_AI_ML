# Student Pass/Fail Prediction using Feedforward Neural Network

from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import StandardScaler

# ------------------------------------------------------------
# Step 1: Prepare the dataset
# [Study Hours, Attendance, Assignment Score]
# Output: 0 = Fail, 1 = Pass
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
# Step 2: Split dataset
# stratify=y keeps class ratio balanced
# ------------------------------------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)

# ------------------------------------------------------------
# Step 3: Scale the input data
# ------------------------------------------------------------
scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# ------------------------------------------------------------
# Step 4: Create FNN model
# lbfgs often works better for very small datasets
# ------------------------------------------------------------
model = MLPClassifier(
    hidden_layer_sizes=(5,),
    activation='relu',
    solver='lbfgs',
    max_iter=2000,
    random_state=42
)

# ------------------------------------------------------------
# Step 5: Train the model
# ------------------------------------------------------------
model.fit(X_train_scaled, y_train)

# ------------------------------------------------------------
# Step 6: Predict
# ------------------------------------------------------------
y_pred = model.predict(X_test_scaled)

# ------------------------------------------------------------
# Step 7: Evaluate
# ------------------------------------------------------------
print("Actual Output   :", y_test)
print("Predicted Output:", y_pred.tolist())

accuracy = accuracy_score(y_test, y_pred)
print("\nAccuracy of model:", accuracy)

print("\nClassification Report:")
print(classification_report(y_test, y_pred, zero_division=0))

# ------------------------------------------------------------
# Step 8: Predict new student
# ------------------------------------------------------------
new_student = [[5, 75, 60]]
new_student_scaled = scaler.transform(new_student)

prediction = model.predict(new_student_scaled)

if prediction[0] == 1:
    print("\nNew Student Prediction: PASS")
else:
    print("\nNew Student Prediction: FAIL")