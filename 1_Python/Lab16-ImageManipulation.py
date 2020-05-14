from PIL import Image
img = Image.open("Documents/airborne.png")
width, height = img.size
pixels = img.load()

for i in range(width):
    for j in range(height):
        r, g, b = pixels[i, j]

        pixels[i, j] = (255-r, 255-g, 255-b)

img.show()