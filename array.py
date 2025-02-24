def moveLast(numList):
    for i in range (numList.count(numList[0])):
        a = numList[0]
        for i in numList:
            if i != numList[0]:
                i.extend(a)
    return i

arrayList = [0, 1, 0, 3, 12]
print(moveLast(arrayList))
