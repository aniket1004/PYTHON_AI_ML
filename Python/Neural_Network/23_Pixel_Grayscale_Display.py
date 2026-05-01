from PIL import Image
import numpy as np

# Load image
img = Image.open("digit_28x28.png")      # Your image name
img = img.convert("L")            # Convert to grayscale
img = img.resize((28,28))         # Resize to 28x28

# Convert image into numpy array
pixels = np.array(img)

# Print shape
print("Image Size :", pixels.shape)

# Print pixel values
print("\nPixel Values:\n")
print(pixels)

# 0 → pure black
# 50 → dark gray
# 120 → medium gray
# 200 → light gray
# 255 → pure white