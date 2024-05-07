max = '0\n'
min = '9\n'
temp = ""

with open("input.txt") as f:
    for line in f:
        temp = int(line[-2])
    if (temp > int(max[-2])):
        max = line;
    elif (temp < int(min[-2])):
        min = line
jun = open("jun.txt", "w")
jun.write(min)
old = open("old.txt", "w")
old.write(max)