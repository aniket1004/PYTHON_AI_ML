import tensorflow as tf

print("----- Marvellous Matrix Multiplication Example -----")

# Create two matrices
matrix1 = tf.constant([
    [1, 2],
    [3, 4]
], dtype=tf.float32)

matrix2 = tf.constant([
    [5, 6],
    [7, 8]
], dtype=tf.float32)

print("Matrix 1:")
print(matrix1)
print()

print("Matrix 2:")
print(matrix2)
print()

# Matrix multiplication
result = tf.matmul(matrix1, matrix2)

print("Matrix Multiplication Result:")
print(result)