import re

reading = open("Day_02/day2.txt").read()


reSkills = re.findall("([Game]{4})\s(\d{1,})(:\s)(.+)", reading)


sum_ID = ""
id_collect = ""


for x in reSkills:
    print(x)

for game, id, colon, val in reSkills:

    check = True
    c = 0

    while c < len(val):

        if val[c].isdigit():
            sum_ID += val[c]
        elif val[c] == "," or val[c] == ";":
            sum_ID += " "


    
    
        c += 1

    else:
        sum_ID += f","
        id_collect += f"{id},"

    print(id, "---", val, "|", len(val), "|", type(val), "|", check)

sum_ID = sum_ID.split(",")

id_collect = id_collect.split(",")


finalSum = []

count1 = 0
count2 = 0
while count1 < len(sum_ID):
    # print(sum_ID[count1], "-", id_collect[count1])
    x = sum_ID[count1].split(" ")
    y = id_collect[count1].split(" ")

    checks = True    




    for testing in x:
        if testing.isdigit():
            if int(testing) > 12:
                checks = False

    if checks:
        print(f"{x} - {y}")
        finalSum.append(y[0])


    count1 += 1

finalAnswer = ""



answer = [int(finalSum[y]) for y in range(0, len(finalSum[:-1]))]
print("Final answer for day 2:", sum(answer), "|", type(answer))