#-----------------------------------------
# Program : Artifical Neural with ReLU Activation
#-----------------------------------------

import matplotlib.pyplot as plt
import numpy as np

#-----------------------------------------
# Step 1 : Activation Function (ReLU)
#-----------------------------------------
# ReLU = max(0, z)
# If z is positive -> output z
# if z is negative -> output 0

def relu(z):
    return max(0, z)

#-----------------------------------------
# Step 2 : Neuron Forward Pass Function
#-----------------------------------------
# This function simulates a single artificial neuron
# It performs :
# 1. Input X Weights multiplication
# 2. Summation + Bias
# 3. Activation (ReLU)

def Marvellous_neuron_forward(inputs, weights, bias):
    print("\n-------- NEURON CALCULATION START --------\n")

    # Display input and weights
    print("Inputs (x) : ", inputs)
    print("Weights (w): ", weights)
    print("Bias (b) :", bias)

    #-----------------------------------------
    # Step 2.1 : Weighted Sum Calculation
    # Formula : z = (x1 * w1 + x2 * w2 + x3 * w3) + bias
    #-----------------------------------------

    z = sum(w * x for w, x in zip(weights, inputs)) + bias

    print("\nStep 1 : Weighted Sum Calculation")
    print("z = w.x + b =", z)

    #-----------------------------------------
    # Step 2.2 : Activation Function
    #-----------------------------------------

    y_hat = relu(z)

    print("\nStep 2 : Activation Function Applied")
    print("Activation Function : ReLU")
    print("Output (y) = ", y_hat)

    print("\n-------- NEURON CALCULATION END --------\n")

    return z, y_hat

#-----------------------------------------
# Step 3 : Plot ReLU Function
#-----------------------------------------
# This helps to VISUALIZE how ReLU behaves

def plot_relu():

    # Generate range of values of z
    z_values = np.linspace(-10, 10, 200)

    # Apply ReLU on all values
    relu_values = np.maximum(0, z_values)

    # Plot graph
    plt.figure(figsize=(8, 5))
    plt.plot(z_values, relu_values, label="ReLU Function", linewidth=2, color="green")

    # Axes lines
    plt.axhline(y = 0, color="black", linewidth = 0.5)
    plt.axvline(x = 0, color="gray", linestyle="--")

    # Labels and title
    plt.title("ReLU Activation Function", fontsize=16)
    plt.xlabel("Input (z)", fontsize=14)
    plt.ylabel("Output", fontsize=14)

    # Grid and legend
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.legend()

    # Show graph
    plt.show()

#-----------------------------------------
# Step 4 : Main Function
#-----------------------------------------

def main():
    print("\n========== MARVELLOUS NEURON DEMO =============\n")

    # Example Inputs (features)
    inputs = [1.0, 2.0, 3.0]

    # Corresponding Weights
    weights = [0.6, 0.4, -0.2]

    # Bias value
    bias =0.5

    # Perform forward propagation
    z, y_hat = Marvellous_neuron_forward(inputs, weights, bias)

    # Plot ReLU graph
    plot_relu()

#-----------------------------------------
# Starter
#-----------------------------------------

if __name__ == "__main__":
    main()
