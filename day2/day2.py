f = open('InDay2.txt', 'r')

total = 0

arr = f.readline().split("\n")

for line in arr:
    val = line.split(" ")
    if val[0] == val[1]:
        total += 1
