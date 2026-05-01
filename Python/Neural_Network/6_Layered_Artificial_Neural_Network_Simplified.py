import math

print("\n===================================================")
print("        MARVELLOUS FORWARD PROPAGATION DEMO")
print("===================================================\n")


# ---------------------------------------------------------
# STEP 1 : INPUT LAYER
# ---------------------------------------------------------

x1 = 2.0
x2 = 3.0

print("STEP 1 : INPUT LAYER")
print("---------------------")
print("Input Features (x):")
print(f"  x1 = {x1}")
print(f"  x2 = {x2}")

print("\nMeaning:")
print("  These inputs can represent features like marks, pixels, etc.")


# ---------------------------------------------------------
# STEP 2 : HIDDEN LAYER
# ---------------------------------------------------------

print("\n===================================================")
print("STEP 2 : HIDDEN LAYER (2 NEURONS)")
print("===================================================\n")


# ===================== HIDDEN NEURON 1 =====================

print("HIDDEN NEURON 1")
print("----------------")

w11 = 0.5
w12 = -0.2
b1 = 0.1

print("Weights:")
print(f"  w11 = {w11}, w12 = {w12}")
print("Bias:")
print(f"  b1 = {b1}")

print("\nFormula:")
print("  z1 = (x1*w11 + x2*w12) + b1")

# Step 1: Multiplication
m1 = x1 * w11
m2 = x2 * w12

print("\nStep 1: Multiply Inputs with Weights")
print(f"  x1*w11 = {x1} * {w11} = {m1}")
print(f"  x2*w12 = {x2} * {w12} = {m2}")

# Step 2: Weighted Sum
z1 = m1 + m2 + b1
print("\nStep 2: Add Bias")
print(f"  z1 = {m1} + {m2} + {b1} = {z1}")

# Step 3: Activation
h1 = max(0, z1)
print("\nStep 3: Apply ReLU Activation")
print(f"  ReLU(z1) = max(0, {z1}) = {h1}")

print("\nOutput of Hidden Neuron 1 (h1):", h1)


# ===================== HIDDEN NEURON 2 =====================

print("\n--------------------------------")
print("HIDDEN NEURON 2")
print("--------------------------------")

w21 = 0.8
w22 = 0.4
b2 = -0.1

print("Weights:")
print(f"  w21 = {w21}, w22 = {w22}")
print("Bias:")
print(f"  b2 = {b2}")

print("\nFormula:")
print("  z2 = (x1*w21 + x2*w22) + b2")

# Step 1: Multiplication
m3 = x1 * w21
m4 = x2 * w22

print("\nStep 1: Multiply Inputs with Weights")
print(f"  x1*w21 = {x1} * {w21} = {m3}")
print(f"  x2*w22 = {x2} * {w22} = {m4}")

# Step 2: Weighted Sum
z2 = m3 + m4 + b2
print("\nStep 2: Add Bias")
print(f"  z2 = {m3} + {m4} + {b2} = {z2}")

# Step 3: Activation
h2 = max(0, z2)
print("\nStep 3: Apply ReLU Activation")
print(f"  ReLU(z2) = max(0, {z2}) = {h2}")

print("\nOutput of Hidden Neuron 2 (h2):", h2)


# ---------------------------------------------------------
# STEP 3 : OUTPUT LAYER
# ---------------------------------------------------------

print("\n===================================================")
print("STEP 3 : OUTPUT LAYER (FINAL PREDICTION)")
print("===================================================\n")

w_out1 = 1.0
w_out2 = -1.5
b_out = 0.2

print("Weights:")
print(f"  w_out1 = {w_out1}, w_out2 = {w_out2}")
print("Bias:")
print(f"  b_out = {b_out}")

print("\nFormula:")
print("  z_out = (h1*w_out1 + h2*w_out2) + b_out")

# Step 1: Multiplication
m5 = h1 * w_out1
m6 = h2 * w_out2

print("\nStep 1: Multiply Hidden Outputs")
print(f"  h1*w_out1 = {h1} * {w_out1} = {m5}")
print(f"  h2*w_out2 = {h2} * {w_out2} = {m6}")

# Step 2: Weighted Sum
z_out = m5 + m6 + b_out
print("\nStep 2: Add Bias")
print(f"  z_out = {m5} + {m6} + {b_out} = {z_out}")

# Step 3: Activation
output = 1 / (1 + math.exp(-z_out))

print("\nStep 3: Apply Sigmoid Activation")
print(f"  Sigmoid(z_out) = 1 / (1 + e^(-{z_out})) = {output}")


# ---------------------------------------------------------
# FINAL RESULT
# ---------------------------------------------------------

print("\n===================================================")
print("FINAL RESULT")
print("===================================================\n")

print(f"Hidden Layer Outputs : h1 = {h1}, h2 = {h2}")
print(f"Final Output (ŷ)     : {output}")
print(f"Confidence (%)       : {output * 100:.2f}%")

print("\nDecision Rule:")
print("  If output >= 0.5 → Positive Class")
print("  If output < 0.5 → Negative Class")

if output >= 0.5:
    print("\nPrediction : Positive Class")
else:
    print("\nPrediction : Negative Class")