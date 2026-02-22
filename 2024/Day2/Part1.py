from Util.util import read_input

data = read_input(2, True)

result = 0
for line in data:
    nums = line.split(" ")
    increase = int (nums[0]) < int (nums[1])
    decrease = int (nums[0]) > int (nums[1])
    safe = True
    for i in range (0,len(nums)-1):
        if decrease:
            if int (nums[i]) > int (nums[i+1]):
                if int(nums[i]) - int(nums[i+1]) < 1 or int (nums[i]) -int (nums[i+1]) > 3:
                    safe = False
                    break
            else:
                safe = False
                break
        elif increase:
            if int (nums[i]) < int (nums[i+1]):
                if int (nums[i+1]) - int(nums[i]) > 3 or int (nums[i+1]) -int (nums[i]) < 1:
                    safe = False
                    break
            else:
                safe = False
                break
    if safe:
        result += 1
print(result)