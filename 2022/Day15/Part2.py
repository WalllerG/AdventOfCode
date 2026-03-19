import re
from z3 import *
with open("input.txt") as f:
    data = f.read().split("\n")
sensors = {}
no_beacons = set()
for line in data:
    coors = re.findall(r"-?\d+", line)
    sx, sy, bx, by = coors
    sensor = (int(sx), int(sy))
    beacon = (int(bx), int(by))
    sensors[sensor] = beacon
solver = z3.Solver()
x = Int("x")
y = Int("y")
solver.add(0 <= x)
solver.add(0 <= y)
solver.add(x <= 4000000)
solver.add(y <= 4000000)
for sensor, beacon in sensors.items():
    sx, sy = sensor
    bx, by = beacon
    dist = abs(sx - bx) + abs(sy - by)
    dist_to_dis = abs(x - sx) + abs(y - sy)
    solver.add(dist < dist_to_dis)
if solver.check() == sat:
    m = solver.model()
    print(m[x].as_long() * 4000000 + m[y].as_long())