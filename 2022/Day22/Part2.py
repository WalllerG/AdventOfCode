import re
with open("input.txt") as f:
    p1, ops = f.read().split("\n\n")
points = {}
for i, line in enumerate(p1.split("\n")):
    row = list(line)
    for j in range(len(row)):
        if row[j] != " ":
            if row[j] == "#":
                points[(i,j)] = 1
            else:
                points[(i,j)] = 0

def get_cube_next(r, c, d):
    dr, dc = [(0, 1), (1, 0), (0, -1), (-1, 0)][d]
    nr, nc, nd = r + dr, c + dc, d

    if (nr, nc) not in points:
        if d == 0:
            if 0 <= r < 50:
                nr, nc, nd = 149 - r, 99, 2
            elif 50 <= r < 100:
                nr, nc, nd = 49, r + 50, 3
            elif 100 <= r < 150:
                nr, nc, nd = 149 - r, 149, 2
            elif 150 <= r < 200:
                nr, nc, nd = 149, r - 100, 3

        elif d == 1:
            if 0 <= c < 50:
                nr, nc, nd = 0, c + 100, 1
            elif 50 <= c < 100:
                nr, nc, nd = c + 100, 49, 2
            elif 100 <= c < 150:
                nr, nc, nd = c - 50, 99, 2

        elif d == 2:
            if 0 <= r < 50:
                nr, nc, nd = 149 - r, 0, 0
            elif 50 <= r < 100:
                nr, nc, nd = 100, r - 50, 1
            elif 100 <= r < 150:
                nr, nc, nd = 149 - r, 50, 0
            elif 150 <= r < 200:
                nr, nc, nd = 0, r - 100, 1

        elif d == 3:
            if 0 <= c < 50:
                nr, nc, nd = c + 50, 50, 0
            elif 50 <= c < 100:
                nr, nc, nd = c + 100, 0, 0
            elif 100 <= c < 150:
                nr, nc, nd = 199, c - 100, 3
    return nr, nc, nd

pattern = re.findall(r'\d+|[a-zA-Z]+', ops)
cur = (0,50)
cur_direction_index = 0
for op in pattern:
    next_move = False
    if op.isdigit():
        for _ in range(int(op)):
            nx, ny, nd = get_cube_next(cur[0], cur[1], cur_direction_index)
            if points[(nx, ny)] == 1:
                break
            else:
                cur = (nx, ny)
                cur_direction_index = nd
    else:
        if op == "R":
            cur_direction_index = (cur_direction_index + 1) % 4
        else:
            cur_direction_index = (cur_direction_index - 1) % 4
print((cur[0] + 1) * 1000 + 4 * (cur[1] + 1) + cur_direction_index)






