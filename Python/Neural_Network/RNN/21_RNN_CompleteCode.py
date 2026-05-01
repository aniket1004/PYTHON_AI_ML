# ============================================================
# Program 21 : Final Complete RNN Sentiment Application
# Target:
# Combine all steps into one complete RNN application
# ============================================================

import numpy as np

from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, SimpleRNN, Dense

print("=" * 60)
print("        Marvellous Infosystems")
print("   RNN Applications - Program 21")
print("=" * 60)

print("Target of this Program:")
print("Build complete RNN sentiment analysis application")
print("-" * 60)

# Step 1: Dataset
sentences = [
    "food was good",
    "food was bad",
    "food was not good"
]

labels = [1, 0, 0]

# Step 2: Tokenization
tokenizer = Tokenizer()
tokenizer.fit_on_texts(sentences)

# Step 3: Convert text to sequences
sequences = tokenizer.texts_to_sequences(sentences)

# Step 4: Padding
max_length = 4
X = pad_sequences(sequences, maxlen=max_length, padding="pre")

y = np.array(labels)

# Step 5: Vocabulary size
vocab_size = len(tokenizer.word_index) + 1

# Step 6: Build RNN model
model = Sequential()
model.add(Embedding(input_dim=vocab_size, output_dim=8))
model.add(SimpleRNN(units=8, activation="tanh"))
model.add(Dense(1, activation="sigmoid"))
model.build(input_shape=(None, max_length))

# Step 7: Compile model
model.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=["accuracy"]
)

# Step 8: Train model
model.fit(X, y, epochs=800, verbose=0)

# Step 9: Display model summary
print("Model Architecture:")
model.summary()

print("\nWord Index:")
print(tokenizer.word_index)

print("\nTraining Input X:")
print(X)

print("\nTraining Labels y:")
print(y)

# Step 10: Prediction
for text in sentences:
    sequence = tokenizer.texts_to_sequences([text])
    padded = pad_sequences(sequence, maxlen=max_length, padding="pre")
    prediction = model.predict(padded, verbose=0)

    print("\n" + "-" * 60)
    print("Sentence:", text)
    print("Sequence:", sequence[0])
    print("Padded  :", padded[0])
    print("Prediction Value:", prediction[0][0])

    if prediction[0][0] >= 0.5:
        print("Final Sentiment: Positive")
    else:
        print("Final Sentiment: Negative")

print("\nConclusion:")
print("RNN reads words sequentially and uses memory to classify sentiment.")