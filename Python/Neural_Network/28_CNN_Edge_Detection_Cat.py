# ------------------------------------------------------------
# Detect edges using OpenCV
# ------------------------------------------------------------

import cv2

# Load image
img = cv2.imread("sample.png")

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply Canny Edge Detection
edges = cv2.Canny(gray, 100, 200)

# Show Original Image
cv2.imshow("Original Image", img)

# Show Grayscale Image
cv2.imshow("Grayscale Image", gray)

# Show Edge Detected Image
cv2.imshow("Edges", edges)

# Wait until key press
cv2.waitKey(0)
cv2.destroyAllWindows()