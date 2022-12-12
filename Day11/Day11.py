class Monkey:
    def __init__(self, number, items, operation,  test, trueMonkey, falseMonkey):
        self.number = number
        self.items = items
        self.operation = operation
        self.test = test
        self.trueMonkey = trueMonkey
        self.falseMonkey = falseMonkey
        self.inspects = 0

monkeys = list()
lines = open(
     'C:/Users/Nick Albright/Projects/AdventOfCode/Day11/realInput.txt', 'r').read().splitlines()

for i in range(len(lines)):
    splitLine = lines[i].split(' ')
    if splitLine[0] == 'Monkey':
        monkeyNumber = splitLine[1][0]

        splitStartLine = lines[i+1].strip().split(' ')
        items = []
        for j in range(2, len(splitStartLine)):
            item = splitStartLine[j]
            if ',' in item:
                items.append(item.split(',')[0])
            else:
                items.append(item)

        splitOpLine = lines[i+2].split('=')
        operation = splitOpLine[1].strip()

        testValue = lines[i+3].strip().split(' ')[3]
        trueMonkey = lines[i+4].strip().split(' ')[5]
        falseMonkey = lines[i+5].strip().split(' ')[5]

        monkeys.append(Monkey(monkeyNumber, items, operation, testValue, trueMonkey, falseMonkey))

# Calculate lcm for Part 2
lcm = 1
for m in monkeys:
    lcm *= int(m.test)

numRounds = 10000 # Part 1 is 20 rounds
currMonkeyIndex = 0
for r in range(numRounds * len(monkeys)):
    currMonkey = monkeys[currMonkeyIndex]
    # print(vars(currMonkey))
    while (currMonkey.items):
        #print('Current Monkey ' + str(currMonkey.number) + ' on item: ' + str(currMonkey.items[0]))
        worryLevel = int(currMonkey.items[0])
        currMonkey.inspects += 1
    
        opSplit = currMonkey.operation.split(' ')
        operand = worryLevel if opSplit[2] == 'old' else int(opSplit[2])
        if opSplit[1] == '*':
           worryLevel *= operand
        else:
            worryLevel += operand

        # part 1 mod
        #worryLevel //= 3
        worryLevel = worryLevel % lcm

        if worryLevel % int(currMonkey.test) == 0:
            monkeys[int(currMonkey.trueMonkey)].items.append(worryLevel)
        else:
            monkeys[int(currMonkey.falseMonkey)].items.append(worryLevel)
        currMonkey.items.pop(0)


    currMonkeyIndex = (currMonkeyIndex + 1) % len(monkeys)

inspectsList = list()
for m in monkeys:
    inspectsList.append(m.inspects)
inspectsList.sort()
print(inspectsList[-1] * inspectsList[-2])

    
        

