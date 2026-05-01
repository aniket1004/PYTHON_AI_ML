# ============================================================
# Program 3 : Manual Vocabulary Creation
# Target:
# Understand vocabulary and word index creation manually
# ============================================================

sentences = [
    "food was good",
    "food was bad",
    "food was not good"
]

vocabulary = []

print("=" * 60)
print("        Marvellous Infosystems")
print("   RNN Applications - Program 3")
print("=" * 60)

print("Target of this Program:")
print("Create vocabulary manually from sentences")
print("-" * 60)

for sentence in sentences:
    words = sentence.split()

    for word in words:
        if word not in vocabulary:
            vocabulary.append(word)

print("Vocabulary List:")
print(vocabulary)
print("-" * 60)

print("Manual Word Index:")
for index, word in enumerate(vocabulary, start=1):
    print(f"{word:10s} ---> {index}")

print("-" * 60)
print("Conclusion:")
print("Vocabulary contains all unique words from dataset.")