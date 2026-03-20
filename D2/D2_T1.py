file1 = open('D2\D2_T1_INPUT.txt', 'r')

arr = []

for line in file1:
    for x in line.split(','):
        arr.append(x)

sum = 0
substr = ''
counter = 1

for z in arr:
    (i, j) = z.split('-')
    for x in range(int(i), int(j), 1):
        strLenModulo = len(str(x)) % 2
        if strLenModulo == 0:
            strMiddleSliceIndex = int(len(str(x))/2)
            leftSlice = str(x)[:strMiddleSliceIndex]
            rightSlice = str(x)[strMiddleSliceIndex:]
            if leftSlice == rightSlice:
                sum +=x

print (sum)