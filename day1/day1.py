f = open('InDay1.txt', 'r')
myList = [0]
i = 0
for line in f:
    if line[0:-2] != "":
        myList[i] += int(line[0:-1])
    else:
        i += 1
        myList.append(0)
myList.sort()
print("Day1 first star: " + str(myList[len(myList) - 1]))
f.close()

sumCal = myList[len(myList) - 1]
if len(myList)-2 >= 0:
    sumCal += myList[len(myList) - 2]
    if len(myList)-3 >= 0:
        sumCal += myList[len(myList) - 3]

print("Day1 second star: " + str(sumCal))
