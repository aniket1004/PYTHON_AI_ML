# ============================================================
# Program 15 : Tanh Function
# Target:
# Understand tanh activation used inside SimpleRNN
# ============================================================

import numpy as np

values = [-3, -1, 0, 1, 3]

print("=" * 60)
print("        Marvellous Infosystems")
print("   RNN Applications - Program 15")
print("=" * 60)

print("Target of this Program:")
print("Understand tanh activation function")
print("-" * 60)

print("Formula:")
print("tanh(x) gives value between -1 and +1")
print("-" * 60)

for value in values:
    result = np.tanh(value)
    print("Input:", value)
    print("tanh :", result)
    print("-" * 60)

print("Conclusion:")
print("RNN uses tanh to keep hidden state values in controlled range.")