import random

print("\n===================================================")
print("        MARVELLOUS LEARNING PROCESS DEMO")
print("===================================================\n")


# ---------------------------------------------------------
# STEP 1 : INITIAL DATA
# ---------------------------------------------------------

# Input and actual output
x = 2
actual_output = 10   # Expected output

print("INPUT VALUE       :", x)
print("EXPECTED OUTPUT   :", actual_output)


# ---------------------------------------------------------
# STEP 2 : RANDOM INITIAL WEIGHT
# ---------------------------------------------------------

weight = random.uniform(0, 1)   # random value between 0 and 1
learning_rate = 0.1

print("\nINITIAL SETTINGS")
print("----------------")
print("Initial Weight   :", weight)
print("Learning Rate    :", learning_rate)


# ---------------------------------------------------------
# TRAINING LOOP
# ---------------------------------------------------------

print("\n===================================================")
print("TRAINING STARTED")
print("===================================================\n")

for step in range(1, 11):   # keep 10 steps for classroom (not 1000)

    print(f"\n------------ STEP {step} ------------")

    # -------------------------------------------------
    # STEP 3 : FORWARD PASS
    # -------------------------------------------------

    predicted_output = x * weight

    print("\nFORWARD PASS")
    print(f"Predicted Output = {x} * {weight} = {predicted_output}")


    # -------------------------------------------------
    # STEP 4 : ERROR CALCULATION
    # -------------------------------------------------

    error = actual_output - predicted_output

    print("\nERROR CALCULATION")
    print(f"Error = {actual_output} - {predicted_output} = {error}")


    # -------------------------------------------------
    # STEP 5 : LOSS (SQUARED ERROR)
    # -------------------------------------------------

    loss = error ** 2

    print("\nLOSS CALCULATION")
    print(f"Loss = Error^2 = {loss}")


    # -------------------------------------------------
    # STEP 6 : WEIGHT UPDATE
    # -------------------------------------------------

    print("\nWEIGHT UPDATE")

    print(f"Old Weight = {weight}")

    # Simple update rule
    weight = weight + (learning_rate * error * x)

    print(f"New Weight = Old Weight + (lr * error * input)")
    print(f"New Weight = {weight}")


# ---------------------------------------------------------
# FINAL RESULT
# ---------------------------------------------------------

print("\n===================================================")
print("FINAL RESULT AFTER TRAINING")
print("===================================================\n")

final_output = x * weight

print("Final Weight     :", weight)
print("Final Prediction :", final_output)
print("Expected Output  :", actual_output)