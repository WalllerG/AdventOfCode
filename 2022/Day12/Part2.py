import string
from collections import deque
with open("input.txt") as f:
    data = f.read().split("\n")
vals = {char: i + 1 for i, char in enumerate(string.ascii_lowercase)}
vals["S"] = 1
vals["E"] = 26
grid = []
e = ()
ans = float("inf")
start_pos = set()
for i in range(len(data)):
    rows =  list(data[i])
    for j in range(len(rows)):
        if rows[j] == "S" or rows[j] == "a":
            start_pos.add((i, j))
        if rows[j] == "E":
            e = (i,j)
    grid.append(rows)

def bfs(start, end):
    queue = deque([(start, 0)])
    seen = {start}
    while queue:
        (x, y), step = queue.popleft()
        if (x, y) == end:
            return step
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and vals[grid[x][y]] - vals[grid[nx][ny]] >= -1:
                new_step = step + 1
                state = (nx, ny)
                if state not in seen:
                    seen.add(state)
                    queue.append(((nx, ny), new_step))
    return -1
for pos in start_pos:
    steps = bfs(pos, e)
    if ans > steps >= 0:
        ans = steps
print(ans)