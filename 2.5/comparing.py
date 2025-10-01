"""
Create a program that uses counting and comparison operators (< > <= >=).
You must use the class' datafile, 'responses.csv' and analyze it
    to make at least 2 interesting observations.
You must use user input to add interactivity to the program.
You must design your algorithm in English first, then translate it to Python code.
Test as you go! Describe in your comments what steps you took to test your code.
"""

file = open("2.4/responses.csv")

reply = input("what's your name?").lower().strip()
for line in file:
    if reply in line.lower():
        print(line)
        myline = line

reply2 = input("who do you want to compare yourself to? enter a name in the comp sci class.").lower().strip()
for line in file:
    if reply in line.lower():
        print(line)
        myline = line




