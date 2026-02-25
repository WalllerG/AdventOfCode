from Util.util import read_input
data = read_input(5,True)
index = 0
IntMap = {}
while data[index] != "":
    line = data[index]
    pair = line.split("|")
    key = pair[0]
    value = pair[1]
    if key in IntMap:
        IntMap[key].append(value)
    else:
        IntMap[key] = [value]
    index += 1

result = 0

incorrectLists = []

def isCorrect(a,b) -> bool:
    for l in range(len(a) - 1):
        if a[l] not in IntMap:
            return False
        elif a[l + 1] not in b[a[l]]:
            return False
    return True

for i in range(index+1,len(data)):
    line = data[i]
    nums = line.split(",")
    for j in range(len(nums)-1):
        if nums[j] not in IntMap:
            incorrectLists.append(nums)
            break
        elif nums[j+1] not in IntMap[nums[j]]:
            incorrectLists.append(nums)
            break

print(incorrectLists)

for incorrectList in incorrectLists:
    k = 0
    while not isCorrect(incorrectList,IntMap):
        moved = False
        for index in range(k+1,len(incorrectList)):
            if incorrectList[k] not in IntMap:
                val = incorrectList.pop(k)
                incorrectList.insert(len(incorrectList)+1,val)
                moved = True
                break
            if incorrectList[index] not in IntMap:
                val = incorrectList.pop(index)
                incorrectList.insert(len(incorrectLists)+1,val)
                moved = True
                break
            if incorrectList[k] in IntMap[incorrectList[index]]:
                val = incorrectList.pop(k)
                incorrectList.insert(index,val)
                moved = True
        if not moved:
            k = k + 1


print(incorrectLists)

for incorrectList in incorrectLists:
    index = int(len(incorrectList) / 2)
    result += int(incorrectList[index])
print(result)







