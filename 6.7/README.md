CODE OVERVIEW
    - My code is about bread. The program will print each percentage of how burnt it is, the top 5 most burnt breads, and will try to find a percentage close to the range chosen. It can be used in bakeries, pastry stores, etc... to see if they can use the bread.
    - I imported 10 images of a mix of breads and toasts. Some toasts are more burnt than others.
    - The code will scan through all the pixels for each of the 10 photos and detect which part of the bread is burnt and not burnt.
    - My 'def is_target_feature(r, g, b)' will return RGB values. As the code iterates, it will determine which colour category it belongs to. Ex. white category, light brown category... etc.
    - After it is done scanning an image, it will bring back a percentage of how much it is burnt. It will print 10 percentages in total.
    - It will get the amount of pixels in each colour category, add the most burnt colours (dark brown and black), divide it by the total area of the bread, and multiply by 100 to get the percentage. Medium brown does not count as burnt because it is a nice, golden brown shade.
    - After the iteration process is finished, the code will go though Selection Sort to print the top 5 most burnt breads based off percentages.
    - In the end, it will go through Binary Search, using the sorted list from Selection Sort to detect of any breads are close to 100.00% burn, with a range of 95.00 - 100.00%. If yes, it will print whatever number the bread is. If not, it will say that no bread was found within that specific percentage.

    - I would say that this code is accurate because it scans through all the pixels in the image and always classifies it into a colour category, meaning that no pixels will be left behind. 
    - The percentages are precise (to 2 decimal places). 
    - Giving the Binary Search a range (95-100%) can ensure a close enough, accurate result to our target value.

TESTING CASES
    - is_target_feature(r, g, b) function works because I was playing with the RGB values to manipulate the 10 percentages of the breads. I was changing some of the values to ensure that it is the most accurate throughout all the images.
    - Selection Sort: Manually checked all 10 percentages to see if the top 5 was in the correct order to see if it works
    - Binary Sort: Similar to selection sort, I manually checked to see if any percentages were close to my search target, and if it printed the correct bread number.

CODE PROFILING
    - When the program is ran for the first time, it takes longer compared to if ran the second time.
        - FIRST TIME: It took 1.997s to import PIL, 0.000s to load the images, and 2.165s to print the output. All in all it took 4.162s.
        - SECOND TIME: It took 0.043s to import PIL, 0.000s to load the images, and 2.056s to print the output. All in all it took 2.099s.
    - During both times, printing the output takes the longest. This is because it has to go through the iteration process, selection sort, and binary sort before finally printing it to the terminal.
    
CHALLENGES FACED
    - Printing the Selection Sort is probably the most hardest encounter during this entire project. I could not print the top 5 lists and was not able to figure out how to turn it into a string. However, with the help of some of my classmates, one of them was able to give me a starting point, which was to print it in a 'for loop [:5].' I made a list that contained the percentage and the bread number. While writing code inside the for loop, I turned the bread number into a string and printed the percentage to 2 decimals for consistency. This way, it would print the top 5 in the for loop instead of having to manually write it 5 times.
    - My percentages were also inaccurate when I was running the code. They will always be too high or too low. I overcame this by changing the colour values multiple times to ensure that they were accurate throughout the 10 images (as stated in the testing case).