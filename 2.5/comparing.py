"""
Create a program that uses counting and comparison operators (< > <= >=).
You must use the class' datafile, 'responses.csv' and analyze it
    to make at least 2 interesting observations.
You must use user input to add interactivity to the program.
You must design your algorithm in English first, then translate it to Python code.
Test as you go! Describe in your comments what steps you took to test your code.
"""

file = open("2.4/responses.csv")
filee = file.readlines()
line = ""
line2 = ""

reply = input("what's your name? ").lower().strip()
reply2 = input("who do you want to compare yourself to? ").lower().strip()

for line in filee:
    if reply in line.lower():
        print(line)
        line = line

    if reply2 in line.lower():
        print(line)
        line2 = line2

line = line.split(",")
line2 = line2.split(",")
user = list(line)


compare = [item for item in line if item in line2]
result = len((compare)

if result <= 0:
    print("You guys are not alike.")
elif result <= 5:
    print("You guys are somewhat alike.")
elif result <= 9:
    print("You guys are similar to eachother.")
elif result >= 10:
    print("You guys share everything in common.")
else:
    print("I'm not sure I understand.")