file1 = open('D4\D4_INPUT.txt', 'r')

arr = []

for line in file1:
    arr.append(line.replace('\n', ''))

rollCounter = 0
lineCounter = 0

lenLine = len(arr[0])

for line in arr:
    i = 0

    for roll in line:

        nearbyRolls = 0
        if roll =='@':
            # Check current line
            if len(line) > i + 1: 
                if line[i+1] == '@': nearbyRolls += 1
            if i - 1 >= 0:
                if line[i-1] == '@': nearbyRolls += 1
            # Above line
            if lineCounter > 0:
                if len(arr[lineCounter - 1]) > i + 1: 
                    if arr[lineCounter - 1][i+1] == '@': nearbyRolls += 1
                if i - 1 >= 0:
                    if arr[lineCounter - 1][i-1] == '@': nearbyRolls += 1
                if arr[lineCounter - 1][i] == '@': nearbyRolls += 1
            # Below line
            if lineCounter + 1 < len(arr):
                if len(arr[lineCounter + 1]) > i + 1: 
                    if arr[lineCounter + 1][i+1] == '@': nearbyRolls += 1
                if i - 1 >= 0:
                    if arr[lineCounter + 1][i-1] == '@': nearbyRolls += 1
                if arr[lineCounter + 1][i] == '@': nearbyRolls += 1
            if nearbyRolls < 4: rollCounter += 1
        i +=1
    
    lineCounter += 1

print(rollCounter)