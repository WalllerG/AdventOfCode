import copy
from functools import lru_cache
from Util.util import read_input
data = read_input(True)
ans = 0


@lru_cache(None)
def divide(s,goal):
    result = 0
    if not goal:
        return 0 if "#" in s else 1
    if not s:
        return 0
    if s[0] == ".":
        return divide(s[1:], goal)
    if s[0] == "#":
        g_size = goal[0]
        if len(s) < g_size:
            return 0
        if "." in s[:g_size]:
            return 0
        if len(s) > g_size and s[g_size] == "#":
            return 0
        return divide(s[g_size+1:], goal[1:])
    result += divide("."+s[1:], goal) + divide("#"+s[1:], goal)
    return result




for line in data:
    unknown, target = line.split(" ")
    uc = unknown
    nums = [int(x) for x in target.split(",")]
    num_copy = copy.deepcopy(nums)
    for i in range(4):
        unknown += "?"
        unknown += uc
        nums += num_copy
    nums = tuple(nums)
    ans += divide(unknown, nums)

print(ans)




