# Sum up game IDs if the configuration is possible: 12 red cubes, 13 green cubes, and 14 blue cubes

reading = open("Day_02/day2.txt", "r")
testing = open("Day_02/testing.txt", "r")

toList = testing.read().split()

red, green, blue = 12, 13, 14

for x in toList:
    print(x, end=" ")
    if ";" in x:
        print("www")
        break
    if "," in x:
        print("-")

