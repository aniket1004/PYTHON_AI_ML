# ============================================================
# Program 10 : Manual Embedding Concept
# Target:
# Understand how tokens can be represented as numeric vectors
# ============================================================

embedding = {
    0: [0.0, 0.0, 0.0],   # padding
    1: [0.2, 0.4, 0.1],   # food
    2: [0.3, 0.1, 0.5],   # was
    3: [0.8, 0.7, 0.9],   # good
    4: [0.1, 0.2, 0.9],   # bad
    5: [0.9, 0.3, 0.2]    # not
}

sequence = [1, 2, 5, 3]

print("=" * 60)
print("        Marvellous Infosystems")
print("   RNN Applications - Program 10")
print("=" * 60)

print("Target of this Program:")
print("Understand embedding as vector representation of words")
print("-" * 60)

print("Sequence for 'food was not good':", sequence)
print("-" * 60)

for token in sequence:
    print("Token :", token)
    print("Vector:", embedding[token])
    print("-" * 60)

print("Conclusion:")
print("Embedding converts every word token into a numeric vector.")