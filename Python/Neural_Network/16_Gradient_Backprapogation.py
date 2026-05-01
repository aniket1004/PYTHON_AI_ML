import math

# ---------------------------------------------------------
# Marvellous ANN Example
# Demonstrates:
# 1. Forward propagation
# 2. Loss calculation
# 3. Backpropagation
# 4. Gradient descent weight update
# ---------------------------------------------------------

# Sigmoid activation function
def Marvellous_Sigmoid(value):
    return 1 / (1 + math.exp(-value))

# Derivative of sigmoid
# If output = sigmoid(z), then derivative = output * (1 - output)
def Marvellous_Sigmoid_Derivative(output):
    return output * (1 - output)

# ---------------------------------------------------------
# Input values (simple values)
# ---------------------------------------------------------
x1 = 1.0
x2 = 2.0

# Actual target output
target = 1.0

# ---------------------------------------------------------
# Initial weights and bias (simple values)
# ---------------------------------------------------------
w1 = 0.5
w2 = -0.3
b = 0.1

# Learning rate
learning_rate = 0.1

# Number of training iterations
epochs = 10

print("Initial Values")
print("w1 =", w1)
print("w2 =", w2)
print("b  =", b)
print("-" * 50)

# ---------------------------------------------------------
# Training loop
# ---------------------------------------------------------
for epoch in range(1, epochs + 1):

    # =========================
    # Step 1: Forward Propagation
    # =========================

    # Weighted sum
    z = (x1 * w1) + (x2 * w2) + b

    # Output after sigmoid activation
    output = Marvellous_Sigmoid(z)

    # =========================
    # Step 2: Loss Calculation
    # =========================

    # Using Mean Squared Error for one sample
    # Loss = 0.5 * (target - output)^2
    loss = 0.5 * (target - output) ** 2

    # =========================
    # Step 3: Backpropagation
    # =========================

    # Derivative of loss with respect to output
    # dL/doutput = output - target
    dL_doutput = output - target

    # Derivative of output with respect to z
    # doutput/dz = sigmoid'(z) = output * (1 - output)
    doutput_dz = Marvellous_Sigmoid_Derivative(output)

    # Chain rule:
    # dL/dz = dL/doutput * doutput/dz
    dL_dz = dL_doutput * doutput_dz

    # Gradients with respect to weights and bias
    # z = x1*w1 + x2*w2 + b
    # dz/dw1 = x1
    # dz/dw2 = x2
    # dz/db = 1
    dL_dw1 = dL_dz * x1
    dL_dw2 = dL_dz * x2
    dL_db = dL_dz

    # =========================
    # Step 4: Gradient Descent
    # =========================

    # Update weights and bias
    w1 = w1 - (learning_rate * dL_dw1)
    w2 = w2 - (learning_rate * dL_dw2)
    b = b - (learning_rate * dL_db)

    # =========================
    # Display all values
    # =========================
    print("Epoch:", epoch)
    print("Weighted Sum (z):", round(z, 4))
    print("Predicted Output :", round(output, 4))
    print("Target Output    :", target)
    print("Loss             :", round(loss, 6))
    print("Gradient dL/dw1  :", round(dL_dw1, 6))
    print("Gradient dL/dw2  :", round(dL_dw2, 6))
    print("Gradient dL/db   :", round(dL_db, 6))
    print("Updated w1       :", round(w1, 6))
    print("Updated w2       :", round(w2, 6))
    print("Updated b        :", round(b, 6))
    print("-" * 50)

print("Final Trained Values")
print("w1 =", round(w1, 6))
print("w2 =", round(w2, 6))
print("b  =", round(b, 6))