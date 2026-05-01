# ============================================================
# Program 17 : Binary Crossentropy Loss
# Target:
# Understand loss calculation for binary classification
# ============================================================

import numpy as np

def binary_crossentropy(actual, predicted):
    return -(actual * np.log(predicted) + (1 - actual) * np.log(1 - predicted))

examples = [
    [1, 0.90],
    [1, 0.60],
    [1, 0.20],
    [0, 0.10],
    [0, 0.40],
    [0, 0.80]
]

print("=" * 60)
print("        Marvellous Infosystems")
print("   RNN Applications - Program 17")
print("=" * 60)

print("Target of this Program:")
print("Understand binary crossentropy loss")
print("-" * 60)

print("Formula:")
print("Loss = -[y log(p) + (1-y) log(1-p)]")
print("-" * 60)

for actual, predicted in examples:
    loss = binary_crossentropy(actual, predicted)

    print("Actual Label          :", actual)
    print("Predicted Probability:", predicted)
    print("Loss                 :", loss)
    print("-" * 60)

print("Conclusion:")
print("Good prediction gives small loss. Wrong prediction gives large loss.")