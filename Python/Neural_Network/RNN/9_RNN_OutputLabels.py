# ============================================================
# Program 9 : Output Labels
# Target:
# Understand binary classification labels 0 and 1
# ============================================================

sentences = [
    "food was good",
    "food was bad",
    "food was not good"
]

labels = [1, 0, 0]

print("=" * 60)
print("        Marvellous Infosystems")
print("   RNN Applications - Program 9")
print("=" * 60)

print("Target of this Program:")
print("Understand output labels for sentiment classification")
print("-" * 60)

for sentence, label in zip(sentences, labels):
    print("Sentence :", sentence)
    print("Label    :", label)

    if label == 1:
        print("Meaning  : Positive Sentiment")
    else:
        print("Meaning  : Negative Sentiment")

    print("-" * 60)

print("Conclusion:")
print("This is binary classification: 1 = Positive, 0 = Negative")