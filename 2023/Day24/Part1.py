from Util.util import read_input
data = read_input = read_input(True)
from z3 import *
least = 200000000000000
most = 400000000000000
ans = 0

hailstones = []
for i in range(len(data)):
    pos, velocity = data[i].split(" @ ")
    x, y, z = [int(x) for x in pos.split(", ")]
    vx, vy, vz = [int(x) for x in velocity.split(", ")]
    hailstones.append(((x, y, z), (vx, vy, vz)))

def solve(s1,s2):
    (x1, y1, _), (dx1, dy1, _) = s1
    (x2, y2, _), (dx2, dy2, _) = s2

    t1, t2 = Reals('t1 t2')
    solver = Solver()
    nx = x1 + dx1 * t1
    ny = y1 + dy1 * t1

    solver.add(nx == x2 + dx2 * t2)
    solver.add(ny == y2 + dy2 * t2)
    solver.add(t1 >= 0, t2 >= 0)
    solver.add(nx >= least, nx <= most)
    solver.add(ny >= least, ny <= most)

    return 1 if solver.check() == sat else 0

for i in range(len(hailstones)):
    for j in range(i + 1, len(hailstones)):
        ans += solve(hailstones[i], hailstones[j])
print(ans)




