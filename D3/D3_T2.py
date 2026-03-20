file1 = open('D3\D3_INPUT.txt', 'r')

arr = []

for line in file1:
    arr.append(line.replace('\n', ''))

counter = 0

linecntr = 0

numArr = [[-1,-1]] * 12

sum = 0

for bank in arr:
    numArr = [[-1,-1]] * 12
    counter = 0
    test = len(bank)
    for batt in bank:
        counterTwo = 0
        for ele in numArr:
            if ele[1] >= counter: break
            if int(ele[0]) < int(batt) and int(ele[1]) < counter and counter + 12 - counterTwo - 1 < len(bank):
                numArr = numArr[:counterTwo] + [[x, counter + i] for i, x in enumerate(bank[(counter) : (counter + 12 - counterTwo)], 0)]
                break
            counterTwo +=1

        counter +=1
    sum += int(''.join([str(j[0]) for j in numArr]))

print(sum)