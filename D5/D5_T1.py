file1 = open('D5\D5_INPUT.txt', 'r')

arr = []

for line in file1:
    arr.append(line.replace('\n', ''))


ids = []
products = []

count = 0

idsIns = True

for line in arr:
    if line == '':
        idsIns = False
        continue
    if idsIns:
        ids.append(line)
    else:
        products.append(line)


ranges = []

for idRange in ids:
    ranges.append(idRange.split('-'))

for item in products:
    for range in ranges:
        if int(item) >= int(range[0]) and int(item) <= int(range[1]): 
            count += 1
            break

print (count)