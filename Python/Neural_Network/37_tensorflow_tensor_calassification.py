import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import numpy as np

print("----- Marvellous Binary Classification -----")

# Simple dataset
# Inputs: [Study Hours, Attendance]
X = np.array([
    [1, 30],
    [2, 40],
    [3, 50],
    [4, 60],
    [5, 70],
    [6, 80],
    [7, 90],
    [2, 35],
    [5, 75],
    [6, 85]
], dtype=float)

# Output: 0 = Fail, 1 = Pass
Y = np.array([0, 0, 0, 0, 1, 1, 1, 0, 1, 1], dtype=float)

# Create model
model = Sequential([
    Dense(8, activation='relu', input_shape=(2,)),
    Dense(4, activation='relu'),
    Dense(1, activation='sigmoid')
])

# Compile model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train model
model.fit(X, Y, epochs=200, verbose=0)

print("Training completed")

# Test sample
test_data = np.array([[5, 65]], dtype=float)
prediction = model.predict(test_data, verbose=0)

print("Predicted Probability:", prediction[0][0])

if prediction[0][0] > 0.5:
    print("Predicted Class: Pass")
else:
    print("Predicted Class: Fail")