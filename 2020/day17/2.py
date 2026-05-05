from itertools import product
import time
from copy import deepcopy
with open('input.txt')as f:
    data = f.read().splitlines()

start_time = time.time()
R = len(data)
C = len(data[0])

actives = set((x, y, 0, 0) for y in range(C) for x in range(R) if data[x][y] == '#')
inactives = set((x, y, 0, 0) for y in range(C) for x in range(R) if data[x][y] == '.')
cycle = 0

while cycle < 6:

    active_copy = deepcopy(actives)

    for x, y, z, w in actives:
        count = 0
        for dx, dy, dz, dw in product([0,1,-1], repeat=4):
            if (dx, dy, dz, dw) != (0,0,0,0):
                nx, ny, nz, nw = x + dx, y + dy, z + dz, w + dw
                if (nx, ny, nz, nw) in actives:
                    count += 1
                elif (nx, ny, nz, nw) not in actives and (nx, ny, nz, nw) not in inactives:
                    inactives.add((nx, ny, nz, nw))
        if count == 2 or count == 3:
            continue
        else:
            active_copy.remove((x, y, z, w))
            inactives.add((x, y, z, w))

    inactive_copy = deepcopy(inactives)

    for x, y, z, w in inactives:
        count = 0
        for dx, dy, dz, dw in product([0,1,-1], repeat=4):
            if (dx, dy, dz, dw) != (0,0,0,0):
                nx, ny, nz, nw = x + dx, y + dy, z + dz, w + dw
                if (nx, ny, nz, nw) in actives:
                    count += 1
        if count == 3:
            inactive_copy.remove((x, y, z, w))
            active_copy.add((x, y, z, w))

    actives = active_copy
    inactives = inactive_copy
    
    cycle += 1

print(f'time: {time.time()-start_time}')
print(len(actives))

