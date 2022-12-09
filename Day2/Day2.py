import numpy as np

def main():
    # read the file in
    content = parseFile()

    # separate each round of play by splitting by newline
    roundList = content.split('\n')
    totalPoints = 0
    for i in range(len(roundList)):
        # totalPoints += pointsFromRoundSelectionGiven(roundList[i])
        totalPoints += pointsFromRoundOutcomeGiven(roundList[i])
    print('The total points are: ' + str(totalPoints))
    

def parseFile():
    file = open(
        'C:/Users/Nick Albright/Projects/AdventOfCode/Day2/RockPaperScissorsInput.txt', 'r')
    content = file.read()
    file.close
    return content

def pointsFromRoundSelectionGiven(roundString):
    firstChar = roundString[0]
    secondChar = roundString[2]

    # first, determine points from selection independent of victory condition
    selectionPoints = 0
    match secondChar:
        case 'X':
            selectionPoints = 1
        case 'Y':
            selectionPoints = 2
        case 'Z':
            selectionPoints = 3

    # now, determine outcome points
    outcomePoints = 0
    match firstChar:
        case 'A':
            match secondChar:
                case 'X':
                    outcomePoints = 3
                case 'Y':
                    outcomePoints = 6
                case 'Z':
                    outcomePoints = 0
        case 'B':
            match secondChar:
                case 'X':
                    outcomePoints = 0
                case 'Y':
                    outcomePoints = 3
                case 'Z':
                    outcomePoints = 6
        case 'C':
            match secondChar:
                case 'X':
                    outcomePoints = 6
                case 'Y':
                    outcomePoints = 0
                case 'Z':
                    outcomePoints = 3    

   # # uncomment for debug 
   # print('\n')
   # print('firstChar: ' + str(firstChar) + ' secondChar: ' + str(secondChar))
   # print('selection points: ' + str(selectionPoints) + ' outcome points: ' + str(outcomePoints))
    return outcomePoints + selectionPoints

def pointsFromRoundOutcomeGiven(roundString):
    firstChar = roundString[0]
    secondChar = roundString[2]

    # first, determine points from outcome independent of selection
    outcomePoints = 0
    match secondChar:
        case 'X':
            outcomePoints = 0
        case 'Y':
            outcomePoints = 3
        case 'Z':
            outcomePoints = 6

    # now, determine selection points
    selectionPoints = 0
    match firstChar:
        case 'A':
            match secondChar:
                case 'X':
                    selectionPoints = 3
                case 'Y':
                    selectionPoints = 1
                case 'Z':
                    selectionPoints = 2
        case 'B':
            match secondChar:
                case 'X':
                    selectionPoints = 1
                case 'Y':
                    selectionPoints = 2
                case 'Z':
                    selectionPoints = 3
        case 'C':
            match secondChar:
                case 'X':
                    selectionPoints = 2
                case 'Y':
                    selectionPoints = 3
                case 'Z':
                    selectionPoints = 1    

    # uncomment for debug 
    # print('\n')
    # print('firstChar: ' + str(firstChar) + ' secondChar: ' + str(secondChar))
    # print('selection points: ' + str(selectionPoints) + ' outcome points: ' + str(outcomePoints))
    return outcomePoints + selectionPoints

main()
