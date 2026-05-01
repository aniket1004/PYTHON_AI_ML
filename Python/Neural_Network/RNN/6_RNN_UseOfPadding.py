# ============================================================
# Program 6 : Need of Padding
# Target:
# Understand why equal length input is required for RNN
# ============================================================

sequences = [
    [1, 2, 3],
    [1, 2, 4],
    [1, 2, 5, 3]
]

print("=" * 60)
print("        Marvellous Infosystems")
print("   RNN Applications - Program 6")
print("=" * 60)

print("Target of this Program:")
print("Understand the need of padding")
print("-" * 60)

print("Original Sequences:")
for sequence in sequences:
    print(sequence, "Length:", len(sequence))

print("-" * 60)
print("Problem:")
print("All sequences do not have the same length.")
print("Neural networks require fixed-size input.")

print("-" * 60)
print("Solution:")
print("Add 0 as padding to shorter sequences.")