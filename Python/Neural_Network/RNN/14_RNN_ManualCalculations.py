# ============================================================
# Program 14 : Manual RNN Calculation
# Target:
# Understand mathematical calculation of hidden state
# ============================================================

import numpy as np

# Sentence: food was not good
# Token sequence: [1, 2, 5, 3]

inputs = [1, 2, 5, 3]

hidden_state = 0

Wx = 0.5      # Weight for current input
Wh = 0.8      # Weight for previous hidden state
bias = 0.1

print("=" * 60)
print("        Marvellous Infosystems")
print("   RNN Applications - Program 14")
print("=" * 60)

print("Target of this Program:")
print("Calculate hidden state manually using RNN formula")
print("-" * 60)

print("Formula:")
print("h_t = tanh(Wx * x_t + Wh * h_t-1 + bias)")
print("-" * 60)

for time_step, x in enumerate(inputs):
    previous_hidden_state = hidden_state

    weighted_input = Wx * x
    weighted_memory = Wh * previous_hidden_state
    total = weighted_input + weighted_memory + bias

    hidden_state = np.tanh(total)

    print("Time Step:", time_step + 1)
    print("Current Input x_t           :", x)
    print("Previous Hidden State h_t-1 :", previous_hidden_state)
    print("Wx * x_t                    :", Wx, "*", x, "=", weighted_input)
    print("Wh * h_t-1                  :", Wh, "*", previous_hidden_state, "=", weighted_memory)
    print("Bias                        :", bias)
    print("Total                       :", total)
    print("Updated h_t = tanh(total)   :", hidden_state)
    print("-" * 60)

print("Final Hidden State:", hidden_state)
print("Final hidden state stores meaning of the full sequence.")