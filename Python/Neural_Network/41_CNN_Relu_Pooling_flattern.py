# ------------------------------------------------------------
# CNN Internal Steps Demonstration
# ReLU
# Pooling
# Flatten
# Fully Connected Layer
# ------------------------------------------------------------

import numpy as np

# ------------------------------------------------------------
# Function to print line
# ------------------------------------------------------------
def Marvellous_Line():
    print("\n" + "-" * 60)

# ------------------------------------------------------------
# MAIN FUNCTION
# ------------------------------------------------------------
def Marvellous_CNN_Internal_Steps():

    # --------------------------------------------------------
    # Assume this is output from Convolution Layer
    # --------------------------------------------------------
    feature_map = np.array([
        [-2, 5, 1, 2],
        [ 3,-1, 4, 1],
        [ 0, 2, 0, 6],
        [ 1, 3, 2, 0]
    ], dtype=float)

    Marvellous_Line()
    print("STEP 1 : INPUT FEATURE MAP (After Convolution)")
    Marvellous_Line()
    print(feature_map)

    # ========================================================
    # STEP 2 : ReLU
    # ========================================================
    Marvellous_Line()
    print("STEP 2 : ReLU ACTIVATION")
    Marvellous_Line()

    print("Rule : ReLU(x) = max(0,x)\n")

    relu_output = np.maximum(0, feature_map)

    for i in range(feature_map.shape[0]):
        for j in range(feature_map.shape[1]):
            print(f"ReLU({feature_map[i][j]:.0f}) = {relu_output[i][j]:.0f}")

    print("\nOutput After ReLU:")
    print(relu_output)

    # ========================================================
    # STEP 3 : Max Pooling
    # ========================================================
    Marvellous_Line()
    print("STEP 3 : MAX POOLING (2x2)")
    Marvellous_Line()

    pooling_output = np.zeros((2,2))

    # Block 1
    block1 = relu_output[0:2,0:2]
    pooling_output[0][0] = np.max(block1)

    print("\nBlock 1:")
    print(block1)
    print("Max =", np.max(block1))

    # Block 2
    block2 = relu_output[0:2,2:4]
    pooling_output[0][1] = np.max(block2)

    print("\nBlock 2:")
    print(block2)
    print("Max =", np.max(block2))

    # Block 3
    block3 = relu_output[2:4,0:2]
    pooling_output[1][0] = np.max(block3)

    print("\nBlock 3:")
    print(block3)
    print("Max =", np.max(block3))

    # Block 4
    block4 = relu_output[2:4,2:4]
    pooling_output[1][1] = np.max(block4)

    print("\nBlock 4:")
    print(block4)
    print("Max =", np.max(block4))

    print("\nOutput After Pooling:")
    print(pooling_output)

    # ========================================================
    # STEP 4 : Flatten
    # ========================================================
    Marvellous_Line()
    print("STEP 4 : FLATTEN")
    Marvellous_Line()

    flatten_output = pooling_output.flatten()

    print("Input Matrix:")
    print(pooling_output)

    print("\nFlatten Output:")
    print(flatten_output)

    # ========================================================
    # STEP 5 : Fully Connected Layer
    # ========================================================
    Marvellous_Line()
    print("STEP 5 : FULLY CONNECTED LAYER")
    Marvellous_Line()

    weights = np.array([0.8, 0.5, 0.3, 0.9])
    bias = 1.0

    print("Flatten Input :", flatten_output)
    print("Weights       :", weights)
    print("Bias          :", bias)

    multiplication = flatten_output * weights

    print("\nInput × Weight:")

    for i in range(len(flatten_output)):
        print(f"{flatten_output[i]:.0f} × {weights[i]} = {multiplication[i]:.2f}")

    total = np.sum(multiplication)

    print("\nSum =", total)

    final_output = total + bias

    print("Final Output = Sum + Bias")
    print(f"{total:.2f} + {bias} = {final_output:.2f}")

    # ========================================================
    # Final Prediction
    # ========================================================
    Marvellous_Line()
    print("STEP 6 : FINAL DECISION")
    Marvellous_Line()

    if final_output > 10:
        print("Prediction : Strong Feature Detected")
    else:
        print("Prediction : Weak Feature Detected")

if __name__ == "__main__":
    Marvellous_CNN_Internal_Steps()