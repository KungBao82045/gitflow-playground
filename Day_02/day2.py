# Sum up the cubes and see if they don't reach up beyong limits.
# If valid, sum up the possible IDs

import re

reading = open("Day_02/day2.txt").read()


reSkills = re.findall("([Game]{4})\s(\d{1,})(:\s)(.+)", reading)

sum_ID = []

color = ["red", "green", "blue"]

for game, id, colon, val in reSkills:
    check = True

    splitting = val.split(";")

    for x in splitting:
        y = x.split(",")
        for z in y:

            c = 0
            while c < len(color):
                if color[c] in z:
                    stripping = z.strip()
                    splitting = stripping.split(" ")
                    if color[c] == "red":
                        if int(splitting[0]) > 12:
                            check = False
                    elif color[c] == "green":
                        if int(splitting[0]) > 13:
                            check = False
                    elif color[c] == "blue":
                        if int(splitting[0]) > 14:
                            check = False
                    
                c += 1
    if check:
        # print(f"{id}: {val}")
        sum_ID.append(id)

answer = [int(sum_ID[y]) for y in range(0, len(sum_ID))]
print("Final answer for day 2:", sum(answer), "|", type(answer))
