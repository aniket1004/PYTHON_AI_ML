# ============================================================
# Program 8 : Vocabulary Size
# Target:
# Calculate vocabulary size required for Embedding layer
# ============================================================

from tensorflow.keras.preprocessing.text import Tokenizer

sentences = [
    "food was good",
    "food was bad",
    "food was not good"
]

tokenizer = Tokenizer()
tokenizer.fit_on_texts(sentences)

word_index = tokenizer.word_index

vocab_size = len(word_index) + 1

print("=" * 60)
print("        Marvellous Infosystems")
print("   RNN Applications - Program 8")
print("=" * 60)

print("Target of this Program:")
print("Understand vocabulary size calculation")
print("-" * 60)

print("Word Index:")
print(word_index)
print("-" * 60)

print("Number of Unique Words:", len(word_index))
print("Padding Index          : 0")
print("Vocabulary Size        :", vocab_size)

print("-" * 60)
print("Formula:")
print("vocab_size = number_of_unique_words + 1")
print("vocab_size =", len(word_index), "+ 1 =", vocab_size)