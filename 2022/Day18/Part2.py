from collections import deque

with open("input.txt") as f:
    data = f.read().split("\n")
ans = 0
cubes = set()
inside_cubes = set()
for line in data:
    if not line: continue
    cubes.add(tuple(map(int, line.split(","))))
def is_adjacent(c1,c2):
    ax, ay, az = c1
    bx, by, bz = c2
    x_diff = abs(ax - bx)
    y_diff = abs(ay - by)
    z_diff = abs(az - bz)
    if ax == bx and ay == by and z_diff == 1:
        return True
    if ay == by and az == bz and x_diff == 1:
        return True
    if ax == bx and az == bz and y_diff == 1:
        return True
    return False

for x, y, z in cubes:
    neighbors = [
        (x + 1, y, z), (x - 1, y, z),
        (x, y + 1, z), (x, y - 1, z),
        (x, y, z + 1), (x, y, z - 1)
    ]
    for n in neighbors:
        if n not in cubes:
            ans += 1

min_x = min(x for x, y, z in cubes) - 1
max_x = max(x for x, y, z in cubes) + 1
min_y = min(y for x, y, z in cubes) - 1
max_y = max(y for x, y, z in cubes) + 1
min_z = min(z for x, y, z in cubes) - 1
max_z = max(z for x, y, z in cubes) + 1

exterior_surface_area = 0
visited = set()
queue = deque([(min_x, min_y, min_z)])
visited.add((min_x, min_y, min_z))

while queue:
    x, y, z = queue.popleft()
    for dx, dy, dz in [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]:
        nx, ny, nz = x + dx, y + dy, z + dz
        if min_x <= nx <= max_x and min_y <= ny <= max_y and min_z <= nz <= max_z:
            if (nx, ny, nz) in cubes:
                exterior_surface_area += 1
            elif (nx, ny, nz) not in visited:
                visited.add((nx, ny, nz))
                queue.append((nx, ny, nz))
print(exterior_surface_area)