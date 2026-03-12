from Util.util import read_input
data = read_input(True)

ans = 0
cx, cy = 0, 0
g = set()
for line in data:
    direction, moves, color = line.split(" ")
    dx, dy = {
        "R": (0, 1),
        "L": (0, -1),
        "U": (-1, 0),
        "D": (1, 0)
    }[direction]
    for _ in range(int(moves)):
        g.add((cx, cy))
        cx += dx
        cy += dy
    g.add((cx, cy))

sx, sy = -4, -3
q = [(sx, sy)]
while len(q) > 0:
    x, y = q.pop()
    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        nx, ny = x + dx, y + dy
        if (nx, ny) not in g:
            g.add((nx, ny))
            q.append((nx, ny))
print(len(g))



