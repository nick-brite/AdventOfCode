import numpy as np

def partOne():
    sum = 0
    for line in open('C:/Users/Nick Albright/Projects/AdventOfCode/Day4/Sections.txt', 'r').read().splitlines():
        first, second = line.split(',')
        if isWithin(first, second):
            sum += 1
    print(sum)    

def partTwo():
    sum = 0
    for line in open('C:/Users/Nick Albright/Projects/AdventOfCode/Day4/Sections.txt', 'r').read().splitlines():
        first, second = line.split(',')
        if overlaps(first, second):
            sum += 1
    print(sum)    


def isWithin(first, second):
    firstArr = np.linspace(int(first.split('-')[0]), int(first.split('-')[1]), int(first.split('-')[1]) - int(first.split('-')[0]) + 1)
    secondArr = np.linspace(int(second.split('-')[0]), int(second.split('-')[1]), int(second.split('-')[1]) - int(second.split('-')[0]) + 1)

    if set(firstArr).issubset(set(secondArr)) or set(secondArr).issubset(set(firstArr)):
        return True
    return False

def overlaps(first, second):
    firstArr = np.linspace(int(first.split('-')[0]), int(first.split('-')[1]), int(first.split('-')[1]) - int(first.split('-')[0]) + 1)
    secondArr = np.linspace(int(second.split('-')[0]), int(second.split('-')[1]), int(second.split('-')[1]) - int(second.split('-')[0]) + 1)

    if set(firstArr).isdisjoint(set(secondArr)):
        return False
    return True

partTwo()