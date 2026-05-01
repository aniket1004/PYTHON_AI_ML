# ============================================================
# Program 5 : Text to Sequences
# Target:
# Convert complete sentences into numeric sequences
# ============================================================

from tensorflow.keras.preprocessing.text import Tokenizer

sentences = [
    "food was good",
    "food was bad",
    "food was not good"
]

tokenizer = Tokenizer()
tokenizer.fit_on_texts(sentences)

sequences = tokenizer.texts_to_sequences(sentences)

print("=" * 60)
print("        Marvellous Infosystems")
print("   RNN Applications - Program 5")
print("=" * 60)

print("Target of this Program:")
print("Convert each sentence into a sequence of numbers")
print("-" * 60)

print("Word Index:")
print(tokenizer.word_index)
print("-" * 60)

for sentence, sequence in zip(sentences, sequences):
    print("Sentence :", sentence)
    print("Sequence :", sequence)
    print("-" * 60)

print("Conclusion:")
print("A sentence is now represented as a list of word numbers.")