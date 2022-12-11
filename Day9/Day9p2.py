def partTwo():
    lines = open(
        'C:/Users/Nick Albright/Projects/AdventOfCode/Day9/realInputc.txt', 'r').read().splitlines()

    # split directions into one-digit steps
    directions = list()
    for l in lines:
        splitLine = l.split(' ')
        for i in range(int(splitLine[1])):
            directions.append(splitLine[0])

    # track where the tail's been
    placesBeen = set()
    # x, y in a cartesian system
    rope = list()
    for i in range(0, 10):
        rope.append((0, 0))
    placesBeen.add(rope[9])

    for d in directions:
        match d:
            case 'R':
                rope[0] = (rope[0][0] + 1, rope[0][1])
            case 'L':
                rope[0] = (rope[0][0] - 1, rope[0][1])
            case 'U':
                rope[0] = (rope[0][0], rope[0][1] + 1)
            case 'D':
                rope[0] = (rope[0][0], rope[0][1] - 1)

        rope = handleRopeMove(rope)
        placesBeen.add(rope[9])

    print(len(placesBeen))

def handleRopeMove(rope):
    for i in range(len(rope) - 1):
        rope[i+1] = handleSegmentMove(rope[i], rope[i+1])
    return rope
        
def handleSegmentMove(newFrontLoc, backLoc):
    hx, hy = newFrontLoc[0], newFrontLoc[1]
    tx, ty = backLoc[0], backLoc[1]
    ntx, nty = backLoc[0], backLoc[1] # new back link

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
        newBackLoc = (ntx, nty)
        #print('tail moved from ' + str(tailLoc) + ' to: ' + str(newTailLoc))
        return newBackLoc
    else:
        # tail is within range of head
        return backLoc

                
partTwo()