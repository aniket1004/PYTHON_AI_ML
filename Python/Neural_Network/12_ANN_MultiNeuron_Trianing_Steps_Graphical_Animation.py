# ---------------------------------------------------------
# Network : 2 Inputs -> 2 Hidden Neurons -> 1 Output
# ---------------------------------------------------------

import random
import matplotlib.pyplot as plt

print("\n==========================================================")
print("      MARVELLOUS MULTI-NEURON ANN TRAINING DEMO")
print("==========================================================\n")

# ---------------------------------------------------------
# STEP 1 : INPUT DATA
# ---------------------------------------------------------
# Simple input values
x1 = 2.0
x2 = 3.0

# Expected output
actual_output = 8.0

print("INPUT DATA")
print("----------")
print(f"x1 = {x1}")
print(f"x2 = {x2}")
print(f"Actual Output = {actual_output}")

# ---------------------------------------------------------
# STEP 2 : INITIAL RANDOM WEIGHTS AND BIASES
# ---------------------------------------------------------

# Hidden neuron 1
w11 = random.uniform(0, 1)
w12 = random.uniform(0, 1)
b1 = random.uniform(0, 1)

# Hidden neuron 2
w21 = random.uniform(0, 1)
w22 = random.uniform(0, 1)
b2 = random.uniform(0, 1)

# Output neuron
w_out1 = random.uniform(0, 1)
w_out2 = random.uniform(0, 1)
b_out = random.uniform(0, 1)

learning_rate = 0.01

print("\nINITIAL PARAMETERS")
print("------------------")
print(f"w11 = {w11:.4f}, w12 = {w12:.4f}, b1 = {b1:.4f}")
print(f"w21 = {w21:.4f}, w22 = {w22:.4f}, b2 = {b2:.4f}")
print(f"w_out1 = {w_out1:.4f}, w_out2 = {w_out2:.4f}, b_out = {b_out:.4f}")
print(f"Learning Rate = {learning_rate}")

# ---------------------------------------------------------
# STEP 3 : LISTS FOR GRAPHICAL REPRESENTATION
# ---------------------------------------------------------

steps = []
loss_list = []
prediction_list = []
actual_list = []

h1_list = []
h2_list = []

w11_list = []
w12_list = []
w21_list = []
w22_list = []
wout1_list = []
wout2_list = []

# ---------------------------------------------------------
# STEP 4 : TRAINING LOOP
# ---------------------------------------------------------

