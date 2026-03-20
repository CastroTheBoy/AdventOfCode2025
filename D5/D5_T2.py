file1 = open('D5\D5_INPUT.txt', 'r')

arr = []

for line in file1:
    arr.append(line.replace('\n', ''))


ids = []
count = 0

for line in arr:
    if line == '':
        break
    ids.append(line)


ranges = []

for idRange in ids:
    ranges.append(idRange.split('-'))

ranges = sorted(ranges, key=lambda x: int(x[0]))
while True:

    itr = 0
    while True:
        joinCount = 0
        if itr +1 < len(ranges) and int(ranges[itr][1]) >= int(ranges[itr + 1][0]) and int(ranges[itr][1]) <= int(ranges[itr + 1][1]):
            ranges[itr] = [ranges[itr][0], ranges[itr + 1][1]]
            joinCount +=1
            del ranges[itr + 1]
            break
        elif itr +1 < len(ranges) and int(ranges[itr][1]) > int(ranges[itr + 1][1]):
            del ranges[itr + 1]
            joinCount +=1
            break
        itr += 1
        if itr == len(ranges): break

    if joinCount == 0: break

for range in ranges:
    count += int(range[1]) - int(range[0]) + 1

print (count)