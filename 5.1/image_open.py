# from PIL import Image
from PIL import Image
import coolcolours

image_green = Image.open("5.1/kid-green.jpg").load()
image_beach = Image.open("5.1/beach.jpg").load()

"""
def colour(r, g, b):
    if r <= 24 and g <= 255 and b <= 24:
        return ("green")
    if r <= 24 and g <= 24 and b <= 255:
        return("blue")
    if r <= 255 and g <= 24 and b <= 24:
        return("red")
    
print(colour(0, 255, 0)) # green
print(colour(0, 0, 255)) # blue
print(colour(255, 0, 0)) # red
"""
image_output = Image.open("5.1/kid-green.jpg")

width = image_output.width
height = image_output.height

for i in range(width):
    for j in range(height):
        r = image_green[i, j][0]
        g = image_green[i, j][1]
        b = image_green[i, j][2]

        if coolcolours.is_green(r, g, b):
            beach_colour = image_beach[i, j]
            image_output.putpixel((i, j), beach_colour)
image_output.save("output.png", "png")