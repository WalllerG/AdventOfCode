import re
with open("input.txt") as f:
    data = f.read().splitlines()
cur_x = 1
cur_cycle = 0
draws = []
height = 0
line2draw = []
cycle_len = 40
for line in data:
    if height == 6:
        break
    x_pos = [cur_x - 1, cur_x, cur_x + 1]
    num = re.findall(r'-?\d+', line)
    if len(num) != 0:
        for i in range(2):
            if cur_cycle == cycle_len:
                draws.append(line2draw)
                line2draw = []
                height += 1
                cur_cycle = 0
            if cur_cycle not in x_pos:
                line2draw.append(".")
            else:
                line2draw.append("#")
            cur_cycle += 1
        cur_x += int(num[0])
    else:
        if cur_cycle in x_pos:
            line2draw.append("#")
        else:
            line2draw.append(".")
        cur_cycle += 1
        if cur_cycle == cycle_len:
            draws.append(line2draw)
            line2draw = []
            height += 1
            cur_cycle = 0
for draw in draws:
    print(*draw)