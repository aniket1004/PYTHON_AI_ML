import tensorflow as tf

print("----- Marvellous Single Neuron Example -----")

# Input values
inputs = tf.constant([1.0, 2.0, 3.0])

# Weights
weights = tf.constant([0.5, -0.2, 0.8])

# Bias
bias = tf.constant(0.1)

# Weighted sum
weighted_sum = tf.reduce_sum(inputs * weights) + bias

# Activation function (Sigmoid)
output = tf.sigmoid(weighted_sum)

print("Inputs:", inputs.numpy())
print("Weights:", weights.numpy())
print("Bias:", bias.numpy())
print("Weighted Sum:", weighted_sum.numpy())
print("Neuron Output after Sigmoid:", output.numpy())