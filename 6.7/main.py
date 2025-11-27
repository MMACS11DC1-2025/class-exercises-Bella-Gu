import time
t0 = time.time()

from PIL import Image
t1 = time.time()


# def is_target_feature()
    # (e.g. colour channels as RGB tuple inputs) and returns a specific, useful output 
    # (e.g., returns True if the pixel matches your custom feature definition else False, or a weight)

# load image file (import 10 photos)
file1 = Image.open("5.1/filename.jpg")      # 10 images not imported yet
file2 = Image.open("5.1/filename.jpg")
file3 = Image.open("5.1/filename.jpg")
file4 = Image.open("5.1/filename.jpg")
file5 = Image.open("5.1/filename.jpg")
file6 = Image.open("5.1/filename.jpg")
file7 = Image.open("5.1/filename.jpg")
file8 = Image.open("5.1/filename.jpg")
file9 = Image.open("5.1/filename.jpg")
file10 = Image.open("5.1/filename.jpg")

# create a pixel access object for faster pixel manipulation
name_image = file1.load()
name_image = file2.load()
name_image = file3.load()
name_image = file4.load()
name_image = file5.load()
name_image = file6.load()
name_image = file7.load()
name_image = file8.load()
name_image = file9.load()
name_image = file10.load()

# print the RGB values and colour category of the first pixel (top left corner)

# create a list to store the pixels of the specific colour
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




