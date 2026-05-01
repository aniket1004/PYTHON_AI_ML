# ============================================================
# Program 18 : Build RNN Architecture
# Target:
# Create Embedding + SimpleRNN + Dense model architecture
# ============================================================

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, SimpleRNN, Dense

vocab_size = 6
max_length = 4

model = Sequential()

model.add(Embedding(
    input_dim=vocab_size,
    output_dim=8
))

model.add(SimpleRNN(
    units=8,
    activation="tanh",
    return_sequences=False
))

model.add(Dense(
    1,
    activation="sigmoid"
))

model.build(input_shape=(None, max_length))

print("=" * 60)
print("        Marvellous Infosystems")
print("   RNN Applications - Program 18")
print("=" * 60)

print("Target of this Program:")
print("Build RNN model architecture")
print("-" * 60)

model.summary()

print("\nArchitecture Flow:")
print("Input Sentence")
print("-> Tokenization")
print("-> Padding")
print("-> Embedding Layer")
print("-> SimpleRNN Layer")
print("-> Dense Layer")
print("-> Sigmoid Output")