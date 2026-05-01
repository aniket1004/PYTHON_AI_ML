# ---------------------------------------------------------
# Program : Sigmoid vs ReLU Neuron Comparison
# Author  : Piyush Manohar Khairnar
# ---------------------------------------------------------

import math
import matplotlib.pyplot as plt
import numpy as np

# ---------------------------------------------------------
# STEP 1 : Activation Functions
# ---------------------------------------------------------

def sigmoid(z):
    """
    Sigmoid Activation Function
    Output range : (0, 1)
    Used for probability-based outputs
    """
    return 1 / (1 + math.exp(-z))

def relu(z):
    """
    ReLU Activation Function
    Output : max(0, z)
    Used in hidden layers of deep networks
    """
    return max(0, z)

# ---------------------------------------------------------
# STEP 2 : Neuron Forward Pass
# ---------------------------------------------------------
# Generic neuron → works with any activation function

def Marvellous_neuron_forward(inputs, weights, bias, activation_func):

    print("\n----- NEURON CALCULATION START -----\n")

    # Display input details
    print("Inputs (x)   :", inputs)
    print("Weights (w)  :", weights)
    print("Bias (b)     :", bias)

    # -----------------------------------------------------
    # Weighted Sum Calculation
    # z = w·x + b
    # -----------------------------------------------------
    z = sum(w * x for w, x in zip(weights, inputs)) + bias

    print("\nStep 1 : Weighted Sum")
    print("z =", z)

    # -----------------------------------------------------
    # Activation Function
    # -----------------------------------------------------
    y_hat = activation_func(z)

    print("\nStep 2 : Activation Function Applied")
    print("Activation Function :", activation_func.__name__)
    print("Output (ŷ) :", y_hat)

    print("\n----- NEURON CALCULATION END -----\n")

    return z, y_hat


# ---------------------------------------------------------
# STEP 3 : Plot Sigmoid vs ReLU
# ---------------------------------------------------------

def plot_sigmoid_relu():

    z_values = np.linspace(-10, 10, 200)

    # Vectorized versions
    sigmoid_values = 1 / (1 + np.exp(-z_values))
    relu_values = np.maximum(0, z_values)

    plt.figure(figsize=(8, 5))

    # Plot both functions
    plt.plot(z_values, sigmoid_values, label="Sigmoid", linewidth=2)
    plt.plot(z_values, relu_values, label="ReLU", linewidth=2)

    # Reference lines
    plt.axhline(y=0, linewidth=0.5)
    plt.axhline(y=1, linewidth=0.5)
    plt.axvline(x=0, linestyle="--")

    # Labels
    plt.title("Sigmoid vs ReLU Activation Functions", fontsize=16)
    plt.xlabel("Input (z)", fontsize=14)
    plt.ylabel("Output", fontsize=14)

    plt.grid(True, linestyle="--", alpha=0.6)
    plt.legend()

    plt.show()


# ---------------------------------------------------------
# STEP 4 : Main function
# ---------------------------------------------------------

def main():

    print("\n========= ACTIVATION FUNCTION COMPARISON =========\n")

    # Example data
    inputs = [1.0, 2.0, 3.0]
    weights = [0.6, 0.4, -0.2]
    bias = 0.5

    # Sigmoid neuron
    print("=== Sigmoid Neuron ===")
    Marvellous_neuron_forward(inputs, weights, bias, sigmoid)

    # ReLU neuron
    print("=== ReLU Neuron ===")
    Marvellous_neuron_forward(inputs, weights, bias, relu)

    # Plot comparison
    plot_sigmoid_relu()


if __name__ == "__main__":
    main()