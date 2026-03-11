from Util.util import read_input
import heapq
data = read_input(True)
grid = [list(line) for line in data]

s = (0, 0)
e = (len(grid)-1, len(grid[0])-1)

def solve_maze(gr, end):
    pq = [(0, 0, 0, 0, 1, 0), (0, 0, 0, 1, 0, 0)]
    visited = set()

    while pq:
        loss, r, c, dr, dc, n = heapq.heappop(pq)

        if (r, c) == end:
            return loss

        state = (r, c, dr, dc, n)
        if state in visited:
            continue
        visited.add(state)

        if n < 4:
            nr, nc = r + dr, c + dc
            if 0 <= nr < len(gr) and 0 <= nc < len(gr[0]):
                heapq.heappush(pq, (loss + int(gr[nr][nc]), nr, nc, dr, dc, n + 1))
        elif 4 <= n < 10:
            nr, nc = r + dr, c + dc
            if 0 <= nr < len(gr) and 0 <= nc < len(gr[0]):
                heapq.heappush(pq, (loss + int(gr[nr][nc]), nr, nc, dr, dc, n + 1))
            for ndr, ndc in [(dc, dr), (-dc, -dr)]:
                nr, nc = r + ndr, c + ndc
                if 0 <= nr < len(gr) and 0 <= nc < len(gr[0]):
                    heapq.heappush(pq, (loss + int(gr[nr][nc]), nr, nc, ndr, ndc, 1))
        elif n == 10:
            for ndr, ndc in [(dc, dr), (-dc, -dr)]:
                nr, nc = r + ndr, c + ndc
                if 0 <= nr < len(gr) and 0 <= nc < len(gr[0]):
                    heapq.heappush(pq, (loss + int(gr[nr][nc]), nr, nc, ndr, ndc, 1))
    return -1

print(solve_maze(grid,e))