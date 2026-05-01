# ------------------------------------------------------------
# Marvellous Edge Detection Demo with Animation
# 6x6 Grayscale Image + 3x3 Kernel
# Step-by-step Convolution Visualization
# ------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

# ------------------------------------------------------------
# Function to print matrix in clean format
# ------------------------------------------------------------
def Marvellous_Print_Matrix(title, matrix):
    print("\n" + "-" * 50)
    print(title)
    print("-" * 50)
    print(matrix)

# ------------------------------------------------------------
# Function to draw values inside matrix cells
# ------------------------------------------------------------
def Marvellous_Draw_Values(ax, matrix, text_color="black"):
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            ax.text(j, i, str(matrix[i][j]),
                    ha='center', va='center',
                    fontsize=12, color=text_color, fontweight='bold')

# ------------------------------------------------------------
# Step 1 : Create 6x6 Image
# Top 3 rows = 0
# Bottom 3 rows = 255
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
# Horizontal edge detector
# ------------------------------------------------------------
kernel = np.array([
    [-1, -1, -1],
    [ 0,  0,  0],
    [ 1,  1,  1]
], dtype=int)

Marvellous_Print_Matrix("3x3 Kernel", kernel)

# ------------------------------------------------------------
# Step 3 : Prepare Feature Map
# Output size = (6-3+1) x (6-3+1) = 4x4
# ------------------------------------------------------------
feature_map = np.zeros((4, 4), dtype=int)

# ------------------------------------------------------------
# Step 4 : Move Kernel Step by Step
# ------------------------------------------------------------
for i in range(4):
    for j in range(4):

        # Extract 3x3 region
        region = image[i:i+3, j:j+3]

        # Multiply region with kernel
        multiplied = region * kernel

        # Sum for one output
        result = np.sum(multiplied)

        # Store in feature map
        feature_map[i][j] = result

        # Print detailed output in terminal
        print("\n" + "=" * 60)
        print(f"STEP : Kernel at Row {i} to {i+2}, Column {j} to {j+2}")
        print("=" * 60)
        print("\nCurrent 3x3 Region:")
        print(region)
        print("\nRegion * Kernel:")
        print(multiplied)
        print("\nSum =", result)
        print("\nFeature Map So Far:")
        print(feature_map)

        # ----------------------------------------------------
        # Graphical Visualization
        # ----------------------------------------------------
        fig, axes = plt.subplots(1, 4, figsize=(16, 4))

        # -------------------------
        # 1. Original Image
        # -------------------------
        axes[0].imshow(image, cmap="gray", vmin=0, vmax=255)
        axes[0].set_title("Original Image")
        Marvellous_Draw_Values(axes[0], image)

        # Red box showing current 3x3 region
        rect = Rectangle((j - 0.5, i - 0.5), 3, 3,
                         linewidth=3, edgecolor='red', facecolor='none')
        axes[0].add_patch(rect)
        axes[0].set_xticks(range(6))
        axes[0].set_yticks(range(6))

        # -------------------------
        # 2. Current Region
        # -------------------------
        axes[1].imshow(region, cmap="gray", vmin=0, vmax=255)
        axes[1].set_title("Marvellous Current 3x3 Region")
        Marvellous_Draw_Values(axes[1], region)
        axes[1].set_xticks(range(3))
        axes[1].set_yticks(range(3))

        # -------------------------
        # 3. Kernel
        # -------------------------
        axes[2].imshow(kernel, cmap="gray")
        axes[2].set_title("3x3 Kernel")
        Marvellous_Draw_Values(axes[2], kernel)
        axes[2].set_xticks(range(3))
        axes[2].set_yticks(range(3))

        # -------------------------
        # 4. Feature Map
        # -------------------------
        axes[3].imshow(feature_map, cmap="gray")
        axes[3].set_title("Feature Map So Far")
        Marvellous_Draw_Values(axes[3], feature_map)
        axes[3].set_xticks(range(4))
        axes[3].set_yticks(range(4))

        plt.suptitle(f"Convolution Step | Output at position ({i},{j}) = {result}",
                     fontsize=14, fontweight='bold')
        plt.tight_layout()
        plt.show()

# ------------------------------------------------------------
# Step 5 : Final Feature Map
# ------------------------------------------------------------
print("\n" + "=" * 60)
print("FINAL FEATURE MAP")
print("=" * 60)
print(feature_map)

# ------------------------------------------------------------
# Step 6 : Final Conclusion
# ------------------------------------------------------------
print("\n" + "=" * 60)
print("FINAL Conclusion")
print("=" * 60)
print("1. The top half of image is black (0).")
print("2. The bottom half of image is white (255).")
print("3. The boundary between them is an edge.")
print("4. The kernel moves one step at a time.")
print("5. At each step, region and kernel are multiplied.")
print("6. Their sum becomes one value in the feature map.")
print("7. High values indicate strong edge detection.")