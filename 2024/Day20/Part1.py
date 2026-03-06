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
                state = (nr, nc, dr, dc)

                if state not in visited or new_step < visited[state]:
                    visited[state] = new_step
                    heapq.heappush(pq, (new_step, nr, nc))
    return -1


origin = solve_maze(grid, s, e)
for wall in walls:
    new_grid = grid
    new_grid[wall[0]][wall[1]] = "."
    new_speed = solve_maze(new_grid, s, e)
    if new_speed < origin:
        save = origin - new_speed
        if save >= 100:
            ans += 1
print(ans)
