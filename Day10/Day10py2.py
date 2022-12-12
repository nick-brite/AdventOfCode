import numpy as np

rowLength = 40
pixelTracker = np.zeros(240)
rowTracker = 0
rowPosition = 0
totalPosition = 0
xPosition = 1

def handleSprite():
    if abs(xPosition - rowPosition) < 2:
        # draw a pixel
        pixelTracker[rowTracker * rowLength + rowPosition] = 1
    else:
        pixelTracker[rowTracker * rowLength + rowPosition] = 0

    

def outputCRT():
    output = ""
    for i in range(240):
        if i % 40 == 0:
            output += '\n'
        if pixelTracker[i] == 0:
            output += '.'
        else:
            output += '#'
    print(output)
        
lines = open(
     'C:/Users/Nick Albright/Projects/AdventOfCode/Day10/realInput.txt', 'r').read().splitlines()

for l in lines:
    if l == 'noop':
        handleSprite()

        totalPosition += 1
        if totalPosition % rowLength == 0: 
            rowTracker += 1
            rowPosition = 0
        else:
            rowPosition += 1
    else:
        num = int(l.split(' ')[1])

        handleSprite()
        totalPosition += 1
        if totalPosition % rowLength == 0: 
            rowTracker += 1
            rowPosition = 0
        else:
            rowPosition += 1

        handleSprite()
        # sprite stuff

        totalPosition += 1
        if totalPosition % rowLength == 0: 
            rowTracker += 1
            rowPosition = 0
        else:
            rowPosition += 1

        xPosition += num

    #print(l)

outputCRT()
