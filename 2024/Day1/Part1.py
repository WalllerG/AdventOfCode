from Util.util import read_input

data = read_input(1, True)
leftList = []
rightList = []
for line in data:
    nums = line.split("  ")
    leftList.append(int(nums[0]))
    rightList.append(int(nums[1]))

rightList.sort()
leftList.sort()

result = 0
for left, right in zip(leftList, rightList):
    result += abs(left - right)
print(result)
