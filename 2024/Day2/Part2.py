from Util.util import read_input

data = read_input(2, True)


def is_safe(num: list[int]) -> bool:
    diffs = [num[j + 1] - num[i] for j in range(len(num) - 1)]

    all_increasing = all(1 <= d <= 3 for d in diffs)
    all_decreasing = all(-3 <= d <= -1 for d in diffs)

    return all_increasing or all_decreasing


result = 0
for line in data:
    nums = [int(x) for x in line.split()]

    if is_safe(nums):
        result += 1
    else:
        for i in range(len(nums)):
            dampened_list = nums[:i] + nums[i + 1:]
            if is_safe(dampened_list):
                result += 1
                break

print(result)