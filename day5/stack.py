f = open('InDay5.txt', 'r')

def push(stack, element):
    stack.append(element)

def pop(stack):
    if stack:
        elem = stack[-1:][0]
        stack.remove(stack[-1:][0])
        return elem
    pass

def check(stack, c, o, d):
    lst = [len(stack[x]) for x in range(0, len(stack))]

    if lst[o] < c:
        c = lst[o]
    lst[o] -= c
    lst[d] += c
    return lst

i = 1
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
i = 0
for line in f:
    lArr = list(filter(lambda a: a.isdigit(), line))
    if i == 13:
        print("")
    cnt = int(lArr[0])
    orig = pStack[int(lArr[1])-1]
    dest = pStack[int(lArr[2])-1]
    lst = check(pStack, cnt, int(lArr[1])-1, int(lArr[2])-1)
    for y in range(0, cnt):
        if orig:
            elem = orig.pop()
            if elem is not None:
                dest.append(elem)
                if dest[-1] is not elem:
                    print("false")
        elem = None
    for l in range(0, len(pStack)):
        if len(pStack[l]) != lst[l]:
            print(str(i))
    i += 1

print("Day5 first star: ", end="")
for x in range(0, len(pStack)):
    if pStack[x]:
        print(str((pStack[x])[len(pStack[x])-1]), end="")
