sum = 0
count = 0

file=  open("observations")
for line in file:
    n = int(line)
    sum += n
    count += 1

print(sum/count)