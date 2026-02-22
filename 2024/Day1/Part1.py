from Util import read_input

data = read_input(1, False)
leftList = []
rightList = []
for line in data:
    nums = line.split("  ")
    leftList.append(int(nums[0]))
    rightList.append(int(nums[1]))

rightList.sort()
leftList.sort()

result = 0
for i in range(len(leftList)):
    result += abs(leftList[i] - rightList[i])
print(result)
