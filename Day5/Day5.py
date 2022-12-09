def partOne():
    lineCounter = 0
    stackList = [[] for x in range(10)]

    lines = open('C:/Users/Nick Albright/Projects/AdventOfCode/Day5/Stacks.txt', 'r').read().splitlines()

    while lineCounter < 8:
        # additional space to make the char counting even, subtraction to flip image for stack building
        line = lines[7 - lineCounter] + ' '
        rows = list(map(''.join, zip(*[iter(line)]*4)))

        for i in range(0, len(rows)):
            if rows[i][1] != ' ':
                stackList[i].append(rows[i][1])
        lineCounter += 1

    # parsing complete, now time to move these boxes
    for k in range (10, len(lines)):
        lineSplit = lines[k].split(' ')
        amount = int(lineSplit[1])
        start = int(lineSplit[3]) - 1
        end = int(lineSplit[5]) - 1

        for j in range(0, amount):
            #outputStacks(stackList)
            stackList[end].append(stackList[start].pop())
    
    outputStacks(stackList)

def partTwo():
    lineCounter = 0
    stackList = [[] for x in range(10)]

    lines = open('C:/Users/Nick Albright/Projects/AdventOfCode/Day5/Stacks.txt', 'r').read().splitlines()

    while lineCounter < 8:
        # additional space to make the char counting even, subtraction to flip image for stack building
        line = lines[7 - lineCounter] + ' '
        rows = list(map(''.join, zip(*[iter(line)]*4)))

        for i in range(0, len(rows)):
            if rows[i][1] != ' ':
                stackList[i].append(rows[i][1])
        lineCounter += 1

    # parsing complete, now time to move these boxes
    for k in range (10, len(lines)):
        lineSplit = lines[k].split(' ')
        amount = int(lineSplit[1])
        start = int(lineSplit[3]) - 1
        end = int(lineSplit[5]) - 1

        miniStack = []
        for j in range(0, amount):
            element = stackList[start].pop()
            miniStack.append(element)
        miniStack.reverse()
        stackList[end].extend(miniStack)

    outputStacks(stackList)

def outputStacks(stackList):
    for i in range(0,9):
        print(stackList[i])
        
partTwo()