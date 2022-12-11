def partOne():
    lines = open(
        'C:/Users/Nick Albright/Projects/AdventOfCode/Day9/realInput.txt', 'r').read().splitlines()

    # split directions into one-digit steps
    directions = list()
    for l in lines:
        splitLine = l.split(' ')
        for i in range(int(splitLine[1])):
            directions.append(splitLine[0])

    # track where the tail's been
    placesBeen = set()
    # x, y in a cartesian system
    headLoc = (0, 0)
    tailLoc = (0, 0)
    placesBeen.add(tailLoc)

    for d in directions:
        match d:
            case 'R':
                headLoc = (headLoc[0] + 1, headLoc[1])
            case 'L':
                headLoc = (headLoc[0] - 1, headLoc[1])
            case 'U':
                headLoc = (headLoc[0], headLoc[1] + 1)
            case 'D':
                headLoc = (headLoc[0], headLoc[1] - 1)

        tailLoc = handleHeadMove(headLoc, tailLoc)
        placesBeen.add(tailLoc)

    print(len(placesBeen))

def handleHeadMove(newHeadLoc, tailLoc):
    hx, hy = newHeadLoc[0], newHeadLoc[1]
    tx, ty = tailLoc[0], tailLoc[1]
    ntx, nty = tailLoc[0], tailLoc[1] # new tail loc

    xdif, ydif = abs(hx-tx), abs(hy-ty)
    if xdif > 1 or ydif > 1:
        # catch-up case
        if xdif > 1:
            ntx = tx + 1 if hx > tx else tx - 1
            if (hy != ty):
                nty = ty + 1 if hy > ty else ty - 1
            
        else:
            # ydif > 1 so
            nty = ty + 1 if hy > ty else ty - 1
            if hx != tx:
                ntx = tx + 1 if hx > tx else tx - 1
        newTailLoc = (ntx, nty)
        return newTailLoc
    else:
        # tail is within range of head
        return tailLoc

                
partOne()