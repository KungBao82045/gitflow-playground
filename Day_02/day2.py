import re  # Bruk 're' (regex) bibliotek til å finne og matche mønster

reading = open("Day_02/day2.txt").read() # Åpne en tekst fil til å lese innholdet
reSkills = re.findall("([Game]{4})\s(\d{1,})(:\s)(.+)", reading) # Bruker regex til å finne og matche mønster (regex101.com)
color = ["red", "green", "blue"]

def partOne():

    sum_ID = []  

    for game, id, colon, val in reSkills: # For loop til å returnere iterasjon av ryddige spill id og verdier ('id', and 'val' are focused)
        check = True

        splitting = val.split(";") # separer string ';' til list: e.g fra, "1 red, 2 green, 13 blue; 1 green, 2 red, 9 blue; 12 red; 3 blue, 5 red" >>> ['11 blue', ' 6 blue, 8 green, 4 red', ' 7 blue, 1 red, 1 green']

        for x in splitting:
            y = x.split(",") # separer string ',' til list: e.g fra, "2 blue, 12 green" >>> ['2 blue', ' 12 green']

            for z in y:

                c = 0

                while c < len(color):
                    if color[c] in z:
                        
                        # Fjern whitespace fra begynnelse og til slutt.
                        # separer string " " til list: e.g fra, "5 blue" >>> ['5', 'blue']   
                        splitting = z.strip().split(" ")  
                        # print(splitting, z)

                        # Hvis farge er rød og høyere enn 12, sett "check = False" som betyr å ikke legg til spill ID
                        # Hvis farge er grønn og høyere enn 13, sett "check = False" som betyr å ikke legg til spill ID
                        # Hvis farge er blå og høyere enn 14, sett "check = False" som betyr å ikke legg til spill ID
                        if color[c] == "red" and int(splitting[0]) > 12 or color[c] == "green" and int(splitting[0]) > 13 or color[c] == "blue" and int(splitting[0]) > 14:
                            check = False
                        
                        
                    c += 1

        if check:
            # print(f"{id}: {val}")
            sum_ID.append(id) # Legg til alle gyldige spill ID


    print("Final answer for day 2, part 1:", sum([int(sum_ID[y]) for y in range(0, len(sum_ID))]))   # Konverter string til integer til å summere antall spill ID

def partTwo():

    finalSum = []
    sum_Color = []

    for game, id, colon, val in reSkills: # For loop til å returnere iterasjon av ryddige spill id og verdier ('val' is focused)
        
        max_Color_G = [] 
        max_Color_B = [] 
        max_Color_R = [] 

        splitting = val.split(";") # separer string ';' til list: e.g fra, "1 red, 2 green, 13 blue; 1 green, 2 red, 9 blue; 12 red; 3 blue, 5 red" >>> ['11 blue', ' 6 blue, 8 green, 4 red', ' 7 blue, 1 red, 1 green']

        for x in splitting:
            y = x.split(",") # separer string ',' til list: e.g fra, "2 blue, 12 green" >>> ['2 blue', ' 12 green']
            for z in y:

                c = 0
                
                splitting = z.strip().split(" ")

                while c < len(color):
                    if color[c] in z:
                        if color[c] == "green":
                            max_Color_G.append(int(splitting[0]))  # Legg till alle antalle grønne kuber
                        elif color[c] == "blue":
                            max_Color_B.append(int(splitting[0]))  # Legg till alle antalle blåde kuber
                            # print(splitting[0])
                        elif color[c] == "red":
                            max_Color_R.append(int(splitting[0]))  # Legg till alle antalle røde kuber

                    c += 1

        # Legg till hvert antall farge kuber (maks)
        sum_Color.append(max(max_Color_R))
        sum_Color.append(max(max_Color_G))
        sum_Color.append(max(max_Color_B))




        count = 1
        new = ""

        # Multipliser alle integer i 'sum_Color'
        while count < len(sum_Color):
            if count == 1:
                x = int(sum_Color[0]) * int(sum_Color[count])
                new = x
                # print(new)
            else:
                summing = int(new) * int(sum_Color[count])
                new = summing

            count += 1

        else:
            finalSum.append(new)  # Summer integer
            # print("SUMMED:", sum_Color, val)
            sum_Color = [] # Tøm listen som at den ikke tar med forrige verdi



    print("Final answer for day 2, part 2:", sum(finalSum))


            
partOne()
partTwo()