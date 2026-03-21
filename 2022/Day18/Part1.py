with open("input.txt") as f:
    data = f.read().split("\n")
cubes = set()
for line in data:
    if not line: continue
    cubes.add(tuple(map(int, line.split(","))))

ans = 0
for x, y, z in cubes:
    neighbors = [
        (x + 1, y, z), (x - 1, y, z),
        (x, y + 1, z), (x, y - 1, z),
        (x, y, z + 1), (x, y, z - 1)
    ]
    for n in neighbors:
        if n not in cubes:
            ans += 1
print(ans)