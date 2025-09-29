file = open("2.4/responses.csv")

reply = input("what's your name?").lower().strip()

for line in file:
    if reply in line.lower():
        print(line)
        myline = line

reply2 = input("who do you want to compare yourself to? enter a name in the comp sci class.").lower.strip()
for line in file:
    if reply2 in line.lower():
        print(line)
        myline = line