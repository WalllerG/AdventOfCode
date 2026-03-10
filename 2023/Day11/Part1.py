import heapq

from Util.util import read_input
data = read_input(True)

galaxies = []
grid = []
ans = 0

for i in range(len(data)):
    row = list(data[i])
    for j in range(len(row)):
        if row[j] == "#":
            galaxies.append([i, j])
    grid.append(row)

m = len(grid)
n = len(grid[0])

count = 0
for i in range(len(grid)):
    if set(grid[i]) == {"."}:
        for g in galaxies:
            if g[0] > i + count:
                g[0] += 1
        m += 1
        count += 1

count = 0
cols = list(zip(*grid))
for i in range(len(cols)):
    if set(cols[i]) == {"."}:
        for g in galaxies:
            if g[1] > i + count:
                g[1] += 1
        n += 1
        count += 1


def find_path(start,end):
    queue = [(start, 0)]
    path = {}
    while queue:
        [x, y], steps = heapq.heappop(queue)
        if [x, y] == end:
            return steps
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n:
                new_steps = steps + 1
                state = (nx, ny)
                if state not in path or new_steps < path[state]:
                    path[state] = new_steps
                    heapq.heappush(queue, ([nx, ny], new_steps))
    return -1

for i in range(len(galaxies)-1):
    for j in range(i+1, len(galaxies)):
        ans += abs(galaxies[i][0]-galaxies[j][0]) + abs(galaxies[i][1]-galaxies[j][1])
print(ans)




