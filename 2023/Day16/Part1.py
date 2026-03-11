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

bouncing(grid, (0, -1, 0, 1))
