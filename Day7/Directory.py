dirList = []

class Directory:
    def __init__(self, name, parent):
        self.parent = parent
        self.name = name
        self.flatFileSize = 0
        self.children = list()

    def toString(self):
        childrenNames = list()
        for c in self.children:
            childrenNames.append(c.name)
        return ('Name: ' + str(self.name) + ' flatFileSize: ' +
              str(self.flatFileSize) + ' children: ' + str(childrenNames))

def addDirectoryAttributes(currDir, lines, counter):
    # add relevant attributes to the directory
    for j in range(counter+2, len(lines)):
        splitLine = lines[j].split(' ')
        if len(splitLine) == 3:
            return j
        if splitLine[0].isdigit():
            currDir.flatFileSize += int(splitLine[0])
        else:
            currDir.children.append(Directory(splitLine[1], currDir))
    return len(lines)

def getFileSum(dir):
    dirSize = 0

    # base case
    if len(dir.children) == 0:
        dirSize = dir.flatFileSize
    else:
        childSize = 0
        for c in dir.children:
            childSize += getFileSum(c)
        dirSize = dir.flatFileSize + childSize
    dirList.append(dirSize)
    return dirSize

lines = open(
    'C:/Users/Nick Albright/Projects/AdventOfCode/Day7/Directory.txt', 'r').read().splitlines()

rootDir = Directory('/', None)
currDir = rootDir
parent = None
i = 0
while i < len(lines):
    splitLine = lines[i].split(' ')

    # TODO: these conditionals should be flip flopped for cleanliness
    if len(splitLine) == 3 and splitLine[1] == 'cd' and splitLine[2] != '/' and splitLine[2] != '..':
        dirName = splitLine[2]
        if (parent == None):
            currDir = Directory(dirName, parent)
        else:
            # find correct directory object in parent
            for c in parent.children:
                if c.name == dirName:
                    currDir = c
                    break

        # add relevant attributes to the directory
        breakLine = addDirectoryAttributes(currDir, lines, i)

        # prep for next directory move
        parent = currDir
        i = breakLine

    elif len(splitLine) == 3 and splitLine[2] == '/':
        currDir = rootDir
        # creation case for root directory
        if len(currDir.children) == 0:
            breakLine = addDirectoryAttributes(currDir, lines, i)
            parent = currDir
            i = breakLine
        else:
            currDir = rootDir
            parent = None
            i += 1

    elif len(splitLine) == 3 and splitLine[2] == '..':
        currDir = currDir.parent
        parent = currDir
        i += 1

#Part one
print(getFileSum(rootDir))
total = 0
#print(dirList)
for dir in dirList:
    if dir <= 100000:
        total += dir

#print(total)

#Part two - used some pocket math to determine the smallest file size that would clear enough space
minSize = 1272621
idealDirSize = 999999999999999999
for dir in dirList:
    if dir >= minSize:
        if dir < idealDirSize:
            idealDirSize = dir
print(idealDirSize)