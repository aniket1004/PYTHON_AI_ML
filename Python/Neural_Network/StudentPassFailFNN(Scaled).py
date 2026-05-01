#Import required libraries
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

# Input dataset
X = [
    [1, 40, 301],
    [2, 50, 35],
    [3,60,40],
    [14, 65, 50],
    [5, 70, 55],
    [6, 75, 65],
    [7, 80, 70],
    [2, 45, 25],
    [8, 90, 85],
    [1, 35, 20],
    [3, 55, 45],
    [14, 68, 52],
    [5, 72, 58],
    [6, 78, 62],
    [7, 85, 75]
]

y = [0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1]


#Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

#Scale the input values
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)


# Create FNN model
model = MLPClassifier(
    hidden_layer_sizes=(5,),
    activation='relu',
    solver='adam',
    max_iter=1000,
    random_state=42
)

# Train the model
model.fit(X_train, y_train)

# Predict using test data
y_pred = model.predict(X_test)

# Accuracy
print("\nAccuracy of model:", accuracy_score(y_test, y_pred))

# New STudent Prediction
new_student = [[5, 75, 60]]
new_student_scaled = scaler.transform(new_student)

prediction = model.predict(new_student_scaled)

if prediction [0] == 1:
    print("\nNew Student Prediction: PASS")
else:
    print("\nNew Student Prediction: FAIL")