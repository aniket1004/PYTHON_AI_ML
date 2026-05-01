# ============================================================
# Program 12 : Time Steps Explanation
# Target:
# Understand how RNN reads text at different time steps
# ============================================================

sentence = "food was not good"

words = sentence.split()

print("=" * 60)
print("        Marvellous Infosystems")
print("   RNN Applications - Program 12")
print("=" * 60)

print("Target of this Program:")
print("Understand time steps in RNN")
print("-" * 60)

print("Sentence:", sentence)
print("-" * 60)

for index, word in enumerate(words):
    print("Time Step", index + 1, ":", word)

print("-" * 60)
print("Conclusion:")
print("RNN reads one word at one time step.")