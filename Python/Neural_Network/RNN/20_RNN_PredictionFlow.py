# ============================================================
# Program 20 : Prediction Flow
# Target:
# Show complete prediction process for a new sentence
# ============================================================

import numpy as np

from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, SimpleRNN, Dense

sentences = [
    "food was good",
    "food was bad",
    "food was not good"
]

labels = [1, 0, 0]

tokenizer = Tokenizer()
tokenizer.fit_on_texts(sentences)

sequences = tokenizer.texts_to_sequences(sentences)

max_length = 4
X = pad_sequences(sequences, maxlen=max_length, padding="pre")
y = np.array(labels)

vocab_size = len(tokenizer.word_index) + 1

model = Sequential()
model.add(Embedding(input_dim=vocab_size, output_dim=8))
model.add(SimpleRNN(units=8, activation="tanh"))
model.add(Dense(1, activation="sigmoid"))
model.build(input_shape=(None, max_length))

model.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=["accuracy"]
)

model.fit(X, y, epochs=800, verbose=0)

print("=" * 60)
print("        Marvellous Infosystems")
print("   RNN Applications - Program 20")
print("=" * 60)

print("Target of this Program:")
print("Understand prediction flow step by step")
print("-" * 60)


def Predict_Sentiment(text):
    print("\n" + "=" * 70)
    print("PREDICTION PROCESS")
    print("=" * 70)

    print("Input Sentence:", text)

    sequence = tokenizer.texts_to_sequences([text])

    print("\nStep 1: Text to Sequence")
    print("Sequence:", sequence[0])

    print("\nStep 2: Word Mapping")
    for word in text.split():
        print(f"{word:10s} ---> {tokenizer.word_index[word]}")

    padded_sequence = pad_sequences(sequence, maxlen=max_length, padding="pre")

    print("\nStep 3: Padding")
    print("Padded Sequence:", padded_sequence[0])

    prediction = model.predict(padded_sequence, verbose=0)

    print("\nStep 4: Sigmoid Output")
    print("Prediction Value:", prediction[0][0])

    print("\nStep 5: Final Decision")
    if prediction[0][0] >= 0.5:
        print("Since value >= 0.5")
        print("Sentiment: Positive")
    else:
        print("Since value < 0.5")
        print("Sentiment: Negative")


Predict_Sentiment("food was good")
Predict_Sentiment("food was bad")
Predict_Sentiment("food was not good")