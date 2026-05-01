import tensorflow as tf

print("----- Marvellous Tensor Reshape Example -----")

# Create 1D tensor with 12 values
original_tensor = tf.constant([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

print("Original Tensor:")
print(original_tensor)
print("Original Shape:", original_tensor.shape)
print()

# Reshape into 3 rows and 4 columns
reshaped_tensor = tf.reshape(original_tensor, (3, 4))

print("Reshaped Tensor (3x4):")
print(reshaped_tensor)
print("New Shape:", reshaped_tensor.shape)
print()

# Reshape into 2x2x3
reshaped_3d = tf.reshape(original_tensor, (2, 2, 3))

print("Reshaped Tensor (2x2x3):")
print(reshaped_3d)
print("New Shape:", reshaped_3d.shape)