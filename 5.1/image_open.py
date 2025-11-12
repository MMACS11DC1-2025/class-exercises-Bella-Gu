# from PIL import Image

# image_green = Image.open("CS11/5.1/kid-green.jpg").load()
# image_beach = Image.open("CS11/5.1/beach.jpg").load()

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