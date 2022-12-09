# Notes - this was an initial failed attempt. I did not realize directory names were not unique so 
# this set-based attempt failed. See Directory.py for the correct attempt

dirSet = set([])
fileSizeDict = {}
nestedDirsDict = {}
totalSizeDict = {}

def partOne():
    # remember / directory
    lines = open(
        'C:/Users/Nick Albright/Projects/AdventOfCode/Day7/Directory.txt', 'r').read().splitlines()
    for l in lines:
        strippedLine = l.strip()
        # print(line)
        if 'dir' in strippedLine:
            dirSet.add(strippedLine.split(' ')[1])

    for i in dirSet:
        fileSizeDict[i] = 0
        totalSizeDict[i] = 0
        nestedDirsDict[i] = []
    for l in range(0, len(lines) - 1):
        #print()
        dir = None
        if 'cd' in lines[l]:
            lineSplit = lines[l].split()
            if len(lineSplit) == 3:
                thirdChar = lineSplit[2]
                if not (thirdChar == 'x' or thirdChar == '..' or thirdChar == '/'):

                    dir = lines[l].split(' ')[2]
                    cont = True
                    if 'ls' not in (lines[l+1]):
                        cont = False
                    n = 2
                    while (cont and l + n < len(lines)):

                        nextLine = lines[l+n]
                        nextLineSplit = nextLine.split(' ')
                        if len(nextLineSplit) == 3:
                            cont = False
                        else:
                            if (nextLineSplit[0].isdigit()):
                                # this sums the file sizes flat to the folder
                                fileSizeDict[dir] += int(nextLineSplit[0])
                            elif nextLineSplit[0] == 'dir':
                                nestedDirsDict[dir].append(nextLineSplit[1])

                        n += 1

    getDirectorySize('gbv')
    #for dirKey in fileSizeDict:
     #    totalSizeDict[dirKey] = getDirectorySize(dirKey)
    #print(fileSizeDict)
    #print(nestedDirsDict)
    # print(totalSizeDict)


def getDirectorySize(dirName):
    if len(nestedDirsDict[dirName]) < 1:
        # base case
        return fileSizeDict[dirName]
    else:
        ret = 0
        for s in nestedDirsDict[dirName]:
            ret += getDirectorySize(s)
        return fileSizeDict[dirName] + ret

class Directory:
    def __init__(self, parent):
        self.parent = parent
        self.flatFileSize = 0
        self.children = []

    def addChildren(self, children):
        self.children = self.children.extend(children)


def partTwo():
    line = open(
        'C:/Users/Nick Albright/Projects/AdventOfCode/Day6/Message.txt', 'r').read()


partOneSecondTry()
