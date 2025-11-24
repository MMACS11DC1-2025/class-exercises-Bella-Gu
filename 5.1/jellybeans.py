from PIL import Image

def colour(r, g, b):
    if r > 150 and g > 150 and b < 150:
        return "yellow"   # high red and green, low blue
    elif r > 160 and g > 0 and b > 1:
        return "red"      # high red, some green and blue
    elif r > 15 and g > 90 and b > 15:
        return "green"    # some green, some red and blue
    elif r > 45 and g > 55 and b > 180:
        return "blue"     # high blue, some red and green
    elif r > 210 and g > 110 and b > 10:
        return "orange"   # very high red, high green, low blue
    else:
        return "other"    # doesnt match any specific colour criteria
   
# Load the image file
file = Image.open("5.1/jelly_beans.jpg")
# Create a pixel access object for faster pixel manipulation
jb_image = file.load()

# Print the RGB values and colour category of the first pixel (top-left corner)
print(jb_image[0,0])
print(colour(jb_image[0,0][0], jb_image[0,0][1], jb_image[0,0][2]))

# create a list to store the pixels of the specific colour
yellow_pixels = []
red_pixels = []
green_pixels = []
blue_pixels = []
orange_pixels = []
other_pixels = []  # dor pixels that dont match any specific colour category

# get image dimensions
width = file.width
height = file.height

# iterate through every pixel in the image (go through all the pixels in the image)
for x in range(width):
    for y in range(height):
        pixel_r = jb_image[x,y][0]
        pixel_g = jb_image[x,y][1]
        pixel_b = jb_image[x,y][2]

        # determine what colour category this pixel belongs to
        color_type = colour(pixel_r, pixel_g, pixel_b)
        
        # Process pixel based on its colour category
        if color_type == "yellow":
            yellow_pixels.append(jb_image[x,y])      # store original pixel
            file.putpixel((x,y), (255, 255, 255))   # replace with white (vice versa for the rest of the colours)

        elif color_type == "red":
            red_pixels.append(jb_image[x,y])
            file.putpixel((x,y), (255, 255, 255))

        elif color_type == "green":
            green_pixels.append(jb_image[x,y])
            file.putpixel((x,y), (255, 255, 255))

        elif color_type == "blue":
            blue_pixels.append(jb_image[x,y])
            file.putpixel((x,y), (255, 255, 255))

        elif color_type == "orange":
            orange_pixels.append(jb_image[x,y])
            file.putpixel((x,y), (255, 255, 255))

        else:
            other_pixels.append(jb_image[x,y])

# calculate pixel counts for each colour
num_yellow = len(yellow_pixels)
num_red = len(red_pixels)
num_green = len(green_pixels)
num_blue = len(blue_pixels)
num_orange = len(orange_pixels)
num_other = len(other_pixels)
total_pixels = width * height

file.save("output.png", "png")

# calculate the ratio of each colour to total pixels
yellow_ratio = num_yellow / total_pixels
red_ratio = num_red / total_pixels
green_ratio = num_green / total_pixels
blue_ratio = num_blue / total_pixels
orange_ratio = num_orange / total_pixels
other_ratio = num_other / total_pixels

# print results
print(f"Yellow pixels: {len(yellow_pixels)}")
print(f"Red pixels: {len(red_pixels)}")
print(f"Green pixels: {len(green_pixels)}")
print(f"Blue pixels: {len(blue_pixels)}")
print(f"Orange pixels: {len(orange_pixels)}")
print(f"Other pixels: {len(other_pixels)}")
print(f"Total pixels: {width * height}")