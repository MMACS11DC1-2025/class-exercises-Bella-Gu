import time
t0 = time.time()

from PIL import Image
t1 = time.time()


# def is_target_feature()
    # (e.g. colour channels as RGB tuple inputs) and returns a specific, useful output 
        # (e.g., returns True if the pixel matches your custom feature definition else False, or a weight)
def is_target_feature(r, g, b):
    if r > 230 and g > 230 and b > 230:
            return "white"                  # white background (edit)
    if r > 235 and b > 214 and b > 183:
        return "beige"
    elif r > 224 and g > 173 and b > 89:
        return "lightbrown"
    elif r > 166 and g > 88 and b > 26:
        return "mediumbrown"
    elif r > 107 and g > 39 and b > 0:
        return "darkbrown"
    elif r > 107 and g > 39 and b > 0:
        return "black"
    else:
        return "other"

# load image files (import 10 photos)
file1 = Image.open("6.7/bread1.jpg")
file2 = Image.open("6.7/bread2.jpg")
file3 = Image.open("6.7/bread3.jpg")
file4 = Image.open("6.7/bread4.jpg")
file5 = Image.open("6.7/bread5.jpg")
file6 = Image.open("6.7/bread6.jpg")
file7 = Image.open("6.7/bread7.jpg")
file8 = Image.open("6.7/bread8.jpg")
file9 = Image.open("6.7/bread9.jpg")
file10 = Image.open("6.7/bread10.jpg")

# create a pixel access object for faster pixel manipulation
bread1 = file1.load()
bread2 = file2.load()
bread3 = file3.load()
bread4 = file4.load()
bread5 = file5.load()
bread6 = file6.load()
bread7 = file7.load()
bread8 = file8.load()
bread9 = file9.load()
bread10 = file10.load()

breads = [bread1, bread2, bread3, bread4, bread5, bread6, bread7, bread8, bread9, bread10]

# create a list to store the pixels of the specific colour
beige_pixels = []
lightbrown_pixels = []
mediumbrown_pixels = []
darkbrown_pixels = []
black_pixels = []
other_pixels = [] # for pixels that don't match any category (eg. white background)

t2 = time.time()
# get image dimensions thtrhrthhtr

# iterate through every pixel in the image (go through all the pixels in the image)
    # calculate "Feature Density Score" for each image (percentage)
for bread in range(breads):
    width = bread[bread].width      # get image dimensions
    height = bread[bread].height

    for x in range(height):
        for y in range(width):
            pixel_r = bread[x,y][0]
            pixel_g = bread[x,y][1]
            pixel_b = bread[x,y][2]
            colour_type = is_target_feature(pixel_r, pixel_g, pixel_b)  # determine what colour category this pixel belongs to

            # process pixel based on its colour category
            if colour_type == "white":
                other_pixels.append(bread[x,y])      # store original pixel
            elif colour_type == "beige":
                beige_pixels.append(bread[x,y])
            elif colour_type == "lightbrown":
                lightbrown_pixels.append(bread[x,y])
            elif colour_type == "mediumbrown":
                mediumbrown_pixels.append(bread[x,y])
            elif colour_type == "darkbrown":
                darkbrown_pixels.append(bread[x,y])
            elif colour_type == "black":
                black_pixels.append(bread[x,y])

    # calculate pixel counts for each colour
    num_other = len(other_pixels)
    num_beige = len(beige_pixels)
    num_lightbrown = len(lightbrown_pixels)
    num_mediumbrown = len(mediumbrown_pixels)
    num_darkbrown = len(darkbrown_pixels)
    num_black = len(black_pixels)
    total_pixels = width * height

    file[bread].save rgergergergregergregre

    # calculate "Feature Density Score" for each image (percentage)
    other_ratio = num_other / total_pixels * 100
    beige_ratio = num_beige / total_pixels * 100
    lightbrown_ratio = num_lightbrown / total_pixels * 100
    mediumbrown_ratio = num_mediumbrown / total_pixels * 100
    darkbrown_ratio = num_darkbrown / total_pixels * 100
    black_ratio = num_black / total_pixels * 100

    # print results
        # "based off the colours (medium, black...), your bread is ...% burnt"

    # implement the Selection Sort algorithm function *yourself* (not using built-in libraries for sorting)
        # sort the master list based on the calculated Feature Density Score (highest to lowest)

    # implement the Binary Search algorithm function *yourself* to search the sorted list for a specific target score

t3 = time.time()

# calculate pixel counts for each colour gywefuhisdklmn
file.save("output.png", "png") # ??? redo

# print results bfdvcsbdf

# code profiling (timings to 3 decimal places)
module_load = t1 - t0
image_open_load = t2 - t1
loop = t3 - t2
entire = t3 - t0
timings = "It took {:.3f}s to import PIL, {:.3f}s to load the image, and {:.3f}s to do the loop. All in all it took {:.3f}s.".format(module_load, image_open_load, loop, entire)
print(timings)