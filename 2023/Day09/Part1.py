import re

from Util.util import read_input
data = read_input(True)
ans = 0
for line in data:
    history = re.findall(r'-?\d+', line)
    last = int (history[-1])
    last_nums = []
    diff = []
    while set(diff) != {0}:
        diff = [int(history[x+1])-int(history[x]) for x in range(0, len(history)-1)]
        last_nums.append(diff[-1])
        history = diff
    cur = 0
    for i in range(len(last_nums)-2, -1, -1):
        cur += last_nums[i]
    ans += cur + last
print(ans)



