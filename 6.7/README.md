CODE OVERVIEW
    - My code is about bread. The program will print the percentage of how burnt it is and also print the top 5 most burnt breads. (with the percentage) #dftyguinmko
    - I imported 10 images of a mix of breads and toasts. Some toasts are more burnt than others.
    - The code will scan through all the pixels for each of the 10 photos and detect which part of the bread is burnt and not burnt.
    - My 'def is_target_feature(r, g, b)' will return RGB values. As the code iterates, it will determine which colour category it belongs to. Ex. white category, light brown category... etc.
    - After it is done scanning an image, it will bring back a percentage of how much it is burnt. It will print 10 percentages in total.
    - It will get the amount of pixels in each colour category, add the most burnt colours (dark brown and black), divide it by the total area of the bread, and multiply by 100 to get the percentage.
    - After the iteration process is finished, the code will go though Selection Sort to print the top 5 most burnt breads based off percentages.
    - In the end, it will go through Binary Search, using the sorted list to detect of any breads are close to 100.00% burn. If yes, it will print whatever number the bread is. If not, it will say that no bread was found with that specific percentage.


    - I would say that this code is accurate because it #oiuuyntbrvcexwq and the percentages are precise. #srdtyfvyubunij

TESTING CASES
    - rjurturuuuturt

CODE PROFILING
    - rdvsergdfsgerf
    
CHALLENGES FACED
    - Printing the Selection Sort is probably the most hardest encounter during this entire project. I could not print the top 5 lists and was not able to figure out how to turn it into a string. However, with the help of some of my classmates, one of them was able to give me a starting point, which was to print it in a 'for loop [:5].' I made a list that contained the percentage and the bread number. While writing code inside the for loop, I turned the bread number into a string and printed the percentage to 2 decimals for consistency. This way, it would print the top 5 in the for loop instead of having to manually write it 5 times.