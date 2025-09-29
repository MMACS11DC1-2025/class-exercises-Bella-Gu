file = open("2.4/responses.csv")

for line in file:
    if "bella" in line.lower():
        print(line)
        myline = line
