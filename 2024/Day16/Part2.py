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

def solve_with_counts(maze, start, end, path=None):
    if path is None:
        path = set()
        path.add(start)


    rows, cols = len(maze), len(maze[0])
    pq = [(0, path, start[0], start[1], 0, 1)]
    visited = {}
    best_ways = []

    while pq:
        cost, path, r, c, ldr, ldc = heapq.heappop(pq)

        if (r, c) == end:
            best_ways.append(path)
            continue

        for dr, dc in [(0, 1), (-1, 0), (0, -1), (1, 0)]:

            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] != "#":

                is_turn = (ldr, ldc) != (dr, dc)

                if is_turn:
                    new_cost = cost + 1001
                else:
                    new_cost = cost + 1

                state = (nr, nc, dr, dc)
                new_path = path.copy()

                if (nr, nc) not in path:
                    new_path.add((nr,nc))

                if state not in visited or new_cost <= visited[state]:
                    visited[state] = new_cost
                    heapq.heappush(pq, (new_cost ,new_path, nr, nc, dr, dc))
    return best_ways

ways = solve_with_counts(grid, s, e)

final_set = ways[0]
for way in ways[1::]:
    final_set = final_set | way

print(len(final_set))
