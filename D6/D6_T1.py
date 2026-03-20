file1 = open('D6\D6_INPUT.txt', 'r')

arr = []

for line in file1:
    arr.append(line.replace('\n', ''))

i = 0
j = 0

homework = []

while i < len(arr):
    arr[i] = arr[i].split(' ')
    j = 0
    while j < len(arr[i]):
        if arr[i][j] == '':
            del arr[i][j]
            j -=1
        j+=1
    i +=1

i = 0
while i < len(arr[0]):
    temp = []
    j = 0
    while j < len(arr):
        temp.append(arr[j][i])
        j += 1
    homework.append(temp)
    i +=1

grandTotal = 0

for line in homework:
    if line[4] == '+':
        grandTotal += int(line[0]) + int(line[1]) + int(line[2]) + int(line[3])
    elif line[4] == '*':
        grandTotal += int(line[0]) * int(line[1]) * int(line[2]) * int(line[3])

print (grandTotal)