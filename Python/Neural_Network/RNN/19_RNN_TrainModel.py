# ============================================================
# Program 19 : Compile and Train Model
# Target:
# Train RNN model on sentiment dataset
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

print("=" * 60)
print("        Marvellous Infosystems")
print("   RNN Applications - Program 19")
print("=" * 60)

print("Target of this Program:")
print("Compile and train RNN model")
print("-" * 60)

print("Input X:")
print(X)

print("\nOutput y:")
print(y)

print("\nCompile Details:")
print("Optimizer     : Adam")
print("Loss Function : Binary Crossentropy")
print("Metric        : Accuracy")

print("\nTraining Started...")

history = model.fit(X, y, epochs=800, verbose=0)

print("Training Completed")
print("Final Loss    :", history.history["loss"][-1])
print("Final Accuracy:", history.history["accuracy"][-1])