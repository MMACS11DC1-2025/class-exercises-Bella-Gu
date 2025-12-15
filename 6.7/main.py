import time
t0 = time.time()

from PIL import Image
t1 = time.time()

# def is_target_feature()
    # (e.g. colour channels as RGB tuple inputs) and returns a specific, useful output 
        # (e.g., returns True if the pixel matches your custom feature definition else False, or a weight)
def is_target_feature(r, g, b):
    if r > 230 and g > 230 and b > 230:
        return "white"
    if r > 235 and g > 214 and b > 183:
        return "beige"
    elif r > 224 and g > 173 and b > 89:
        return "lightbrown"
    elif r > 179 and g > 88 and b > 26:
        return "mediumbrown"
    elif r > 100 and g > 83 and b > 37:
        return "darkbrown"
    elif r > 45 and g > 34 and b > 6:
        return "black"
    else:
        return "other"

breads = ["6.7/bread1.png", "6.7/bread2.png", "6.7/bread3.png", "6.7/bread4.png", "6.7/bread5.png", "6.7/bread6.png", "6.7/bread7.png", "6.7/bread8.png", "6.7/bread9.png", "6.7/bread10.png"] # store the files in a list for iterating

t2 = time.time()

percentage = []
# iterate (go through all the pixels in the image)
for i in range(len(breads)):
    bread_file = breads[i]
    file = Image.open(bread_file)
    breadImage = file.load()

    width = file.width      # get image dimensions
    height = file.height

    # create a list to store the pixels of the specific colour
    beige_pixels = []
    lightbrown_pixels = []
    mediumbrown_pixels = []
    darkbrown_pixels = []
    black_pixels = []

    for x in range(width):
        for y in range(height):
            # get pixel data
            pixel_data = breadImage[x, y]
            pixel_r = pixel_data[0]
            pixel_g = pixel_data[1]
            pixel_b = pixel_data[2]
            colour_type = is_target_feature(pixel_r, pixel_g, pixel_b)  # determine what colour category this pixel belongs to

            # process pixel based on its colour category
            if colour_type == "beige":
                beige_pixels.append((x, y))     # store original pixel
            elif colour_type == "lightbrown":
                lightbrown_pixels.append((x, y))
            elif colour_type == "mediumbrown":
                mediumbrown_pixels.append((x, y))
            elif colour_type == "darkbrown":
                darkbrown_pixels.append((x, y))
            elif colour_type == "black":
                black_pixels.append((x, y))

    # calculate pixel counts for each colour  
    num_beige = len(beige_pixels)
    num_lightbrown = len(lightbrown_pixels)
    num_mediumbrown = len(mediumbrown_pixels)
    num_darkbrown = len(darkbrown_pixels)
    num_black = len(black_pixels)
    total_pixels = width * height

    # calculate "Feature Density Score" for each image (percentage)
    total_burnt = num_darkbrown + num_black # beige, light brown, and medium brown do not count because it is not burnt
    total_bread = num_beige + num_lightbrown + num_mediumbrown + num_darkbrown + num_black # total area of the bread

    if total_bread > 0: # avoid dividing by 0 for safety
        burnt_percentage = total_burnt / total_bread * 100
        percentage.append((burnt_percentage, breads[i]))
    else:
        burnt_percentage = 0
        percentage.append((burnt_percentage, breads[i]))

    # print results
    output = "Based off bread {}, it is {:.2f}% burnt.".format(breads[i], burnt_percentage)
    print(output)    

#  *UNIT 6* implement the Selection Sort algorithm function yourself (not using built-in libraries for sorting)
    # sort the master list based on the calculated Feature Density Score (highest to lowest)
for i in range(len(percentage)): # highest to lowest
    largest_index = i

    for j in range(i + 1, len(percentage)):
        if percentage[j][0] > percentage[largest_index][0]: # find the largest
            largest_index = j

    percentage[i], percentage[largest_index] = percentage[largest_index], percentage[i] # swap new largest element with old one

print("\nTop 5 most burnt breads are:")
for i in percentage[:5]:
    print(str(i[1]) + " with " + f"{i[0]:.2f}%" + " burn.")

#  *UNIT 6* implement the Binary Search algorithm function yourself to search the sorted list for a specific target score
def search(list_of_lists, query):
    querymin = query - 5 # if burnt percentage is more than 95% (100 - 5)
    search_start_index = 0  # define indexes of search space
    search_end_index = len(list_of_lists) - 1

    while search_start_index <= search_end_index:   # as long as our search space exists
        midpoint = int((search_start_index + search_end_index) / 2) # calculate centre of search space

        if list_of_lists[midpoint][0] <= query and list_of_lists[midpoint][0] >= querymin: # if the element in the centre is what we are looking for, return element
            return list_of_lists[midpoint][1]
        
        elif list_of_lists[midpoint][0] > query and list_of_lists[midpoint][0] >= querymin:    # if what we are looking for is greater than the centre value:
            search_start_index = midpoint + 1   # cut out entire left-hand side of our search space

        else:   # if our query is less than our centre value:
            search_end_index = midpoint - 1 # cut out entire right-hand side of our search space

search_target = 100.00    # looking for bread with 100% burn
found_target = search(percentage, search_target)

if found_target:
    print("\nFound bread with approximately {:.2f}% burn: {}".format(search_target, found_target))
else:
    print("\nNo bread found with approximately {:.2f}% burn".format(search_target))

t3 = time.time()

# code profiling (timings to 3 decimal places)
module_load = t1 - t0
image_open_load = t2 - t1
print_output = t3 - t2
entire = t3 - t0
timings = "It took {:.3f}s to import PIL, {:.3f}s to load the images, and {:.3f}s to print the output. All in all it took {:.3f}s.".format(module_load, image_open_load, print_output, entire)
print(timings)