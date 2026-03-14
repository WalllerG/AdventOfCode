from Util.util import read_input
data = read_input(True)

start = ()
grid = []
for i in range(len(data)):
    row = list(data[i])
    for j in range(len(row)):
        if row[j] == "S":
            start = (i, j)
    grid.append(row)

def solve(gr, s, target):
    garden_plots = set()
    garden_plots.add((0, s[0],s[1]))
    q = [(0, start[0],start[1])]
    while q:
        step, x, y = q.pop(0)
        if step == target:
            continue
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(gr) and 0 <= ny < len(gr[0]) and gr[nx][ny] != "#":
                new_step = step + 1
                state = (new_step, nx, ny)
                garden_plots.add(state)
                if state not in q:
                    q.append(state)
        garden_plots.remove((step, x, y))
    return len(garden_plots)

print(solve(grid, start, 64))




