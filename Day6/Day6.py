def partOne():
    line = open('C:/Users/Nick Albright/Projects/AdventOfCode/Day6/Message.txt', 'r').read()
    for i in range (3, len(line)):
        groupOfFour = []
        groupOfFour.append(line[i])
        groupOfFour.append(line[i-1])
        groupOfFour.append(line[i-2])
        groupOfFour.append(line[i-3])
        if len(set(groupOfFour)) == 4:
            print(i)
            print(groupOfFour)
            break

def partTwo():
    line = open('C:/Users/Nick Albright/Projects/AdventOfCode/Day6/Message.txt', 'r').read()
    for i in range (13, len(line)):
        groupOfFourTeen = []
        for n in range(0, 14):
            groupOfFourTeen.append(line[i-n])
        if len(set(groupOfFourTeen)) == 14:
            print(i)
            print(groupOfFourTeen)
            break

partTwo()