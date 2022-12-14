from collections import deque
from collections import defaultdict


visited = set()
queue = deque()

def outputArray(array):
    for a in array:
        print(a)

def outputDistanceMap(dict: defaultdict, distanceArr):
    for key in dict.keys():
        distanceArr[key[0]][key[1]] = dict.get(key)
    outputArray(distanceArr)

def getUnvisitedNeighbors(row, col):
    neighbors = list()
    for i in range(-1, 2):
        for j in range(-1, 2):
            # make sure not self and make sure in range of array
            if (i, j) != (0, 0) and not (abs(i) == 1 and abs(j) == 1):
                rowIndex, colIndex = row + i, col + j
                if rowIndex > -1 and rowIndex < len(elevationArray) and colIndex > -1 and colIndex < len(elevationArray[0]):
                    if (rowIndex, colIndex) not in visited:
                        neighbors.append((row + i, col + j))

    return (neighbors)


elevationArray = list()
for l in open(
        'C:/Users/Nick Albright/Projects/AdventOfCode/Day12/realInput.txt', 'r').read().splitlines():
    elevationArray.append([*l])

for r in range(len(elevationArray)):
    for c in range(len(elevationArray[0])):
        if elevationArray[r][c] == 'S':
            elevationArray[r][c] = 26
        elif elevationArray[r][c] == 'E':
            startPosition = (r, c)
            elevationArray[r][c] = 0
        else:
            elevationArray[r][c] = abs(ord(elevationArray[r][c]) - ord('a') - 26)

# for debugging
distanceArr = list()
for r in range(len(elevationArray)):
    thisList = list()
    distanceArr.append(thisList)
    for c in range(len(elevationArray[0])):
        thisList.append(1000000)
        

# this means that if distance[k] then distance[k] = 1000000
distance = defaultdict(lambda: 1000000)
distance[startPosition] = 0

# Breadth First Search time
queue.append(startPosition)

while queue:
    vertex = queue.popleft()
    visited.add(vertex)
    vertDistance = distance[vertex]

    if (elevationArray[vertex[0]][vertex[1]]) == 26:
        print('shortest a location ' + str(vertex) +
              ' found: ' + str(vertDistance))
        break
    else:
        vertexNeighbors = getUnvisitedNeighbors(vertex[0], vertex[1])
        for n in vertexNeighbors:
            if elevationArray[n[0]][n[1]] - elevationArray[vertex[0]][vertex[1]] < 2:
                newDistance = vertDistance + 1
                if newDistance < distance[n]:
                    queue.append(n)
                    distance[n] = vertDistance + 1


