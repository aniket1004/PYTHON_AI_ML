import tensorflow as tf

print("----- Marvellous TensorFlow Tensor Creation Example -----")

# Scalar tensor (single value)
scalar_tensor = tf.constant(10)
print("Scalar Tensor:")
print(scalar_tensor)
print()

# 1D tensor (vector)
vector_tensor = tf.constant([10, 20, 30, 40])
print("1D Tensor / Vector:")
print(vector_tensor)
print()

# 2D tensor (matrix)
matrix_tensor = tf.constant([
    [1, 2, 3],
    [4, 5, 6]
])
print("2D Tensor / Matrix:")
print(matrix_tensor)
print()

# 3D tensor
tensor_3d = tf.constant([
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
])
print("3D Tensor:")
print(tensor_3d)
print()

# Show shape of tensors
print("Shape of scalar tensor:", scalar_tensor.shape)
print("Shape of vector tensor:", vector_tensor.shape)
print("Shape of matrix tensor:", matrix_tensor.shape)
print("Shape of 3D tensor:", tensor_3d.shape)