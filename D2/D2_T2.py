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
        k = str(x)
        counter = 1
        while (len(k) / 2 >= counter):
            indices = list(range(0,len(k), counter))
            parts = [k[i:j] for i,j in zip(indices, indices[1:]+[None])]
            if len(set(parts)) == 1:
                sum += x
                # don't double count
                break
            counter +=1
            # early exit here to prevent it raising counter pointlessly
            if len(k) / 2 < counter: break
            while (len(k) % counter != 0):
                counter +=1 

print (sum)