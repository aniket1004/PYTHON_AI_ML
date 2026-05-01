import math
import matplotlib.pyplot as plt
import numpy as np

print("\n===================================================")
print("     MARVELLOUS ANN FORWARD PROPAGATION DEMO")
print("===================================================\n")


# ---------------------------------------------------------
# STEP 1 : INPUT LAYER
# ---------------------------------------------------------
# We have 2 inputs

x1 = 2.0
x2 = 3.0

print("STEP 1 : INPUT LAYER")
print("---------------------")
print("Input x1 =", x1)
print("Input x2 =", x2)


# ---------------------------------------------------------
# STEP 2 : HIDDEN LAYER - NEURON 1
# ---------------------------------------------------------
# Hidden neuron 1 weights and bias

w11 = 0.5
w12 = -0.2
b1 = 0.1

print("\nSTEP 2 : HIDDEN LAYER - NEURON 1")
print("--------------------------------")
print("Weights : w11 =", w11, ", w12 =", w12)
print("Bias    : b1  =", b1)

m1 = x1 * w11
m2 = x2 * w12

print("\nMultiplication:")
print(f"x1 * w11 = {x1} * {w11} = {m1}")
print(f"x2 * w12 = {x2} * {w12} = {m2}")

z1 = m1 + m2 + b1
print(f"\nWeighted Sum z1 = {m1} + {m2} + {b1} = {z1}")

h1 = max(0, z1)   # ReLU
print(f"ReLU(z1) = max(0, {z1}) = {h1}")


# ---------------------------------------------------------
# STEP 3 : HIDDEN LAYER - NEURON 2
# ---------------------------------------------------------
# Hidden neuron 2 weights and bias

w21 = 0.8
w22 = 0.4
b2 = -0.1

print("\nSTEP 3 : HIDDEN LAYER - NEURON 2")
print("--------------------------------")
print("Weights : w21 =", w21, ", w22 =", w22)
print("Bias    : b2  =", b2)

m3 = x1 * w21
m4 = x2 * w22

print("\nMultiplication:")
print(f"x1 * w21 = {x1} * {w21} = {m3}")
print(f"x2 * w22 = {x2} * {w22} = {m4}")

z2 = m3 + m4 + b2
print(f"\nWeighted Sum z2 = {m3} + {m4} + {b2} = {z2}")

h2 = max(0, z2)   # ReLU
print(f"ReLU(z2) = max(0, {z2}) = {h2}")


# ---------------------------------------------------------
# STEP 4 : OUTPUT LAYER
# ---------------------------------------------------------
# Output neuron weights and bias

w_out1 = 1.0
w_out2 = -1.5
b_out = 0.2

print("\nSTEP 4 : OUTPUT LAYER")
print("----------------------")
print("Weights : w_out1 =", w_out1, ", w_out2 =", w_out2)
print("Bias    : b_out  =", b_out)

m5 = h1 * w_out1
m6 = h2 * w_out2

print("\nMultiplication:")
print(f"h1 * w_out1 = {h1} * {w_out1} = {m5}")
print(f"h2 * w_out2 = {h2} * {w_out2} = {m6}")

z_out = m5 + m6 + b_out
print(f"\nWeighted Sum z_out = {m5} + {m6} + {b_out} = {z_out}")

output = 1 / (1 + math.exp(-z_out))   # Sigmoid
print(f"Sigmoid(z_out) = 1 / (1 + e^(-{z_out})) = {output}")


# ---------------------------------------------------------
# STEP 5 : FINAL RESULT
# ---------------------------------------------------------

print("\nSTEP 5 : FINAL RESULT")
print("----------------------")
print("Hidden Neuron 1 Output (h1) :", h1)
print("Hidden Neuron 2 Output (h2) :", h2)
print("Final Output                :", output)
print("Confidence Percentage       :", round(output * 100, 2), "%")

if output >= 0.5:
    print("Prediction                  : Positive Class")
else:
    print("Prediction                  : Negative Class")


# ---------------------------------------------------------
# GRAPH 1 : ANN STRUCTURE DIAGRAM
# ---------------------------------------------------------

plt.figure(figsize=(10, 6))

# Node positions
input_x = [1, 1]
input_y = [2, 1]

