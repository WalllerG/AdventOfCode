from Util.util import read_input
data = read_input = read_input(True)
from z3 import *
least = 200000000000000
most = 400000000000000
hailstones = []
for i in range(len(data)):
    pos, velocity = data[i].split(" @ ")
    x, y, z = [int(x) for x in pos.split(", ")]
    vx, vy, vz = [int(x) for x in velocity.split(", ")]
    hailstones.append(((x, y, z), (vx, vy, vz)))


def solve(stones):
    solver = Solver()
    vars = []
    x = Int('x')
    y = Int('y')
    z = Int('z')
    vx = Int('vx')
    vy = Int('vy')
    vz = Int('vz')
    solver.add(x >= 0)
    solver.add(y >= 0)
    solver.add(z >= 0)
    for i in range(len(stones)):
        t = Int("t{}".format(i))
        vars.append(t)
        (cx, cy, cz), (dx, dy, dz) = stones[i]
        solver.add(cx + dx * t == x + vx * t)
        solver.add(cy + dy * t == y + vy * t)
        solver.add(cz + dz * t == z + vz * t)

    for var in vars:
        solver.add(var >= 0)
    for i in range(len(vars)):
        for j in range(i + 1, len(vars)):
            solver.add(vars[i] != vars[j])

    solver.check()
    m = solver.model()
    x_val = m[x].as_long()
    y_val = m[y].as_long()
    z_val = m[z].as_long()
    return x_val + y_val + z_val

print(solve(hailstones))








