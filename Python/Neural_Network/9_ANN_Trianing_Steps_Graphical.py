import random
import matplotlib.pyplot as plt

print("\n===================================================")
print("        MARVELLOUS LEARNING WITH VISUALIZATION")
print("===================================================\n")


# ---------------------------------------------------------
# STEP 1 : DATA
# ---------------------------------------------------------

x = 2
actual_output = 10

print("Input Value     :", x)
print("Expected Output :", actual_output)


# ---------------------------------------------------------
# STEP 2 : INITIAL SETTINGS
# ---------------------------------------------------------

weight = random.uniform(0, 1)
learning_rate = 0.1

print("\nInitial Weight :", weight)
print("Learning Rate  :", learning_rate)


# ---------------------------------------------------------
# STORE VALUES FOR GRAPH
# ---------------------------------------------------------

steps = []
loss_list = []
weight_list = []
prediction_list = []


# ---------------------------------------------------------
# TRAINING LOOP
# ---------------------------------------------------------

for step in range(1, 21):   # 20 steps for better graph

    print(f"\n------------ STEP {step} ------------")

    # Forward Pass
    predicted_output = x * weight
    print("Predicted Output :", predicted_output)

    # Error
    error = actual_output - predicted_output
    print("Error            :", error)

    # Loss
    loss = error ** 2
    print("Loss             :", loss)

    # Store values
    steps.append(step)
    loss_list.append(loss)
    weight_list.append(weight)
    prediction_list.append(predicted_output)

    # Update Weight
    weight = weight + (learning_rate * error * x)
    print("Updated Weight   :", weight)


# ---------------------------------------------------------
# FINAL RESULT
# ---------------------------------------------------------

print("\n===================================================")
print("FINAL RESULT")
print("===================================================\n")

final_output = x * weight

print("Final Weight     :", weight)
print("Final Prediction :", final_output)
print("Expected Output  :", actual_output)


# ---------------------------------------------------------
# GRAPH 1 : LOSS REDUCTION
# ---------------------------------------------------------

plt.figure()
plt.plot(steps, loss_list, marker='o')
plt.title("Loss Decreasing During Training")
plt.xlabel("Steps")
plt.ylabel("Loss")
plt.grid()
plt.show()


# ---------------------------------------------------------
# GRAPH 2 : PREDICTION VS ACTUAL
# ---------------------------------------------------------

actual_line = [actual_output] * len(steps)

plt.figure()
plt.plot(steps, prediction_list, marker='o', label="Predicted Output")
plt.plot(steps, actual_line, linestyle='--', label="Actual Output")
plt.title("Prediction Approaching Actual Output")
plt.xlabel("Steps")
plt.ylabel("Value")
plt.legend()
plt.grid()
plt.show()


# ---------------------------------------------------------
# GRAPH 3 : WEIGHT CHANGE
# ---------------------------------------------------------

plt.figure()
plt.plot(steps, weight_list, marker='o')
plt.title("Weight Adjustment During Learning")
plt.xlabel("Steps")
plt.ylabel("Weight Value")
plt.grid()
plt.show()
