import re

with open("input.txt") as f:
    data = f.read().splitlines()
cycle = 0
prev_x = 1
cur_x = 1
ans = 0
is_add = True
need2add = [20,60,100, 140,180,220]
for line in data:
    if need2add and cycle >= need2add[0]:
        c = need2add.pop(0)
        if is_add:
            ans += prev_x * c
        else:
            ans += c * cur_x
    num = re.findall(r'-?\d+', line)
    if len(num) != 0:
        is_add = True
        prev_x = cur_x
        cur_x += int(num[0])
        cycle += 2
    else:
        is_add = False
        cycle += 1
print(ans)