for step in range(1, 51):

    print(f"\n==================== TRAINING STEP {step} ====================")

    # -----------------------------------------------------
    # FORWARD PASS - HIDDEN NEURON 1
    # -----------------------------------------------------
    z1 = (x1 * w11) + (x2 * w12) + b1
    h1 = max(0, z1)   # ReLU

    print("\nHidden Neuron 1")
    print(f"z1 = ({x1} * {w11:.4f}) + ({x2} * {w12:.4f}) + {b1:.4f} = {z1:.4f}")
    print(f"h1 = ReLU(z1) = {h1:.4f}")

    # -----------------------------------------------------
    # FORWARD PASS - HIDDEN NEURON 2
    # -----------------------------------------------------
    z2 = (x1 * w21) + (x2 * w22) + b2
    h2 = max(0, z2)   # ReLU

    print("\nHidden Neuron 2")
    print(f"z2 = ({x1} * {w21:.4f}) + ({x2} * {w22:.4f}) + {b2:.4f} = {z2:.4f}")
    print(f"h2 = ReLU(z2) = {h2:.4f}")

    # -----------------------------------------------------
    # FORWARD PASS - OUTPUT NEURON
    # -----------------------------------------------------
    predicted_output = (h1 * w_out1) + (h2 * w_out2) + b_out

    print("\nOutput Neuron")
    print(f"Predicted Output = ({h1:.4f} * {w_out1:.4f}) + ({h2:.4f} * {w_out2:.4f}) + {b_out:.4f}")
    print(f"Predicted Output = {predicted_output:.4f}")

    # -----------------------------------------------------
    # ERROR AND LOSS
    # -----------------------------------------------------
    error = actual_output - predicted_output
    loss = error ** 2

    print("\nError and Loss")
    print(f"Error = {actual_output:.4f} - {predicted_output:.4f} = {error:.4f}")
    print(f"Loss  = Error^2 = {loss:.4f}")

    # -----------------------------------------------------
    # STORE VALUES FOR GRAPHS
    # -----------------------------------------------------
    steps.append(step)
    loss_list.append(loss)
    prediction_list.append(predicted_output)
    actual_list.append(actual_output)

    h1_list.append(h1)
    h2_list.append(h2)

    w11_list.append(w11)
    w12_list.append(w12)
    w21_list.append(w21)
    w22_list.append(w22)
    wout1_list.append(w_out1)
    wout2_list.append(w_out2)

    # -----------------------------------------------------
    # SIMPLE WEIGHT UPDATE
    # -----------------------------------------------------
    # Output layer weights update
    w_out1 = w_out1 + (learning_rate * error * h1)
    w_out2 = w_out2 + (learning_rate * error * h2)
    b_out = b_out + (learning_rate * error)

    # Hidden layer rough update
    if z1 > 0:
        w11 = w11 + (learning_rate * error * x1 * w_out1 * 0.1)
        w12 = w12 + (learning_rate * error * x2 * w_out1 * 0.1)
        b1 = b1 + (learning_rate * error * w_out1 * 0.1)

    if z2 > 0:
        w21 = w21 + (learning_rate * error * x1 * w_out2 * 0.1)
        w22 = w22 + (learning_rate * error * x2 * w_out2 * 0.1)
        b2 = b2 + (learning_rate * error * w_out2 * 0.1)

    print("\nUpdated Parameters")
    print(f"w11 = {w11:.4f}, w12 = {w12:.4f}, b1 = {b1:.4f}")
    print(f"w21 = {w21:.4f}, w22 = {w22:.4f}, b2 = {b2:.4f}")
    print(f"w_out1 = {w_out1:.4f}, w_out2 = {w_out2:.4f}, b_out = {b_out:.4f}")

# ---------------------------------------------------------
# FINAL RESULT
# ---------------------------------------------------------

print("\n==========================================================")
print("FINAL RESULT AFTER TRAINING")
print("==========================================================\n")

final_z1 = (x1 * w11) + (x2 * w12) + b1
final_h1 = max(0, final_z1)

final_z2 = (x1 * w21) + (x2 * w22) + b2
final_h2 = max(0, final_z2)

final_output = (final_h1 * w_out1) + (final_h2 * w_out2) + b_out

print(f"Final Hidden Output h1 = {final_h1:.4f}")
print(f"Final Hidden Output h2 = {final_h2:.4f}")
print(f"Final Prediction       = {final_output:.4f}")
print(f"Actual Output          = {actual_output:.4f}")
print(f"Final Error            = {actual_output - final_output:.4f}")

# ---------------------------------------------------------
# GRAPH 1 : LOSS DECREASING
# ---------------------------------------------------------

plt.figure(figsize=(8, 5))
plt.plot(steps, loss_list, marker='o')
plt.title("Loss Decreasing During ANN Training")
plt.xlabel("Training Step")
plt.ylabel("Loss")
plt.grid(True)
plt.show()

# ---------------------------------------------------------
# GRAPH 2 : PREDICTION VS ACTUAL
# ---------------------------------------------------------

plt.figure(figsize=(8, 5))
plt.plot(steps, prediction_list, marker='o', label="Predicted Output")
plt.plot(steps, actual_list, linestyle='--', label="Actual Output")
plt.title("Prediction Approaching Actual Output")
plt.xlabel("Training Step")
plt.ylabel("Output Value")
plt.legend()
plt.grid(True)
plt.show()

# ---------------------------------------------------------
# GRAPH 3 : HIDDEN NEURON OUTPUTS
# ---------------------------------------------------------

plt.figure(figsize=(8, 5))
plt.plot(steps, h1_list, marker='o', label="Hidden Neuron h1")
plt.plot(steps, h2_list, marker='s', label="Hidden Neuron h2")
plt.title("Hidden Neuron Activations During Training")
plt.xlabel("Training Step")
plt.ylabel("Activation Value")
plt.legend()
plt.grid(True)
plt.show()

# ---------------------------------------------------------
# GRAPH 4 : OUTPUT WEIGHTS CHANGE
# ---------------------------------------------------------

