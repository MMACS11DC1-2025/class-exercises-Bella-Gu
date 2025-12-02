import time
t0 = time.time()

from PIL import Image
t1 = time.time()


# def is_target_feature()
    # (e.g. colour channels as RGB tuple inputs) and returns a specific, useful output 
    # (e.g., returns True if the pixel matches your custom feature definition else False, or a weight)

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

# print the RGB values and colour category of the first pixel (top left corner)

# create a list to store the pixels of the specific colour
beige_pixels = []
lightbrown_pixels = []
mediumbrown_pixels = []
darkbrown_pixels = []
black_pixels = []
other_pixels = [] # for pixels that don't match any category (eg. white background)

t2 = time.time()
# get image dimensions

# iterate through every pixel in the image (go through all the pixels in the image)
    # calculate "Feature Density Score" for each image 
t3 = time.time()

# calculate pixel counts for each colour
file.save("output.png", "png") # ??? redo

# print results

# code profiling (timings to 3 decimal places)
module_load = t1-t0
image_open_load = t2-t1
loop = t3-t2
entire = t3-t0
timings = "It took {:.3f}s to import PIL, {:.3f}s to load the image, and {:.3f}s to do the loop. All in all it took {:.3f}s.".format(module_load, image_open_load, loop, entire)
print(timings)