


def partOne():
    reading = open("Day_01/day1.txt", "r")
    calibration = ""

    for x in reading.read():
        if x.isdigit():
            calibration += x
        elif x.isspace():
            calibration += ","


    toList = calibration.split(",")
    toString = ""

    for z in range(0, len(toList)):
        if len(toList[z]) == 0:
            continue

        else:
            one = toList[z][0]
            toString += one

            two = toList[z][-1]
            toString += two
            toString += ","

    modifiedListedString = toString.split(",")[:-1]

    answer = [int(modifiedListedString[y]) for y in range(0, len(modifiedListedString))]
    print("Final answer for part 1:", sum(answer))



def partTwo():
    reading = open("Day_01/day1.txt", "r")
    listOfNums = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    calibration = ""

    firstList = reading.read().split("\n")

    for y in firstList:
        for i, val in enumerate(listOfNums):
            count = 0
            while count < len(y):
                if i > 9:
                    i = 0
                    count += 1
                if y.startswith(listOfNums[i], count):
                    # print(f"({count}) String:", y, listOfNums[i], count)
                    calibration += str(i)
                    i += 1
                    count -= 1
                elif y.startswith(str(i), count):
                    # print(f"({count}) Number:", y, i, count)
                    calibration += str(i)
                    i += 1
                    count -= 1
                elif not y.startswith(str(i), count):
                    # print("Not found", i, count)
                    i += 1
                    count -= 1
                
                count += 1
            else:
                calibration += ","
                break

    modifiedCalibration = calibration.split(",")

    while "" in modifiedCalibration:
        modifiedCalibration.remove("")

    # print(modifiedCalibration)



    toList = calibration.split(",")
    toString = ""

    for z in range(0, len(toList)):
        if len(toList[z]) == 0:
            continue

        else:
            one = toList[z][0]
            toString += one

            two = toList[z][-1]
            toString += two
            toString += ","

    modifiedListedString = toString.split(",")[:-1]
    # print(modifiedListedString)

    answer = [int(modifiedListedString[y]) for y in range(0, len(modifiedListedString))]
    print("Final answer for part 2:", sum(answer), "|", type(answer))


partOne()
partTwo()