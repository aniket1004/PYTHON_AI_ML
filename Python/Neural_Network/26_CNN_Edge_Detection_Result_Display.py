# ------------------------------------------------------------
# Marvellous Convolution Demo with Visualization
# 6x6 Grayscale Image
# Top 3 rows = 0
# Bottom 3 rows = 255
# 3x3 Kernel detects horizontal edge
# Shows:
# 1. Input image
# 2. Current 3x3 region
# 3. Multiplication result
# 4. Feature map building step by step
# ------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt

# ------------------------------------------------------------
# Function to print matrix nicely
# ------------------------------------------------------------
def Marvellous_Print_Matrix(title, matrix):
    print("\n" + "-" * 50)
    print(title)
    print("-" * 50)
    print(matrix)

# ------------------------------------------------------------
# Step 1 : Create 6x6 Grayscale Image
# ------------------------------------------------------------
image = np.array([
    [0,   0,   0,   0,   0,   0],
    [0,   0,   0,   0,   0,   0],
    [0,   0,   0,   0,   0,   0],
    [255, 255, 255, 255, 255, 255],
    [255, 255, 255, 255, 255, 255],
    [255, 255, 255, 255, 255, 255]
], dtype=int)

Marvellous_Print_Matrix("Original 6x6 Image", image)

# ------------------------------------------------------------
# Step 2 : Create 3x3 Kernel
# This kernel detects horizontal edges
# ------------------------------------------------------------
kernel = np.array([
    [-1, -1, -1],
    [ 0,  0,  0],
    [ 1,  1,  1]
], dtype=int)

Marvellous_Print_Matrix("3x3 Edge Detection Kernel", kernel)

# ------------------------------------------------------------
# Step 3 : Prepare Feature Map
# Output size = (6-3+1) x (6-3+1) = 4x4
# ------------------------------------------------------------
feature_map = np.zeros((4, 4), dtype=int)

# ------------------------------------------------------------
# Step 4 : Convolution Operation Step by Step
# ------------------------------------------------------------
for i in range(4):
    for j in range(4):
        print("\n\n==================================================")
        print(f"Kernel Position -> Row: {i} to {i+2}, Column: {j} to {j+2}")
        print("==================================================")

        # Extract 3x3 region from image
        region = image[i:i+3, j:j+3]

        Marvellous_Print_Matrix("Current 3x3 Region from Image", region)

        # Element-wise multiplication
        multiplied = region * kernel
        Marvellous_Print_Matrix("Region * Kernel", multiplied)

        # Sum all elements
        result = np.sum(multiplied)
        print("\nSum of all values =", result)

        # Store in feature map
        feature_map[i][j] = result

        Marvellous_Print_Matrix("Feature Map Built So Far", feature_map)

# ------------------------------------------------------------
# Step 5 : Final Feature Map
# ------------------------------------------------------------
Marvellous_Print_Matrix("Final Feature Map", feature_map)

# ------------------------------------------------------------
# Step 6 : Graphical Visualization
# ------------------------------------------------------------
plt.figure(figsize=(6, 6))
plt.imshow(image, cmap="gray", vmin=0, vmax=255)
plt.title("Original 6x6 Grayscale Image")
plt.colorbar()
plt.show()

plt.figure(figsize=(4, 4))
plt.imshow(kernel, cmap="gray")
plt.title("3x3 Kernel")
plt.colorbar()
plt.show()

plt.figure(figsize=(5, 5))
plt.imshow(feature_map, cmap="gray")
plt.title("Feature Map After Edge Detection")
plt.colorbar()
plt.show()

# ------------------------------------------------------------
# Step 7 : Final Understanding
# ------------------------------------------------------------
print("\n" + "=" * 60)
print("FINAL UNDERSTANDING")
print("=" * 60)
print("1. Original image has top black area and bottom white area.")
print("2. This sudden change creates an edge.")
print("3. Kernel moves over the image one step at a time.")
print("4. At each position, region and kernel are multiplied.")
print("5. Sum of multiplication gives one output value.")
print("6. High value means strong edge detected.")
print("7. All output values together form the feature map.")