f = open('InDay5.txt', 'r')

inStack = []
l = f.readline()
while not(l[1].isdigit()):
    inStack.append(l.replace("\n", ''))
    l = f.readline()

test = list(filter(lambda x: x.isdigit(), l))
length = len(test)
pStack = [[] for x in range(0, length)]

for string in inStack:
    arr = list(string)
    for x in range(0, len(string)):
        if arr[x].isalpha():
            pStack[int(x / 4)].insert(0, arr[x])

ta = f.readline()

for line in f:
    lArr = list(filter(lambda a: a.isnumeric(), line.replace("\n", '').split(" ")))
    cnt = int(lArr[0])
    orig = pStack[int(lArr[1])-1]
    dest = pStack[int(lArr[2])-1]
    for y in range(0, cnt):
        if orig:
            elem = orig.pop()
            if elem is not None:
                dest.append(elem)
        elem = None

print("Day5 first star: ", end="")
for x in range(0, len(pStack)):
    if pStack[x]:
        print(str((pStack[x])[len(pStack[x])-1]), end="")


f = open("InDay5.txt", 'r')



inStack = []
l = f.readline()
while not(l[1].isdigit()):
    inStack.append(l.replace("\n", ''))
    l = f.readline()

test = list(filter(lambda x: x.isdigit(), l))
length = len(test)
pStack = [[] for x in range(0, length)]

for string in inStack:
    arr = list(string)
    for x in range(0, len(string)):
        if arr[x].isalpha():
            pStack[int(x / 4)].insert(0, arr[x])

ta = f.readline()

for line in f:
    lArr = list(filter(lambda a: a.isnumeric(), line.replace("\n", '').split(" ")))
    cnt = int(lArr[0])
    orig = pStack[int(lArr[1]) - 1]
    dest = pStack[int(lArr[2]) - 1]
    if len(orig) < cnt:
        cnt = len(orig)
    if cnt != 0:
        st = orig[len(orig)-cnt:]
        pStack[int(lArr[1]) - 1] = orig[0:len(orig)-cnt]
        dest.extend(st)

print("\nDay5 second star: ", end="")
for x in range(0, len(pStack)):
    if pStack[x]:
        print(str((pStack[x])[len(pStack[x])-1]), end="")