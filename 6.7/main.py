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

breads = ["6.7/bread1.png", "6.7/bread2.png", "6.7/bread3.png", "6.7/bread4.png", "6.7/bread5.png", "6.7/bread6.png", "6.7/bread7.png", "6.7/bread8.png", "6.7/bread9.png", "6.7/bread10.png"] # store the files in a list for nested loop

for bread in breads:
    file = Image.open(bread)
    breadImage = file.load()

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
for i in range(len(breads)):
    width = file.width      # get image dimensions
    height = file.height

    for x in range(height):
        for y in range(width):
            pixel_r = (breads[i])[x,y][0]
            pixel_g = (breads[i])[x,y][1]
            pixel_b = (breads[i])[x,y][2]
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

    # calculate "Feature Density Score" for each image (percentage)
    total_burnt = num_mediumbrown + num_darkbrown + num_black # beige and light brown do not count because it is not burnt
    total_bread = num_beige + num_lightbrown + num_mediumbrown + num_darkbrown + num_black # total area of the bread
    burnt_percentage = total_burnt / total_bread * 100

    # print results
        # "based off the colours (medium, black...), your bread #1 is ...% burnt"
    output = "Based off bread " + str[bread] + ", it is {}% burnt.".format(burnt_percentage)
    

    #  *UNIT 6* implement the Selection Sort algorithm function *yourself* (not using built-in libraries for sorting)
        # sort the master list based on the calculated Feature Density Score (highest to lowest)

    #  *UNIT 6* implement the Binary Search algorithm function *yourself* to search the sorted list for a specific target score

t3 = time.time()

# code profiling (timings to 3 decimal places)
module_load = t1 - t0
image_open_load = t2 - t1
loop = t3 - t2
entire = t3 - t0
timings = "It took {:.3f}s to import PIL, {:.3f}s to load the image, and {:.3f}s to do the loop. All in all it took {:.3f}s.".format(module_load, image_open_load, loop, entire)
print(timings)