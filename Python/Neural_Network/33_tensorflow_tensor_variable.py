import tensorflow as tf

print("----- Marvellous TensorFlow Variable Example -----")

# Create a variable
weight = tf.Variable(5.0)

print("Initial Weight Value:")
print(weight.numpy())
print()

# Update variable value
weight.assign(10.0)
print("Updated Weight Value:")
print(weight.numpy())
print()

# Add value to variable
weight.assign_add(2.5)
print("After assign_add(2.5):")
print(weight.numpy())
print()

# Subtract value from variable
weight.assign_sub(1.5)
print("After assign_sub(1.5):")
print(weight.numpy())