import tensorflow as tf

print("-----Marvellous Tensor Operations Example -----")

tensor1 = tf.constant([10, 20, 30])
tensor2 = tf.constant([1, 2, 3])

# Addition
addition_result = tf.add(tensor1, tensor2)
print("Addition:", addition_result)

# Subtraction
subtraction_result = tf.subtract(tensor1, tensor2)
print("Subtraction:", subtraction_result)

# Multiplication
multiplication_result = tf.multiply(tensor1, tensor2)
print("Multiplication:", multiplication_result)

# Division
division_result = tf.divide(tensor1, tensor2)
print("Division:", division_result)

# Square
square_result = tf.square(tensor1)
print("Square:", square_result)

# Reduce sum
sum_result = tf.reduce_sum(tensor1)
print("Sum of tensor1:", sum_result)

# Reduce mean
mean_result = tf.reduce_mean(tf.cast(tensor1, tf.float32))
print("Mean of tensor1:", mean_result)