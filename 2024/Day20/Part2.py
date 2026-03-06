import heapq

from Util.util import read_input

data = read_input(20, True)
grid = []
s = ()
e = ()
walls = set()
ans = 0

for i in range(len(data)):
    r = list(data[i])
    for j in range(len(r)):
        if r[j] == "S":
            s = (i,j)
        elif r[j] == "E":
            e = (i,j)
        elif r[j] == "#":
            walls.add((i,j))
    grid.append(r)


def solve_maze(maze, start, end):
    row = len(maze)
    col = len(maze[0])
    pq = [(0, start[0], start[1])]
    visited = {}

    while pq:
        steps, r, c = heapq.heappop(pq)

        if (r, c) == end:
            return steps

        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < row and 0 <= nc < col and maze[nr][nc] != "#":
                new_step = steps + 1
                state = (nr, nc)

                if state not in visited or new_step < visited[state]:
                    visited[state] = new_step
                    heapq.heappush(pq, (new_step, nr, nc))

    return -1


origin = solve_maze(grid, s, e)

def dist(tempx, tempy):
    dictionary = {}
    for a in range(len(grid)):
        for b in range(len(grid[0])):
            if (a, b) not in dictionary:
                dis = solve_maze(grid, (tempx,tempy), (a,b))
                if dis != -1:
                    dictionary[(a, b)] = dis

    return dictionary

fromStart = dist(s[0],s[1])
fromEnd = dist(e[0],e[1])

for x, y in fromStart.keys():
    for nx, ny in fromEnd.keys():
        if abs(nx-x) + abs(ny-y) <= 20:
            if fromStart[(x,y)] + abs(nx-x) + abs(ny-y)  + fromEnd[(nx,ny)] <= origin - 100:
                ans += 1

print(ans)