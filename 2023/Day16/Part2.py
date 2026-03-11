from Util.util import read_input
data = read_input(True)

grid = [list(line) for line in data]
travel = set()
def bouncing(gr, start):
    cache = set()
    traveled = set()
    pq = [start]
    while pq:
        x, y, d1, d2 = pq.pop()
        nx, ny = x + d1, y + d2
        state = (nx, ny, d1, d2)
        if not (0 <= nx < len(gr) and 0 <= ny < len(gr[0])):
            continue
        if state in cache:
            continue
        cache.add(state)
        traveled.add((nx, ny))
        char = gr[nx][ny]
        if char == "/":
            pq.append((nx, ny, -d2, -d1))
        elif char == "\\":
            pq.append((nx, ny, d2, d1))
        elif char == "|" and d2 != 0:
            pq.append((nx, ny, 1, 0))
            pq.append((nx, ny, -1, 0))
        elif char == "-" and d1 != 0:
            pq.append((nx, ny, 0, 1))
            pq.append((nx, ny, 0, -1))
        else:
            pq.append((nx, ny, d1, d2))
    return len(traveled)

entries = []
for i in range(0, len(grid)):
    lx, ly  = 0, 1
    rx, ry = 0, -1
    entries.append((i, -1, lx, ly))
    entries.append((i, len(grid[0]), rx, ry))
for i in range(0, len(grid[0])):
    ux, uy = 1, 0
    dx, dy = -1, 0
    entries.append((-1, i, ux, uy))
    entries.append((len(grid), i, dx, dy))

largest = float("-inf")
for entry in entries:
    re = bouncing(grid, entry)
    if re > largest:
        largest = re
print(largest)


