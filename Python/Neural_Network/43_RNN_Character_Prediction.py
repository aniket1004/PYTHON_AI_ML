import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import SimpleRNN, Dense
from tensorflow.keras.utils import to_categorical

def MarvellousCharcterPredictions():

    # 1) Prepare toy text dataset
    text = "hellohellohellohello"   # repeating pattern
    chars = sorted(list(set(text)))  # unique characters
    char_to_int = {c:i for i,c in enumerate(chars)}
    int_to_char = {i:c for i,c in enumerate(chars)}

    print("Unique characters:", chars)

    # 2) Convert text to integer sequence
    encoded = [char_to_int[c] for c in text]

    # 3) Create input-output pairs (sequence length = 3)
    seq_length = 3
    X, y = [], []
    for i in range(len(encoded) - seq_length):
        X.append(encoded[i:i+seq_length])   # e.g. "hel"
        y.append(encoded[i+seq_length])     # next char e.g. "l"

    X = np.array(X)
    y = np.array(y)

    # One-hot encode output
    y = to_categorical(y, num_classes=len(chars))

    # Reshape X for RNN (samples, timesteps, features)
    X = X.reshape((X.shape[0], X.shape[1], 1))

    # 4) Build RNN model
    model = Sequential()
    model.add(SimpleRNN(16, activation="tanh", input_shape=(seq_length, 1)))
    model.add(Dense(len(chars), activation="softmax"))

    model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])

    # 5) Train
    model.fit(X, y, epochs=300, verbose=0)

    # 6) Test prediction
    test_input = ["h","e","l"]  # we expect model to predict "l"
    encoded_input = np.array([[char_to_int[c] for c in test_input]]).reshape((1, seq_length, 1))

    pred = model.predict(encoded_input, verbose=0)
    predicted_char = int_to_char[np.argmax(pred)]

    print("Input:", test_input, "-> Predicted next char:", predicted_char)

def main():
    MarvellousCharcterPredictions()

if __name__ == "__main__":
    main()