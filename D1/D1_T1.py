file1 = open('D1_T1_INPUT.txt', 'r')

arr = []

for line in file1:
    arr.append(line.replace('\n', ''))

startPos = 50;
counter = 0;

for rot in arr:
    if rot[0:1] == 'L':
        startPos -= int(rot[1:])
    elif rot[0:1] == 'R':
        startPos += int(rot[1:])
    while (startPos < 0 or startPos > 99):
        if startPos < 0:
            startPos += 100
        elif startPos > 99:
            startPos -= 100
    
    if startPos == 0: counter+=1

print(counter)