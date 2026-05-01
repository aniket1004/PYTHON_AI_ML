# ============================================================
# Program 16 : Sigmoid Function
# Target:
# Understand sigmoid function used for binary output
# ============================================================

import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

values = [-3, -1, 0, 1, 3]

print("=" * 60)
print("        Marvellous Infosystems")
print("   RNN Applications - Program 16")
print("=" * 60)

print("Target of this Program:")
print("Understand sigmoid function for Positive/Negative decision")
print("-" * 60)

print("Formula:")
print("sigmoid(x) = 1 / (1 + e^-x)")
print("-" * 60)

for value in values:
    result = sigmoid(value)

    print("Input:", value)
    print("Sigmoid Output:", result)

    if result >= 0.5:
        print("Decision: Positive")
    else:
        print("Decision: Negative")

    print("-" * 60)