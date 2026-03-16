from Util.util import read_input
data = read_input = read_input(True)
import sympy
hailstones = []
for i in range(len(data)):
    pos, velocity = data[i].split(" @ ")
    x, y, z = [int(x) for x in pos.split(", ")]
    vx, vy, vz = [int(x) for x in velocity.split(", ")]
    hailstones.append(((x, y, z), (vx, vy, vz)))

def solve(stones):
    equation = []
    xr, yr, zr, vxr, vyr, vzr = sympy.symbols("xr, yr, zr, vxr, vyr, vzr")
    for (sx, sy, sz),(vx, vy, vz) in stones:
        equation.append((xr - sx) * (vy - vyr) - (yr - sy) * (vx - vxr))
        equation.append((yr- sy) * (vz - vzr) - (zr - sz) * (vy - vyr))
    ans = sympy.solve(equation)
    return ans[0][xr] + ans[0][yr] + ans[0][zr]

print(solve(hailstones))








