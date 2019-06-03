def readfile(): #funkcja odczytująca wartości z pliku
    data = []
    file = open("learning.txt", "r")
    for i, line in enumerate(file):
        line = line.replace("\n", "")  
        line = line.replace("\r", "")
        line = line.replace("[", "")
        line = line.replace(")", "")
        line = line.replace(",",".")
        data.append(line.split("|"))
    file.close()
    return data

def splitdata(data): #funkcja dzieląca odczytane dane z pliku na pojedyńcze liczby
    dataA = []
    dataB = []
    for line in data:
        dataA.append(line[0].split("; "))
        dataB.append(line[1].split("; "))
    return dataA,dataB

def group(data,howmany): #funkcja grupuje wszystkie rekordy i zlicza ich wystąpienie w danym zbiorze
    groupdata = []
    i = 0
    for line in data:
        if i < howmany:
            counter = 0
            for line2 in groupdata:
                if line[0] == line2[0] and line[1] == line2[1]:
                    counter += 1
                    if line[2] == "A":
                        line2[2] += 1
                    elif line[2] == "B":
                        line2[3] += 1
                    elif line[2] == "C":
                        line2[2] += 1
                else:
                    continue
            if counter == 0:
                if line[2] == "A":
                    groupdata.append([line[0], line[1], 1, 0, 0])
                elif line[2] == "B":
                    groupdata.append([line[0], line[1], 0, 1, 0])
                elif line[2] == "C":
                    groupdata.append([line[0], line[1], 0, 0, 1])
            i += 1
        else:
            break
    return groupdata

def countpack(): # funkcja licząca ile rekordów jest w pliku
    counts = 0
    data = readfile()
    for line in data:
        counts += 1
    return counts/10

def check(a,b): # najważniejsza funkcja programu która sprawdza do którego zbioru należą dane liczby
    howmany = 10
    j = 0
    pA = 0
    pB = 0
    pC = 0
    pack = 1
    maxpack = int(countpack())
    counter = 0
    print("Program rozpoczyna analizę:")
    while True:
        if pack <= maxpack:
            print("Paczka " + str(pack) + " z " + str(maxpack))
            dataA, dataB = splitdata(group(readfile(), howmany))
            groupdata = group(readfile(), howmany)
            for line in groupdata:
                counter += 1
            while j < counter:
                if (float(dataA[j][0]) <= float(a) < float(dataA[j][1])) and (float(dataB[j][0]) <= float(b) < float(dataB[j][1])):
                    pA += ((float(groupdata[j][2]) * 1)/1) * ((float(groupdata[j][2]) * 1)/1) * (float(groupdata[j][2])/float(howmany))
                    pB += ((float(groupdata[j][3]) * 1)/1) * ((float(groupdata[j][3]) * 1)/1) * (float(groupdata[j][3])/float(howmany))
                    pC += ((float(groupdata[j][4]) * 1)/1) * ((float(groupdata[j][4]) * 1)/1) * (float(groupdata[j][4])/float(howmany))
                j += 1
            maxp = max(pA, pB, pC)
            if maxp > 0:
                if maxp == pA:
                    print("Nelezy do A")
                elif maxp == pB:
                    print("Należy do B")
                elif maxp == pC:
                    print("Należy do C")
            else:
                print("Na podstawie tych danych nie można przydzielić do żadnego zbioru")
            print("Czy chcesz doczytać kolejną paczkę danych ?[tak / nie]")
            w = input()
            if w == "tak":
               howmany += 10
               counter = 0
               j = 0
               maxp = 0
            else:
               break
            pack += 1
        else:
            print("Odczytano juz dane z wszystkich paczek, program zakończy pracę.")
            break

print("Podaj wartości a i b, mogą być to wartości zmiennoprzecinkowe lub całkowite")
a = input("Podaj a: ")
b = input("Podaj b: ")
check(float(a),float(b))

##przykładowa wartość a = 6.7 i b = 2.2 pokazuje że program dopiero po wczytaniu kilku paczek potrafi przydzielić do
# konkretnego zbioru, a wartość a = 5.5 i b = 1.7, że po kilku paczkach program zmienia decyzję co do przydzielenia