with open("input.txt") as f:
    data = list(f.read().split("\n"))
def ogr(index, nums):
    zeros = []
    ones = []
    for num in nums:
        if num[index] == "0":
            zeros.append(num)
        else:
            ones.append(num)
    if len(nums) == 1:
        return int(nums[0], 2)
    elif len(zeros) == len(ones):
        return ogr(index, ones)
    elif len(zeros) > len(ones):
        return ogr(index+1, zeros)
    else:
        return ogr(index+1, ones)
def CO2(index, nums):
    zeros = []
    ones = []
    for num in nums:
        if num[index] == "0":
            zeros.append(num)
        else:
            ones.append(num)
    if len(nums) == 1:
        return int(nums[0], 2)
    elif len(zeros) == len(ones):
        return CO2(index + 1, zeros)
    elif len(zeros) < len(ones):
        return CO2(index + 1, zeros)
    else:
        return CO2(index + 1, ones)
print(CO2(0, data) * ogr(0, data))

