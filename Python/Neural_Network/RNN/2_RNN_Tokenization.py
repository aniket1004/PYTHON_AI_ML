# ============================================================
# Program 2 : Split Sentence into Words
# Target:
# Understand that RNN reads text word by word in sequence
# ============================================================

sentence = "food was not good"

words = sentence.split()

print("=" * 60)
print("        Marvellous Infosystems")
print("   RNN Applications - Program 2")
print("=" * 60)

print("Target of this Program:")
print("Split sentence into individual words")
print("-" * 60)

print("Original Sentence:", sentence)
print("Total Words:", len(words))
print("-" * 60)

for index, word in enumerate(words):
    print("Position", index + 1, ":", word)

print("-" * 60)
print("Conclusion:")
print("RNN processes sentence one word at a time.")