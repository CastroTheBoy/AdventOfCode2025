file1 = open('D7\D7_INPUT.txt', 'r')

arr = []

for line in file1:
    arr.append(line.replace('\n', ''))

splitCounter = 0
lineCounter = 0

lenLine = len(arr[0])
while lineCounter < len(arr):
    if lineCounter == 0: 
        lineCounter += 1
        continue
    i = 0

    while i < len(arr[lineCounter]):
        temp = []
        roll = arr[lineCounter][i]
        line = arr[lineCounter]
        if lineCounter == 1:
            while True:
                if arr[lineCounter - 1][i] == 'S':
                    temp = list(arr[lineCounter])
                    temp[i] = '|'
                    arr[lineCounter] = ''.join(temp)
                    lineCounter += 1
                    break
                i += 1
            continue
        
        if arr[lineCounter - 1][i] == '|': 
            if roll =='^':
                splitCounter += 1                    
                temp = list(arr[lineCounter])
                if i + 1 < len(line):
                    temp[i+1] = '|'
                if i - 1 >= 0: 
                    temp[i-1] = '|'
                arr[lineCounter] = ''.join(temp)
            elif roll =='.':
                temp = list(arr[lineCounter])
                temp[i] = '|'
                arr[lineCounter] = ''.join(temp)

        i +=1
    
    lineCounter += 1

print(splitCounter)