plt.figure(figsize=(8, 5))
plt.plot(steps, wout1_list, marker='o', label="w_out1")
plt.plot(steps, wout2_list, marker='s', label="w_out2")
plt.title("Output Layer Weights During Training")
plt.xlabel("Training Step")
plt.ylabel("Weight Value")
plt.legend()
plt.grid(True)
plt.show()

# ---------------------------------------------------------
# GRAPH 5 : HIDDEN LAYER WEIGHTS CHANGE
# ---------------------------------------------------------

plt.figure(figsize=(10, 5))
plt.plot(steps, w11_list, label="w11")
plt.plot(steps, w12_list, label="w12")
plt.plot(steps, w21_list, label="w21")
plt.plot(steps, w22_list, label="w22")
plt.title("Hidden Layer Weights During Training")
plt.xlabel("Training Step")
plt.ylabel("Weight Value")
plt.legend()
plt.grid(True)
plt.show()

# ---------------------------------------------------------
# GRAPH 6 : FINAL ANN STRUCTURE WITH ALL VALUES
# ---------------------------------------------------------

plt.figure(figsize=(14, 8))

# -------------------------------
# Node positions
# -------------------------------

# Input layer
input_x = [1, 1]
input_y = [5, 1]

# Hidden layer
hidden_x = [5, 5]
hidden_y = [6, 0]

# Output layer
output_x = [9]
output_y = [3]

# -------------------------------
# Draw neurons
# -------------------------------

plt.scatter(input_x, input_y, s=3500)
plt.scatter(hidden_x, hidden_y, s=3500)
plt.scatter(output_x, output_y, s=3500)

# -------------------------------
# Draw connections
# -------------------------------

# Input -> Hidden
for i in range(2):
    for j in range(2):
        plt.plot([input_x[i], hidden_x[j]], [input_y[i], hidden_y[j]], linewidth=2)

# Hidden -> Output
for j in range(2):
    plt.plot([hidden_x[j], output_x[0]], [hidden_y[j], output_y[0]], linewidth=2)

# -------------------------------
# Label neurons with values
# -------------------------------

# Input neurons
plt.text(input_x[0], input_y[0], f"x1\n{x1:.2f}", ha='center', va='center', fontsize=12)
plt.text(input_x[1], input_y[1], f"x2\n{x2:.2f}", ha='center', va='center', fontsize=12)

# Hidden neurons
plt.text(hidden_x[0], hidden_y[0], f"h1\n{final_h1:.2f}", ha='center', va='center', fontsize=12)
plt.text(hidden_x[1], hidden_y[1], f"h2\n{final_h2:.2f}", ha='center', va='center', fontsize=12)

# Output neuron
plt.text(output_x[0], output_y[0], f"y_hat\n{final_output:.2f}", ha='center', va='center', fontsize=12)

# -------------------------------
# Layer labels
# -------------------------------

plt.text(1, 7.2, "Input Layer", ha='center', fontsize=14, fontweight='bold')
plt.text(5, 7.2, "Hidden Layer", ha='center', fontsize=14, fontweight='bold')
plt.text(9, 7.2, "Output Layer", ha='center', fontsize=14, fontweight='bold')

# -------------------------------
# Weight labels : Input -> Hidden
# -------------------------------

plt.text(2.7, 5.6, f"w11 = {w11:.2f}", fontsize=11)
plt.text(2.7, 3.6, f"w12 = {w12:.2f}", fontsize=11)
plt.text(2.7, 2.4, f"w21 = {w21:.2f}", fontsize=11)
plt.text(2.7, 0.4, f"w22 = {w22:.2f}", fontsize=11)

# -------------------------------
# Weight labels : Hidden -> Output
# -------------------------------

plt.text(6.8, 5.0, f"w_out1 = {w_out1:.2f}", fontsize=11)
plt.text(6.8, 1.0, f"w_out2 = {w_out2:.2f}", fontsize=11)

# -------------------------------
# Bias labels
# -------------------------------

plt.text(5.8, 6.5, f"b1 = {b1:.2f}", fontsize=11)
plt.text(5.8, -0.5, f"b2 = {b2:.2f}", fontsize=11)
plt.text(9.8, 3.2, f"b_out = {b_out:.2f}", fontsize=11)

