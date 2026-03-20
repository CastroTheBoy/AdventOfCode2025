import numpy as np

# read in file
file1 = open('C:\\Users\\janso\\Desktop\\VA\\Algoritmi_2\\D7\\D7_INPUT.txt', 'r')
arrInit = []
for line in file1:
    arrInit.append(list(line.replace('\n', '')))

# Initialize a dictionary with a set for each line
arr = {}
i = 0
while i < len(arrInit):
    arr[i] = set()
    i +=1

# For each line store indices of each splitter
i = 0
j = 0
while i < len(arrInit):
    j = 0
    while j < len(arrInit[0]):
        if arrInit[i][j] != '.':
            arr[i].add(j)
        j += 1
    i +=1

# initial var declaration
lineCounter = 2
path = []
pathLineCounters = []
loopCounter = 0
z = next(iter(arr[0]))
i = z
arrLen = len(arr)
exit = False;

# first loop - all lefts
while lineCounter < len(arr):
    if i in arr[lineCounter]:
        path.append(-1)
        pathLineCounters.append(lineCounter)
        i -= 1
    lineCounter += 1

loopCounter += 1

# main loop
while True:
    # Find last Left in previous loop and set the split before it as current start point
    path = path[:len(path) - 1 - path[::-1].index(-1)]
    lineCounter = pathLineCounters.pop()

    # adjust index according to path
    i = z
    i += sum(path)

    # Next split is Right
    while True:
        if i in arr[lineCounter]:
            path.append(1)
            i += 1
            lineCounter += 1
            break
        lineCounter += 1
        
    # Any remaining splits are Left
    while lineCounter < arrLen:
        if i in arr[lineCounter]:
            path.append(-1)
            pathLineCounters.append(lineCounter)
            i -= 1
        lineCounter += 1

    loopCounter += 1

    if loopCounter % 500000 == 0:
        print(loopCounter)
        print(''.join(['L' if x == -1 else 'R' for x in path]))

    if exit: break

print(loopCounter)
print(''.join(['L' if x == -1 else 'R' for x in path]))