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
    # SIMPLE WEIGHT UPDATE (TEACHING VERSION)
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

