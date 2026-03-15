from Util.util import read_input
data = read_input(True)
grid = [list(line) for line in data]
start = (0,1)
end = (len(grid)-1, len(grid[0])-2)

points = [start, end]
for i in range(len(grid)):
    for j in range(len(grid[0])):
        neighbour = 0
        if grid[i][j] != "#":
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = i + dx, j + dy
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] != "#":
                    neighbour += 1
            if neighbour >= 3:
                points.append((i, j))

graph = {pt: {} for pt in points}
for sx, sy in points:
    stack = [(0, sx, sy)]
    seen = {(sx, sy)}
    while stack:
        n, x, y = stack.pop()
        if n != 0 and (x,y) in points:
            graph[(sx,sy)][(x,y)] = n
            continue
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] != "#" and (nx, ny) not in seen:
                stack.append((n+1,nx,ny))
                seen.add((nx, ny))

seen = set()
def dfs(pt):
    if pt == end:
        return 0
    m = float("-inf")
    seen.add(pt)
    for nx in graph[pt]:
        if nx not in seen:
            m = max(m, dfs(nx) + graph[pt][nx])
    seen.remove(pt)
    return m
print(dfs(start))






