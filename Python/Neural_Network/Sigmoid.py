#------------------------------------------------------------
# Program : Aritificial Neural with Sigmoid Function
#------------------------------------------------------------

import math
import matplotlib.pyplot as plt
import numpy as np

#------------------------------------------------------------
# Step 1 : Sigmoid Activation Function
#------------------------------------------------------------
# Sigmoid converts input into range(0, 1)
# Used for probability-based outputs

def sigmoid(z):
    """
    Sigmoid Function
    Formula = 1 / (1+ e ^ (-z))
    """
    return 1 / (1 + math.exp(-z))

#------------------------------------------------------------
# Step 2 : Neuron Forward Pass
#------------------------------------------------------------
# Performs :
# 1. Weighted sum
# 2. Add bias
# 3. Apply sigmoid activation
def Marvellous_neuron_forward(inputs, weights, bias):
    print("\n---------- NEURON CALCULATION START ----------\n")

    # Display inputs
    print("Inputs (x) : ", inputs)
    print("Weights (w) : ", weights)
    print("Bias (b) : ", bias)
    #------------------------------------------------------------
    # Weighted Sum Calculation
    # z = w.x + b
    #------------------------------------------------------------

    z = sum(w * x for w, x in zip(weights, inputs)) + bias

    print("\n Step 1 : Weighted Sum")
    print("z = ", z)

    #------------------------------------------------------------
    # Apply Sigmoid Function
    #------------------------------------------------------------
    y_hat = sigmoid(z)

    print("\n Step 2 : Activation Function")
    print("Activation Function : Sigmoid")
    print("Output (y) = ", y_hat)

    print("\n---------- NEURON CALCULATION END ----------\n")

    return z, y_hat

#------------------------------------------------------------
# Step 3 : Plot Sigmoid Function
#------------------------------------------------------------
def plot_sigmoid():
    # Generate input range
    z_values = np.linspace(-10, 10, 200)

    # Apply sigmoid on range
    sigmoid_values = 1 / (1 + np.exp(-z_values))

    # Plot graph
    plt.figure(figsize=(8, 5))
    plt.plot(z_values, sigmoid_values, label="Sigmoid Function", linewidth=2, color="blue")

    # Reference lines
    plt.axhline(y=0, color="black", linewidth=0.5)
    plt.axhline(y = 1, color="black", linewidth=0.5)
    plt.axvline(x = 0, color="gray", linestyle="--")

    # Labels and title

    plt.title("Sigmoid Activation Function", fontsize=16)
    plt.xlabel("Input (z)", fontsize=14)
    plt.ylabel("Output (Probability)", fontsize=14)

    # Grid and legend
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.legend()

    plt.show()

#------------------------------------------------------------
# Step 4 : Main Function
#------------------------------------------------------------
def main():
    print("\n========== MARVELLOUS SIGMOID NEURON ==========\n")

    #Example Inputs
    inputs = [1.0, 2.0, 3.0]

    # Weights
    weights = [0.6, 0.4, -0.2]

    # Bias
    bias = 0.5

    # Forward pass
    z, y_hat = Marvellous_neuron_forward(inputs, weights, bias)

    print("Final z : ", z)
    print("Final y_hat : ", y_hat)

    # Plot graph
    plot_sigmoid()

#------------------------------------------------------------
# Entry Point
#------------------------------------------------------------

if __name__ == "__main__":
    main()