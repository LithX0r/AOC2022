x = open('InDay6.txt', 'r')

res = 0

f = x.readline()
x.close()

for x in range(3, len(f)):
    st = f[x-3: x+1]
    t = st.count(f[x-3])
    t += st.count(f[x-2])
    t += st.count(f[x-1])
    t += st.count(f[x])

    if t == 4:
        res = x+1
        break

print("Day 6 first star: " + str(res))

x = open('InDay6.txt')

f = x.readline()
x.close()

for x in range(13, len(f)):
    st = f[x-13: x+1]
    stl = len(st)
    t = 0
    for y in range(0, 14):
        c = x - y
        t += st.count(f[x-y])

    if t == 14:
        res = x+1
        break

print("Day 6 second star: " + str(res))