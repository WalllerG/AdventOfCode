import heapq
with open("input.txt") as f:
    data = f.read().split("\n")
grid = [list(map(int, line)) for line in data]
s = (0,0)
e = (len(grid)-1,len(grid[0])-1)
def bfs(sx, sy, ex, ey):
    queue = [(sx,sy, 0)]
    seen = {(sx,sy):0}
    while queue:
        cx, cy, risk = heapq.heappop(queue)
        if (cx,cy) == (ex, ey):
            return risk
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                new_risk = risk + grid[nx][ny]
                state = (nx, ny)
                if state not in seen or new_risk < seen[state]:
                    heapq.heappush(queue, (nx, ny, new_risk))
                    seen[state] = new_risk
    return -1
print(bfs(0,0, e[0], e[1]))