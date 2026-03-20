file1 = open('D3\D3_INPUT.txt', 'r')

arr = []

for line in file1:
    arr.append(line.replace('\n', ''))

largestOne = 0
largestTwo = 0

counter = 0

linecntr = 0

sum = 0

for bank in arr:
    largestOne = 0
    largestTwo = 0
    counter = 0
    bank_iter = iter(bank)
    for batt in bank_iter:
        if counter == 0:
            largestOne = batt
            largestTwo = bank[counter+1:counter+2]
            counter +=1
            continue

        if int(largestOne) < int(batt) and counter+1 < len(bank):
            largestOne = batt
            largestTwo = bank[counter+1:counter+2]
            if largestTwo > largestOne:
                counter +=1
                continue
            next(bank_iter)
            counter +=1
        elif int(largestTwo) < int(batt):
            largestTwo = batt
        counter +=1
    sum += int(str(largestOne) + str(largestTwo))

print(sum)