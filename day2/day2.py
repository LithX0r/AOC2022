f = open('InDay2.txt', 'r')
total = 0
for line in f:
    val = line.replace('\n', "").split(' ')
    if ord(val[0]) - ord('A') == ord(val[1]) - ord('X'):
        total += 3
    elif (val[0] == 'A' and val[1] == 'Y') or (val[0] == 'B' and val[1] == 'Z') or (val[0] == 'C' and val[1] == 'X'):
        total += 6
    else:
        total += 0
    total += ord(val[1]) - ord('X') + 1
f.close()

print("Day2 first star: " + str(total))

g = open('InDay2.txt', 'r')
total = 0

for line in g:
    val = line.replace('\n', "").split(' ')
    res = (ord(val[1]) - ord('X'))*3
    total += res
    if res == 6:
        total += (ord(val[0]) - ord('A') + 1) % 3 + 1
    elif res == 3:
        total += ord(val[0]) - ord('A') +1
    else:
        total += (ord(val[0]) - ord('A') - 1) % 3 + 1

print("Day2 second star: " + str(total))
g.close()

