import re
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
for val in sensors.values():
    x, y = val
    if y == 2000000:
        no_beacons.add(val)
for sensor, beacon in sensors.items():
    sx, sy = sensor
    bx, by = beacon
    dis = abs(sx - bx) + abs(sy - by) - 1
    dis2y = abs(sy - 2000000)
    leftover = dis - dis2y
    no_beacons.add((sx,2000000))
    clx = sx
    crx = sx
    for _ in range(leftover):
        clx -= 1
        no_beacons.add((clx,2000000))
    for _ in range(leftover):
        crx += 1
        no_beacons.add((crx,2000000))
