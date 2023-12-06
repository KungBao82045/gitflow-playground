# Sum up the cubes and see if they don't reach up beyong limits.
# If valid, sum up the possible IDs

import re  # Bruk 're' (regex) bibliotek til å finne og matche mønster

reading = open("Day_02/day2.txt").read() # Open a file to read its content


reSkills = re.findall("([Game]{4})\s(\d{1,})(:\s)(.+)", reading) # Bruker regex til å finne og matche mønster (regex101.com)

sum_ID = []  

color = ["red", "green", "blue"]

for game, id, colon, val in reSkills: # For loop til å returnere iterasjon av ryddige spill id og verdier
    check = True

    splitting = val.split(";") # separer string ';' til list: e.g fra        "1 red, 2 green, 13 blue; 1 green, 2 red, 9 blue; 12 red; 3 blue, 5 red" >>> ['11 blue', ' 6 blue, 8 green, 4 red', ' 7 blue, 1 red, 1 green']

    for x in splitting:
        y = x.split(",") # separer string ',' til list: e.g fra     "2 blue, 12 green" >>> ['2 blue', ' 12 green']

        for z in y:

            c = 0

            while c < len(color):
                if color[c] in z:
                    stripping = z.strip() # Fjern whitespace fra begynnelse og til slutt
                    splitting = stripping.split(" ") # separer string " " til list: e.g fra        "5 blue" >>> ['5', 'blue']  
                    print(splitting, z)

                    # Hvis farge er rød og høyere enn 12, sett "check = False" som betyr å ikke legg til spill ID
                    if color[c] == "red":
                        if int(splitting[0]) > 12:
                            check = False
                    # Hvis farge er grønn og høyere enn 13, sett "check = False" som betyr å ikke legg til spill ID
                    elif color[c] == "green":
                        if int(splitting[0]) > 13:
                            check = False
                    # Hvis farge er blå og høyere enn 14, sett "check = False" som betyr å ikke legg til spill ID
                    elif color[c] == "blue":
                        if int(splitting[0]) > 14:
                            check = False
                    
                c += 1
    if check:
        # print(f"{id}: {val}")
        sum_ID.append(id) # Legg til alle gyldige spill ID

answer = [int(sum_ID[y]) for y in range(0, len(sum_ID))]            # Konverter string til integer til å summere antall spill ID
print("Final answer for day 2:", sum(answer), "|", type(answer))
