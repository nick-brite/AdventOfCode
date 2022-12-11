def partOne():
    lines = open(
        'C:/Users/Nick Albright/Projects/AdventOfCode/Day8/realInput.txt', 'r').read().splitlines()
    # Use unpack method
    splitStrings = [[*string] for string in lines]
    forest = list(splitStrings)
    forest = [[int(string) for string in row] for row in forest]

    visibleTrees = 0
    for row in range(1, len(forest) - 1):
        for col in range(1, len(forest[row]) - 1):
            treeHouse = forest[row][col]
            visible = True

            c = col + 1
            while c < len(forest[row]):
                if forest[row][c] >= treeHouse:
                    visible = False
                    break
                c += 1

            if visible:
                visibleTrees += 1
                continue
            visible = True

            # check treehouse's column left
            c = col - 1
            while c > -1:
                if forest[row][c] >= treeHouse:
                    visible = False
                    break
                c -= 1

            if visible:
                visibleTrees += 1
                continue
            visible = True

            # check treehouse's row down
            r = row - 1
            while r > -1:
                if forest[r][col] >= treeHouse:
                    visible = False
                    break
                r -= 1

            if visible:
                visibleTrees += 1
                continue
            visible = True

            # check treehouse's row up
            r = row + 1
            while r < len(forest):
                if forest[r][col] >= treeHouse:
                    visible = False
                    break
                r += 1

            if visible:
                visibleTrees += 1
                continue
            visible = True

    print('interior visible trees: ' + str(visibleTrees))
    # add trees visible from exterior
    exteriorTrees = len(forest) * 2 + len(forest[0]) * 2 - 4
    print('exterior visible trees: ' + str(exteriorTrees))
    print(visibleTrees + exteriorTrees)


def partTwo():
    lines = open(
        'C:/Users/Nick Albright/Projects/AdventOfCode/Day8/realInput.txt', 'r').read().splitlines()
    # Use unpack method
    splitStrings = [[*string] for string in lines]
    forest = list(splitStrings)
    forest = [[int(string) for string in row] for row in forest]

    highestTreeScore = 0
    for row in range(1, len(forest) - 1):
        for col in range(1, len(forest[row]) - 1):
            treeHouse = forest[row][col]
            treeScore = 1

            # check treehouse's viewing score right
            c = col + 1
            directionalTreeScore = len(forest[row]) - col - 1
            while c < len(forest[row]):
                if forest[row][c] >= treeHouse:
                    directionalTreeScore = c - col
                    break
                c += 1

            treeScore *= directionalTreeScore
            if treeScore == 0:
                continue

            # check treehouse's column left
            c = col - 1
            directionalTreeScore = col
            while c > -1:
                if forest[row][c] >= treeHouse:
                    directionalTreeScore = col - c
                    break
                c -= 1

            treeScore *= directionalTreeScore
            if treeScore == 0:
                continue

            # check treehouse's row up
            r = row - 1
            directionalTreeScore = row
            while r > -1:
                if forest[r][col] >= treeHouse:
                    directionalTreeScore = row - r
                    break
                r -= 1

            treeScore *= directionalTreeScore
            if treeScore == 0:
                continue

            # check treehouse's row down
            r = row + 1
            directionalTreeScore = len(forest) - row - 1
            while r < len(forest):
                if forest[r][col] >= treeHouse:
                    directionalTreeScore = r - row
                    break
                r += 1

            treeScore *= directionalTreeScore
            if treeScore == 0:
                continue

            if treeScore > highestTreeScore:
                highestTreeScore = treeScore

    print(highestTreeScore)


partTwo()
