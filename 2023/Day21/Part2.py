from collections import deque
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

size = len(grid)
steps = 26501365

def solve(s, target):
    garden_plots = set()
    seen = {(s[0], s[1])}
    q = deque([(s[0], s[1], target)])
    while q:
        x, y, step = q.popleft()
        if step % 2 == 0:
            garden_plots.add((x, y))
        if step == 0:
            continue
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= len(grid) or ny < 0 or ny >= len(grid[0]) or grid[nx][ny] == "#" or (nx, ny) in seen:
                continue
            seen.add((nx, ny))
            q.append((nx, ny, step - 1))
    return len(garden_plots)

grid_width = steps // size - 1
odd = (grid_width // 2 * 2 + 1) ** 2
even = ((grid_width + 1) // 2 * 2) ** 2
coner_t = solve((size-1,  start[1]), size -1 )
coner_r = solve((start[0], 0), size -1)
coner_b = solve((0, start[1]), size -1)
coner_l = solve((start[0], size -1), size -1)
small_tr = solve((size -1, 0), size // 2 -1)
small_tl = solve((size -1, size -1), size // 2 -1)
small_br = solve((0, 0), size // 2 -1)
small_bl = solve((0, size -1), size // 2 -1)
long_tr = solve((size -1, 0), size * 3 // 2 -1)
long_tl = solve((size -1, size -1), size * 3 // 2 -1)
long_br = solve((0, 0), size * 3// 2 -1)
long_bl = solve((0, size -1), size * 3 // 2 -1)
odd_points = solve(start, size*2+1)
even_points = solve(start, size*2)

print(
    odd * odd_points +
    even * even_points +
    coner_t + coner_r + coner_b + coner_l +
    (grid_width + 1) * (small_tr + small_tl + small_br + small_bl) +
    grid_width * (long_tr + long_tl + long_br + long_bl)
)

