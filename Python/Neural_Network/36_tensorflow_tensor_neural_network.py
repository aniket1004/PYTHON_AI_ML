import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import numpy as np

print("----- Marvellous Neural Network -----")

# Sample input and output
X = np.array([[1], [2], [3], [4], [5]], dtype=float)
Y = np.array([[2], [4], [6], [8], [10]], dtype=float)

# Create model
model = Sequential()

# Add one hidden layer with 4 neurons
model.add(Dense(4, activation='relu', input_shape=(1,)))

# Add output layer
model.add(Dense(1))

# Compile model
model.compile(optimizer='adam', loss='mse')

# Train model
model.fit(X, Y, epochs=200, verbose=0)

print("Training completed")

# Test prediction
test_value = np.array([[6]], dtype=float)
prediction = model.predict(test_value, verbose=0)

print(f"Prediction for input 6: {prediction[0][0]:.4f}")