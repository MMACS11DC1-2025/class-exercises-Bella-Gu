CODE OVERVIEW
    - My code is about bread. The program will print the percentage of how burnt it is and also print the top 5 most burnt breads. (with the percentage) #dftyguinmko
    - I imported 10 images of a mix of breads and toasts. Some toasts are more burnt than others.
    - The code will scan through all the pixels for each of the 10 photos and detect which part of the bread is burnt and not burnt.
    - My 'def is_target_feature(r, g, b)' will return RGB values. As the code iterates, it will determine which colour category it belongs to. Ex. white category, light brown category... etc.
    - After it is done scanning an image, it will bring back a percentage of how much it is burnt. It will print 10 percentages in total.
    - It will get the amount of pixels in each colour category, add the most burnt colours (dark brown and black), divide it by the total area of the bread, and multiply by 100 to get the percentage.
    - After the iteration process is finished, the code will go though Selection Sort to print the top 5 most burnt breads based off percentages.
    - In the end, it will go through Binary Search, using the sorted list to detect of any breads are close to 100.00% burn, with a range of 95.00 - 100.00%. If yes, it will print whatever number the bread is. If not, it will say that no bread was found within that specific percentage.


    - I would say that this code is accurate because it #oiuuyntbrvcexwq and the percentages are precise. #srdtyfvyubunij

TESTING CASES
    - rjurturuuuturt

CODE PROFILING
    - When the program is ran for the first time, it takes longer compared to if ran the second time.
        - FIRST TIME: It took 1.997s to import PIL, 0.000s to load the images, and 2.165s to print the output. All in all it took 4.162s.
        - SECOND TIME: It took 0.043s to import PIL, 0.000s to load the images, and 2.056s to print the output. All in all it took 2.099s.
    - During both times, printing the output takes the longest. This is because it has to go through the iteration process, selection sort, and binary sort before finally printing it to the terminal.
    
CHALLENGES FACED
    - Printing the Selection Sort is probably the most hardest encounter during this entire project. I could not print the top 5 lists and was not able to figure out how to turn it into a string. However, with the help of some of my classmates, one of them was able to give me a starting point, which was to print it in a 'for loop [:5].' I made a list that contained the percentage and the bread number. While writing code inside the for loop, I turned the bread number into a string and printed the percentage to 2 decimals for consistency. This way, it would print the top 5 in the for loop instead of having to manually write it 5 times.