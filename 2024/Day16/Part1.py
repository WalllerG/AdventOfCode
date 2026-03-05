from Util.util import read_input
import heapq

data = read_input(16,True)


results = []
grid = []
s = ()
e = ()

for i in range(len(data)):
    lst = list(data[i])
    row = []
    for j in range(len(lst)):
        row.append(lst[j])
        if lst[j] == 'S':
            s = (i,j)
        if lst[j] == 'E':
            e = (i,j)
    grid.append(row)


def solve_with_counts(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    pq = [(0, 0, 0, start[0], start[1], 0, 0)]
    visited = {}

    while pq:
        cost, turns, steps, r, c, ldr, ldc = heapq.heappop(pq)

        if (r, c) == end:
            return {"cost": cost, "turns": turns, "steps": steps}

        for dr, dc in [ (0, 1), (1, 0),(0, -1), (-1, 0)]:
            nr, nc = r + dr, c + dc

            if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] != "#":
                is_turn = (ldr, ldc) != (0, 0) and (ldr, ldc) != (dr, dc)

                new_turns = turns + (1 if is_turn else 0)
                new_steps = steps + 1

                new_cost = (new_turns * 1000) + new_steps

                state = (nr, nc, dr, dc)

                if state not in visited or new_cost < visited[state]:
                    visited[state] = new_cost
                    heapq.heappush(pq, (new_cost, new_turns, new_steps, nr, nc, dr, dc))

    return None

print(solve_with_counts(grid, s, e))


