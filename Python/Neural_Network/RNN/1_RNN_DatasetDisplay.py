# ============================================================
# Program 1 : Dataset and Labels
# Target:
# Understand training data and output labels used for RNN
# ============================================================

sentences = [
    "food was good",
    "food was bad",
    "food was not good"
]

labels = [1, 0, 0]

print("=" * 60)
print("        Marvellous Infosystems")
print("   RNN Applications - Program 1")
print("=" * 60)

print("Target of this Program:")
print("Understand input dataset and sentiment labels")
print("-" * 60)

for sentence, label in zip(sentences, labels):
    sentiment = "Positive" if label == 1 else "Negative"

    print("Sentence :", sentence)
    print("Label    :", label)
    print("Meaning  :", sentiment)
    print("-" * 60)