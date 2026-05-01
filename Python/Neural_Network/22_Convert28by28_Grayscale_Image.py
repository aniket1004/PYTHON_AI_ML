from PIL import Image

img = Image.open("digit.png")
img = img.convert("L")      # grayscale
img = img.resize((28,28))

img.save("digit_28x28.png")

print(img.size)