# -------------------------------
# Extra information
# -------------------------------

plt.text(9, -1.0, f"Actual Output = {actual_output:.2f}", ha='center', fontsize=12, fontweight='bold')
plt.text(9, -1.7, f"Final Error = {actual_output - final_output:.4f}", ha='center', fontsize=12)

plt.title("Final Artificial Neural Network Structure with All Values", fontsize=16, fontweight='bold')
plt.xlim(0, 11)
plt.ylim(-2.5, 8)
plt.axis('off')
plt.show()

# ---------------------------------------------------------
# GRAPH 7 : ANIMATED ANN OUTPUT
# ---------------------------------------------------------

from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots(figsize=(14, 8))

def update(frame):
    ax.clear()

    # Fixed positions
    input_x = [1, 1]
    input_y = [5, 1]

    hidden_x = [5, 5]
    hidden_y = [6, 0]

    output_x = [9]
    output_y = [3]

    # Current values from training history
    current_h1 = h1_list[frame]
    current_h2 = h2_list[frame]
    current_output = prediction_list[frame]

    current_w11 = w11_list[frame]
    current_w12 = w12_list[frame]
    current_w21 = w21_list[frame]
    current_w22 = w22_list[frame]
    current_wout1 = wout1_list[frame]
    current_wout2 = wout2_list[frame]

    # Draw neurons
    ax.scatter(input_x, input_y, s=3500)
    ax.scatter(hidden_x, hidden_y, s=3500)
    ax.scatter(output_x, output_y, s=3500)

    # Draw connections
    for i in range(2):
        for j in range(2):
            ax.plot([input_x[i], hidden_x[j]], [input_y[i], hidden_y[j]], linewidth=2)

    for j in range(2):
        ax.plot([hidden_x[j], output_x[0]], [hidden_y[j], output_y[0]], linewidth=2)

    # Label neuron values
    ax.text(input_x[0], input_y[0], f"x1\n{x1:.2f}", ha='center', va='center', fontsize=12)
    ax.text(input_x[1], input_y[1], f"x2\n{x2:.2f}", ha='center', va='center', fontsize=12)

    ax.text(hidden_x[0], hidden_y[0], f"h1\n{current_h1:.2f}", ha='center', va='center', fontsize=12)
    ax.text(hidden_x[1], hidden_y[1], f"h2\n{current_h2:.2f}", ha='center', va='center', fontsize=12)

    ax.text(output_x[0], output_y[0], f"y_hat\n{current_output:.2f}", ha='center', va='center', fontsize=12)

    # Layer names
    ax.text(1, 7.2, "Input Layer", ha='center', fontsize=14, fontweight='bold')
    ax.text(5, 7.2, "Hidden Layer", ha='center', fontsize=14, fontweight='bold')
    ax.text(9, 7.2, "Output Layer", ha='center', fontsize=14, fontweight='bold')

    # Weight labels
    ax.text(2.7, 5.6, f"w11 = {current_w11:.2f}", fontsize=11)
    ax.text(2.7, 3.6, f"w12 = {current_w12:.2f}", fontsize=11)
    ax.text(2.7, 2.4, f"w21 = {current_w21:.2f}", fontsize=11)
    ax.text(2.7, 0.4, f"w22 = {current_w22:.2f}", fontsize=11)

    ax.text(6.8, 5.0, f"w_out1 = {current_wout1:.2f}", fontsize=11)
    ax.text(6.8, 1.0, f"w_out2 = {current_wout2:.2f}", fontsize=11)

    # Step info
    ax.text(9, -1.0, f"Training Step = {steps[frame]}", ha='center', fontsize=12, fontweight='bold')
    ax.text(9, -1.7, f"Predicted = {current_output:.4f}   Actual = {actual_output:.4f}", ha='center', fontsize=12)
    ax.text(9, -2.4, f"Loss = {loss_list[frame]:.4f}", ha='center', fontsize=12)

    ax.set_title("Animated ANN Learning Process", fontsize=16, fontweight='bold')
    ax.set_xlim(0, 11)
    ax.set_ylim(-3, 8)
    ax.axis('off')

ani = FuncAnimation(fig, update, frames=len(steps), interval=700, repeat=True)
plt.show()