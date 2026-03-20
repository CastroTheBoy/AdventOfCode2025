import re
import math

file1 = open('D6\D6_INPUT.txt', 'r')

arr = []

for line in file1:
    arr.append(line.replace('\n', ''))

i = 0
j = 0

homework = []

colLen = 0

i = 0
while True:
    colLen = 0
    i = 0
    while i < len(arr) -1:
        reg = re.search("^(\s*\d+)", arr[i])
        if reg is None: break
        colLen = len(reg.group()) if len(reg.group()) > colLen  else colLen
        i +=1
    if reg is None: break
    i = 0
    temp = []
    while i < len(arr):
        temp.append(arr[i][:colLen])
        arr[i] = arr[i][colLen + 1:]
        if i == len(arr) - 1:
            temp[i] = temp[i].replace(' ','')
        i +=1
    homework.append((temp, colLen))

homework2 = []

i = 0
while i < len(homework):
    j = 0

    z = 0
    temp = []
    while z < homework[i][1]:
        j = 0
        s = ''
        while j < len(homework[0][0]) - 1:
            s = s + homework[i][0][j][z]
            j +=1
        z+=1
        temp.append(s.replace(' ',''))
    temp.append(homework[i][0][len(homework[i][0]) - 1])
    homework2.append(temp)
    
    i +=1

grandTotal = 0

for line in homework2:
    if line[len(line) - 1] == '+':
        grandTotal += sum([int(x) for x in line[:-1]])
    elif line[len(line) - 1] == '*':
        grandTotal += math.prod([int(x) for x in line[:-1]])

print (grandTotal)