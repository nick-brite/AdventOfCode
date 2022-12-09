import numpy as np

def main():
    content = parseFile()
    splitString = parseContents(content)
    elfCals = countCalories(splitString)
    maxVal = np.argmax(elfCals)
    print('The largest elf weight is: ' + str(elfCals[maxVal]) + ' !!!!!!!!!')
    sortedElfCals = np.sort(elfCals)
    print('The three largest elf weights are: ' + str(sortedElfCals[-1]) + ' ' + str(sortedElfCals[-2]) + ' ' + str(sortedElfCals[-3]))
    print('The total of these elves is: ' + str(sortedElfCals[-1] + sortedElfCals[-2] + sortedElfCals[-3]))

def parseFile():
    file = open(
        'C:/Users/Nick Albright/Projects/AdventOfCode/Day1/ElfCalories.txt', 'r')
    content = file.read()
    file.close
    return content

def parseContents(content):
    splitString = content.split('\n')
    return splitString

def countCalories(splitString):
    elfCals = []
    elfIndex = 0
    
    for i in range(len(splitString)):
        if splitString[i] == '':
            elfIndex += 1
        else:
            if i != 0 and splitString[i-1] != '':
                 elfCals[len(elfCals)-1] += int(splitString[i])
            else:
                elfCals.append(int(splitString[i]))

    return elfCals

main()
