from Util import read_input

data = read_input(1, True)
leftList = []
rightList = []
for line in data:
    nums = line.split("  ")
    leftList.append(int(nums[0]))
    rightList.append(int(nums[1]))

rightList.sort()
leftList.sort()

memo = {}
result = 0
for left in leftList:
    count = 0
    if left not in memo:
        for right in rightList:
            if right  == left:
                count += 1
        memo[left] = count
        result += memo[left] * left
    elif left in memo:
        result += left * memo[left]


print(result)