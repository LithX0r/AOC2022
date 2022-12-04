f = open('InDay4.txt', 'r')

total = 0

def checkRange(big, little):
    return int(little[0]) - int(big[0]) >= 0 and int(big[1]) - int(little[1]) >= 0


for line in f:
    l = line.replace('\n', '').split(",")
    exp1 = l[0].split("-")
    exp2 = l[1].split("-")
    diff1 = -(int(exp1[0]) - int(exp1[1]))
    diff2 = -(int(exp2[0]) - int(exp2[1]))
    if diff1 >= diff2 and checkRange(exp1, exp2) or diff2 > diff1 and checkRange(exp2, exp1):
        total += 1

print("Day4 first star: " + str(total))
f.close()

f = open('InDay4.txt', 'r')

total = 0

for line in f:
    l = line.replace('\n', '').split(",")
    exp1 = l[0].split("-")
    exp2 = l[1].split("-")
    r1 = set(range(int(exp1[0]), int(exp1[1])+1))
    r2 = set(range(int(exp2[0]), int(exp2[1])+1))
    i = r1.intersection(r2)
    if len(i) != 0:
        total += 1

print("Day4 second star: " + str(total))
f.close()