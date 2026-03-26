from collections import deque
with open("input.txt") as f:
    data = f.read().split("\n")
grid = [list(map(int, line)) for line in data]
flashes = 0
def increase():
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            grid[i][j] += 1
def get_nines():
    s = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 10:
                s.append((i,j))
    return s
for _ in range(100):
    increase()
    nines = get_nines()
    if len(nines) != 0:
        queue = deque(nines)
        seen = set(nines)
        while queue:
            flashes += 1
            i, j = queue.popleft()
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1), (1,1), (1,-1), (-1,1), (-1,-1)]:
                nx, ny = i + dx, j + dy
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                    if (nx, ny) in seen:
                        continue
                    else:
                        grid[nx][ny] += 1
                        if grid[nx][ny] == 10 and (nx, ny) not in seen:
                            seen.add((nx,ny))
                            queue.append((nx,ny))
            grid[i][j] = 0
print(flashes)