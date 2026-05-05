from itertools import product
from copy import deepcopy
with open('input.txt')as f:
    data = f.read().splitlines()

R = len(data)
C = len(data[0])

actives = set((x, y, 0) for y in range(C) for x in range(R) if data[x][y] == '#')
inactives = set((x, y, 0) for y in range(C) for x in range(R) if data[x][y] == '.')
cycle = 0

while cycle < 6:

    active_copy = deepcopy(actives)

    for x, y, z in actives:
        count = 0
        for dx, dy, dz in product([0,1,-1], repeat=3):
            if (dx, dy, dz) != (0,0,0):
                nx, ny, nz = x + dx, y + dy, z + dz
                if (nx, ny, nz) in actives:
                    count += 1
                elif (nx, ny, nz) not in actives and (nx, ny, nz) not in inactives:
                    inactives.add((nx, ny, nz))
        if count == 2 or count == 3:
            continue
        else:
            active_copy.remove((x, y, z))
            inactives.add((x, y, z))

    inactive_copy = deepcopy(inactives)

    for x, y, z in inactives:
        count = 0
        for dx, dy, dz in product([0,1,-1], repeat=3):
            if (dx, dy, dz) != (0,0,0):
                nx, ny, nz = x + dx, y + dy, z + dz
                if (nx, ny, nz) in actives:
                    count += 1
        if count == 3:
            inactive_copy.remove((x, y, z))
            active_copy.add((x, y, z))

    actives = active_copy
    inactives = inactive_copy
    
    cycle += 1

print(len(actives))

