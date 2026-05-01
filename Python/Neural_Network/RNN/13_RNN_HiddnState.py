# ============================================================
# Program 13 : Hidden State Concept
# Target:
# Understand hidden state as memory of RNN
# ============================================================

words = ["food", "was", "not", "good"]

hidden_state = "empty memory"

print("=" * 60)
print("        Marvellous Infosystems")
print("   RNN Applications - Program 13")
print("=" * 60)

print("Target of this Program:")
print("Understand hidden state as RNN memory")
print("-" * 60)

print("Initial Hidden State:", hidden_state)
print("-" * 60)

for index, word in enumerate(words):
    print("Time Step:", index + 1)
    print("Current Word   :", word)
    print("Previous Memory:", hidden_state)

    hidden_state = "memory after reading '" + " ".join(words[:index + 1]) + "'"

    print("Updated Memory :", hidden_state)
    print("-" * 60)

print("Conclusion:")
print("Hidden state stores information from previously read words.")