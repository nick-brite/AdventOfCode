def checkInterestingValue(cycleCounter, xVal):
    if cycleCounter in interestingValues:
        print('InterestingValue: ' + str(cycleCounter) + ' xVal: ' + str(xVal) + ' multiplied: ' + str(xVal * cycleCounter))
        return xVal * cycleCounter
    return 0

lines = open(
     'C:/Users/Nick Albright/Projects/AdventOfCode/Day10/realInput.txt', 'r').read().splitlines()

interestingValues = (20, 60, 100, 140, 180, 220)
intValueSum = 0
cycleCounter = 0
xVal = 1
for l in lines:
    if l == 'noop':
        cycleCounter += 1
        intValueSum += checkInterestingValue(cycleCounter, xVal)
    else:
        num = int(l.split(' ')[1])
        cycleCounter += 1
        intValueSum += checkInterestingValue(cycleCounter, xVal)

        cycleCounter += 1
        intValueSum += checkInterestingValue(cycleCounter, xVal)
        xVal += num

    #print(l)

print(intValueSum)