hidden_x = [3, 3]
hidden_y = [2.5, 0.5]

output_x = [5]
output_y = [1.5]

# Plot nodes
plt.scatter(input_x, input_y, s=1200)
plt.scatter(hidden_x, hidden_y, s=1200)
plt.scatter(output_x, output_y, s=1200)

# Draw input to hidden connections
for i in range(2):
    for j in range(2):
        plt.plot([input_x[i], hidden_x[j]], [input_y[i], hidden_y[j]])

# Draw hidden to output connections
for j in range(2):
    plt.plot([hidden_x[j], output_x[0]], [hidden_y[j], output_y[0]])

# Label nodes
plt.text(0.85, 2, f"x1\n{x1}", ha='center', va='center', fontsize=10)
plt.text(0.85, 1, f"x2\n{x2}", ha='center', va='center', fontsize=10)

plt.text(3, 2.5, f"h1\n{h1:.2f}", ha='center', va='center', fontsize=10)
plt.text(3, 0.5, f"h2\n{h2:.2f}", ha='center', va='center', fontsize=10)

plt.text(5, 1.5, f"y\n{output:.3f}", ha='center', va='center', fontsize=10)

# Layer labels
plt.text(1, 2.9, "Input Layer", ha='center', fontsize=12)
plt.text(3, 3.2, "Hidden Layer", ha='center', fontsize=12)
plt.text(5, 2.2, "Output Layer", ha='center', fontsize=12)

# Weight labels
plt.text(1.8, 2.3, f"w11={w11}", fontsize=9)
plt.text(1.8, 1.3, f"w12={w12}", fontsize=9)
plt.text(1.8, 1.8, f"w21={w21}", fontsize=9)
plt.text(1.8, 0.8, f"w22={w22}", fontsize=9)

plt.text(4, 2.2, f"w_out1={w_out1}", fontsize=9)
plt.text(4, 1.0, f"w_out2={w_out2}", fontsize=9)

plt.title("Artificial Neural Network Structure with Values")
plt.axis('off')
plt.show()


# ---------------------------------------------------------
# GRAPH 2 : BAR CHART OF HIDDEN AND OUTPUT VALUES
# ---------------------------------------------------------

labels = ['Hidden Neuron 1', 'Hidden Neuron 2', 'Final Output']
values = [h1, h2, output]

plt.figure(figsize=(8, 5))
bars = plt.bar(labels, values)

plt.title("Neuron Outputs")
plt.xlabel("Neurons")
plt.ylabel("Output Value")
plt.ylim(0, max(values) + 1)

# Add values on bars
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 0.05, round(yval, 3),
             ha='center', va='bottom', fontsize=10)

plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.show()


# ---------------------------------------------------------
# GRAPH 3 : SIGMOID FUNCTION WITH OUTPUT POINT
# ---------------------------------------------------------

z_values = np.linspace(-6, 6, 200)
sigmoid_values = 1 / (1 + np.exp(-z_values))

plt.figure(figsize=(8, 5))
plt.plot(z_values, sigmoid_values, label="Sigmoid Function", linewidth=2)

# Mark the actual network output point
plt.scatter(z_out, output, s=100, label="Network Output Point")
plt.text(z_out, output + 0.05, f"({z_out:.2f}, {output:.3f})", fontsize=10)

plt.axhline(y=0.5, linestyle='--', alpha=0.7)
plt.axvline(x=0, linestyle='--', alpha=0.7)

plt.title("Sigmoid Function with Network Output")
plt.xlabel("Input to Sigmoid (z_out)")
plt.ylabel("Output")
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()


# ---------------------------------------------------------
# GRAPH 4 : INPUT vs HIDDEN vs OUTPUT FLOW
# ---------------------------------------------------------

stage_labels = ['Input x1', 'Input x2', 'Hidden h1', 'Hidden h2', 'Final Output']
stage_values = [x1, x2, h1, h2, output]

plt.figure(figsize=(10, 5))
plt.plot(stage_labels, stage_values, marker='o', linewidth=2)

for i in range(len(stage_labels)):
    plt.text(i, stage_values[i] + 0.05, round(stage_values[i], 3),
             ha='center', fontsize=10)

plt.title("Flow of Values Through the Network")
plt.xlabel("Stages")
plt.ylabel("Value")
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()