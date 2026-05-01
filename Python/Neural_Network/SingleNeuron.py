import numpy as np

#-----------------------------------------
# Step 1 : Define Input Features
#-----------------------------------------
# These are the inputs coming to the neuron (x1, x2, x3)
# Example : could be marks, pixel values, or any features

inputs = np.array([2.0, 3.0, 4.0])

#-----------------------------------------
# Step 2 : Define Weights
#-----------------------------------------
# Each input has a corresponding weight (w1, w2, w3)
# Weights represent importance of each input

weights = np.array([0.5, 0.3, 0.2])

#-----------------------------------------
# Step 3 : Define Bias
#-----------------------------------------
# Bias is an additional parameter that helps shift the output
# It allows the model to fit data better

bias = 1.0

#-----------------------------------------
# Step 4 : Calculate Weighted Sum (Z)
#-----------------------------------------
# Formula :
# Z = (x1 * w1 + x2 * w2 + x3 * w3) + bias
# Using numpy dot product for efficient calculation

weighted_sum = np.dot(inputs, weights) + bias

# Manual calculation :
# (2.0 * 0.5) + (3.0 * 0.3) + (4.0 * 0.2) + 1.0
# = 1.0 + 0.9 + 0.8 + 1.0 = 3.7

#-----------------------------------------
# Step 5 : Activation Function (ReLU)
#-----------------------------------------
# ReLU (Rectified Linear Unit):
# If value > 0 -> return value
# IF value < 0 -> return 0

def relu(x):
    return max(0, x)

#-----------------------------------------
# Step 6 : Final Output
#-----------------------------------------
# Pass the weighted sum through activation function

output = relu(weighted_sum)

#-----------------------------------------
# Step 7 : Display Results
#-----------------------------------------

print("Inputs : ", inputs)
print("Weights : ", weights)
print("Bias : ", bias)
print("Weighted Sum(Z) : ", weighted_sum)
print("Final Output : ", output)
