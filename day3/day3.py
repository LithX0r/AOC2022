f = open('InDay3.txt', 'r')

total = 0

for line in f:
    l = line[0:-1]
    cutoff = int(len(l)/2)
    comp1 = set(l[0:cutoff])
    comp2 = set(l[cutoff:len(l)])
    cur = list(comp1.intersection(comp2))[0]
    if ord(cur) <= ord("Z"):
        total += ord(cur) - ord("A") + 27
    else:
        total += ord(cur) - ord("a") + 1
print("Day3 first star: " + str(total))
f.close()

f = open('InDay3.txt', 'r')
total = 0
it = 0
s = []
for line in f:
    line = line[0:-1]
    if it < 3:
        s.append(set(line))
        it += 1
    if it == 3:
        cur = list(s[0].intersection(s[1]).intersection(s[2]))[0]
        it = 0
        s = []
        if ord(cur) <= ord("Z"):
            total += ord(cur) - ord("A") + 27
        else:
            total += ord(cur) - ord("a") + 1
print("Day3 second star: " + str(total))
