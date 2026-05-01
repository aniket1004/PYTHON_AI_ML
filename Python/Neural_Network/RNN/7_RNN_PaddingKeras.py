# ============================================================
# Program 7 : Padding using Keras
# Target:
# Use pad_sequences to make all sentence sequences equal length
# ============================================================

from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

sentences = [
    "food was good",
    "food was bad",
    "food was not good"
]

tokenizer = Tokenizer()
tokenizer.fit_on_texts(sentences)

sequences = tokenizer.texts_to_sequences(sentences)

max_length = 4

padded_sequences = pad_sequences(
    sequences,
    maxlen=max_length,
    padding="pre"
)

print("=" * 60)
print("        Marvellous Infosystems")
print("   RNN Applications - Program 7")
print("=" * 60)

print("Target of this Program:")
print("Apply padding to make all sequences length 4")
print("-" * 60)

print("Maximum Length:", max_length)
print("Padding Type   : pre")
print("Padding Value  : 0")
print("-" * 60)

for sentence, sequence, padded in zip(sentences, sequences, padded_sequences):
    print("Sentence          :", sentence)
    print("Original Sequence :", sequence)
    print("Padded Sequence   :", padded)
    print("-" * 60)