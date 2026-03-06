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

for i in range(index+1,len(data)):
    line = data[i]
    nums = line.split(",")
    isRightOrder = True
    for j in range(len(nums)-1):
        if nums[j] not in IntMap:
            isRightOrder = False
            break
        elif nums[j+1] not in IntMap[nums[j]]:
            isRightOrder = False
            break
    if isRightOrder:
        index = int (len(nums) / 2)
        result += int (nums[index])


print(result)
