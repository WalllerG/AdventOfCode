import re
from collections import defaultdict
with open("input.txt") as f:
    p1, ops = f.read().split("\n\n")
points = {}
adjacents = {}
for i, line in enumerate(p1.split("\n")):
    row = list(line)
    for j in range(len(row)):
        if row[j] != " ":
            if row[j] == "#":
                points[(i,j)] = 1
            else:
                points[(i,j)] = 0
rows = defaultdict(list)
cols = defaultdict(list)
for r, c in points:
    rows[r].append(c)
    cols[c].append(r)
row_limits = {r: (min(cs), max(cs)) for r, cs in rows.items()}
col_limits = {c: (min(rs), max(rs)) for c, rs in cols.items()}
for x, y in points:
    adj = []
    for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:
        nx, ny = x + dx, y + dy
        if (nx, ny) not in points:
            if dx == 0:
                min_c, max_c = row_limits[x]
                if ny > max_c:
                    ny = min_c
                elif ny < min_c:
                    ny = max_c
            else:
                min_r, max_r = col_limits[y]
                if nx > max_r:
                    nx = min_r
                elif nx < min_r:
                    nx = max_r
            if (nx, ny) in points:
                adj.append((nx, ny))
        else:
            adj.append((nx, ny))
    adjacents[(x,y)] = adj

pattern = re.findall(r'\d+|[a-zA-Z]+', ops)
cur = (0,50)
cur_direction_index = 0
for op in pattern:
    next_move = False
    if op.isdigit():
        for i in range(int(op)):
            next_cur = adjacents[cur][cur_direction_index]
            if points[next_cur] == 1:
                next_move = True
                break
            else:
                cur = next_cur
        if next_move:
            continue
    else:
        if op == "R":
            cur_direction_index = (cur_direction_index + 1) % 4
        else:
            cur_direction_index = (cur_direction_index - 1) % 4
print((cur[0] + 1) * 1000 + 4 * (cur[1] + 1) + cur_direction_index)






