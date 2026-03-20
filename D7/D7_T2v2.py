import numpy as np

# read in file
file1 = open('C:\\Users\\janso\\Desktop\\VA\\Algoritmi_2\\D7\\D7_INPUT.txt', 'r')
arrInit = []
for line in file1:
    arrInit.append(list(line.replace('\n', '')))

# Initialize a dictionary with a set for each line
arr = {}
arr2 = {}
i = 0
while i < len(arrInit):
    arr[i] = []
    arr2[i] = []
    i +=1

# For each line store indices of each splitter
i = 0
j = 0
while i < len(arrInit):
    j = 0
    while j < len(arrInit[0]):
        if arrInit[i][j] != '.':
            arr[i].append(j)
        j += 1
    i +=1

# Last row - splitters have no children so two paths
for ele in arr[len(arr) - 2]:
    arr2[len(arr) - 2].append((ele, 2))


i = len(arr) - 4
j = i + 2
counter = 0
childCnt = 0
leftSet = False
rightSet = False
while i >= 0:
    leftSet = False
    rightSet = False
    counter = 0
    childCnt = 0
    j = i + 2
    if(len(arr[i]) == 0):
        i -= 1
        continue
    
    for ele in arr[i]:
        j = i + 2
        counter = 0
        childCnt = 0
        leftSet = False
        rightSet = False
        while True:
            for chld in arr2[j]:
                if childCnt == 2:
                    break
                if chld[0] == ele - 1 and not leftSet:
                    counter += chld[1]
                    childCnt += 1
                    leftSet = True
                if chld[0] == ele + 1 and not rightSet:
                    counter += chld[1]
                    childCnt += 1
                    rightSet = True
            if j == len(arr) - 2:
                break
            if childCnt == 2:
                break
            j += 2
        arr2[i].append((ele, counter + 2 - childCnt))
    

    i -= 1

print(counter)
x = 5