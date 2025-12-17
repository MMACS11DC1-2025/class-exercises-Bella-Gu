"""
Create a program that uses counting and comparison operators (< > <= >=).
You must use the class' datafile, 'responses.csv' and analyze it
    to make at least 2 interesting observations.
You must use user input to add interactivity to the program.
You must design your algorithm in English first, then translate it to Python code.
Test as you go! Describe in your comments what steps you took to test your code.
"""

f"""
Simple Personality Comparison Program
Compares survey responses between two people
"""

"""
Bella Gu Data Analysis
1) Introduction and ask for 2 user's name
2) Compare the 2 users and return a number of things they have in common
3) Return how similar they are based off how much they have in common
"""
# Open and read the data file
file = open("2.4/responses.csv")
lines = file.readlines()

# Introduction
print("\nWelcome to the compatibility score! \nEnter 2 names and find out how many things they have in common with eachother.")

# Get user input (2 names)
name1 = input("\nName 1: ").lower().strip()
name2 = input("Name 2: ").lower().strip()

# Find both people in the data
person1 = ""
person2 = ""

for line in lines:
    if name1 in line.lower():
        person1 = line.strip().split(",") # Split the data into a list
    if name2 in line.lower():
        person2 = line.strip().split(",") # Split the data into a list

# If name is not found in the database
if person1 == "" or person2 == "":
    print("Oops! Name(s) not found. Please try again.")
    exit()

# Compare their answers (skip the number and name at index 0)
matches = 0
for match in range(2, min(len(person1), len(person2))):
    if person1[match] == person2[match]:
        matches += 1

print("\nNumber of things in common: " + str(matches))

# Determine compatibility
if matches <= 1:
    print("\nYou guys are not alike. It's okay, I'm sure you guys will be good friends.")
elif matches > 1 and matches <= 3:
    print("\nYou guys are somewhat alike. Befriend them! Bring a smile on their face!")
elif matches > 3 and matches <= 6:
    print("\nYou guys are quite similar to eachother. Try talking to them! Who knows what friendship you guys will have?")
elif matches >= 8:
    print("\nYou guys share a lot in common! It's best to start getting to know them better! You guys can be best friends forever!")

"""
Results:
1) Compared Bella and Bella, prints correct comment (Share a lot matches in comon)
2) Compared Bella and Erisha, prints correct comment (Somewhat alike)
3) Compared 'Hello' and 'Goodbye', prints correct comment (Names not found)
"""