from PIL import Image, ImageDraw

width = 500
height = 500

img = Image.new('RGB', (width, height))

draw = ImageDraw.Draw(img)


draw.rectangle(((0, 0), (width, height)), fill="white")

color = (256, 128, 128)
draw.line((250, 100, 250, 300), fill=color)
draw.line((200, 250, 300, 250), fill=color)
draw.line((250, 300, 200, 350), fill=color)
draw.line((250, 300, 300, 350), fill=color)

draw.rectangle(((200, 100), (300, 200)), fill="lightblue")

img.show()