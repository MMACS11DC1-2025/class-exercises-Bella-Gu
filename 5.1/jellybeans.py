from PIL import Image
import jellybeans

jelly = Image.open("5.1/jelly_beans.jpg")

width = image_output.width
height = image_output.height

for x in range(width):
    for y in range(height):
        r = jelly[x, y][0]
        g = jelly[x, y][1]
        b = jelly[x, y][2]

        if coolcolours.colour(r, g, b) == "yellow":
            image_output.putpixel((x, y), (255, 255, 255))
image.output.save("output.png", "png")