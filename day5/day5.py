f = open('InDay5.txt', 'r')

def push(stack, element):
    stack.append(element)

def pop(stack):
    if stack:
        elem = stack[len(stack)-1]
        stack.remove(elem)
        return elem
    pass

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

for line in f:
    lArr = list(filter(lambda a: a.isdigit(), line))
    for y in range(0, int(lArr[0])):
        push(pStack[int(lArr[2])-1], pop(pStack[int(lArr[1])-1]))
        pStack[int(lArr[1])-1] = (pStack[int(lArr[1])-1])[0:-1]

for x in range(0, len(pStack)):
    if pStack[x]:
        print(str((pStack[x])[len(pStack[x])-1]), end="")



