import heapq
from Util.util import read_input

data = read_input(18, True)
count = 0

grid = []
for i in range(71):
    row = []
    for j in range(71):
        row.append(".")
    grid.append(row)

for coor in data:
    if count == 1024:
        break
    cd = coor.split(",")
    x = int (cd[0])
    y = int (cd[1])
    grid[y][x] = "#"
    count += 1

def solve_maze(maze, start, end):
    row = len(maze)
    col = len(maze[0])
    pq = [(0, start[0], start[1])]
    visited = {}

    while pq:
        steps, r, c = heapq.heappop(pq)

        if (r,c) == end:
            print(steps)
            break

        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < row and 0 <= nc < col and maze[nr][nc] != "#":

                new_step = steps + 1
                state = (nr, nc, dr, dc)

                if state not in visited or new_step < visited[state]:
                    visited[state] = new_step
                    heapq.heappush(pq, (new_step, nr, nc))

solve_maze(grid,(0,0),(70,70))