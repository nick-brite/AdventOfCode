# tried to make my code shorter and use more tricks, shoutout hyper-neutrino on the leaderboards for the inspiration

def partOne():
    sum = 0
    # one-line iteration through file with splitlines
    for line in open('C:/Users/Nick Albright/Projects/AdventOfCode/Day3/Rucksacks.txt', 'r').read().splitlines():
        # split line in half then use sets and the union operator to get duplicates
        first, second = line[:len(line)//2], line[len(line)//2:]
        duplicates = set(first) & set(second)

        lineSum = 0
        for c in duplicates:
            numVal = 0
            # use unicode and ord method to get the letter to the desired number value
            if c.isupper():
                numVal = ord(c) - 38
            else:
                numVal = ord(c) - 96
            lineSum += numVal

        sum += lineSum
    print(sum)


def partTwo():
    badgeTotal = 0
    lines = open(
        'C:/Users/Nick Albright/Projects/AdventOfCode/Day3/Rucksacks.txt', 'r').read().splitlines()

    # get lines, three at a time
    for i in range(len(lines)//3):
        first, second, third = lines[3*i], lines[3*i + 1], lines[3*i + 2]
        badge = list(set(first) & set(second) & set(third))
        if badge[0].isupper():
            badgeTotal += ord(badge[0]) - 38
        else:
            badgeTotal += ord(badge[0]) - 96

    print(badgeTotal)

partOne()
