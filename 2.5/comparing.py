"""
Create a program that uses counting and comparison operators (< > <= >=).
You must use the class' datafile, 'responses.csv' and analyze it
    to make at least 2 interesting observations.
You must use user input to add interactivity to the program.
You must design your algorithm in English first, then translate it to Python code.
Test as you go! Describe in your comments what steps you took to test your code.
"""

file = open("2.4/responses.csv")
fileList = file.read().strip().split("\n")
line = fileList[1].split(',')
print(line[1])

reply = input("what's your name?").lower().strip()
reply2 = input("who do you want to compare yourself to? enter a name in the comp sci class.").lower().strip()

for line in file:
    if reply in line.lower():
        print(line)
        line = line
    if reply2 in line.lower():
        print(line)
        line2 = line2

result = [item for item in reply if item in reply2]
print(result)



