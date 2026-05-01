# ------------------------------------------------------------
# Read Colored Image and Display Output
# ------------------------------------------------------------

from PIL import Image
import numpy as np

# Load image
img = Image.open("color.png")

# Resize image to 28x28
img = img.resize((28,28))

# Convert image into numpy array
pixels = np.array(img)

# ------------------------------------------------------------
# Basic Information
# ------------------------------------------------------------
print("\n---------------------------------")
print("IMAGE INFORMATION")
print("---------------------------------")

print("Image Shape :", pixels.shape)
print("Height      :", pixels.shape[0], "Rows")
print("Width       :", pixels.shape[1], "Columns")
print("Channels    :", pixels.shape[2], "(R,G,B)")

total_pixels = pixels.shape[0] * pixels.shape[1]
print("Total Pixels:", total_pixels)

# ------------------------------------------------------------
# Display Sample Pixel Values
# ------------------------------------------------------------
print("\n---------------------------------")
print("SAMPLE PIXEL VALUES")
print("---------------------------------")

print("Pixel[0][0]   =", pixels[0][0])
print("Pixel[5][10]  =", pixels[5][10])
print("Pixel[10][10] =", pixels[10][10])
print("Pixel[15][15] =", pixels[15][15])
print("Pixel[20][20] =", pixels[20][20])

# ------------------------------------------------------------
# Explain One Pixel
# ------------------------------------------------------------
print("\n---------------------------------")
print("PIXEL MEANING")
print("---------------------------------")

r = pixels[10][10][0]
g = pixels[10][10][1]
b = pixels[10][10][2]

print("Pixel[10][10] contains:")
print("Red   =", r)
print("Green =", g)
print("Blue  =", b)

# ------------------------------------------------------------
# Full Matrix
# ------------------------------------------------------------
print("\n---------------------------------")
print("FIRST 5 ROWS OF IMAGE MATRIX")
print("---------------------------------")

print(pixels[:5])

print("\n---------------------------------")
print("FINAL UNDERSTANDING")
print("---------------------------------")
print("Image = Collection of Pixels")
print("Each Pixel = [R,G,B]")
print("Computer sees image as numbers")
print("CNN uses these numbers as input")