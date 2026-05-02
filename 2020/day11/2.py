from copy import deepcopy
import time
with open('input.txt')as f:
    grid = f.read().splitlines()

start_time = time.time()
R = len(grid)
C = len(grid[0])

empty = set((r, c) for r in range(R) for c in range(C) if grid[r][c] == 'L')
occupied = set()

def solve(e, o):
    def find_empty_seat(x, y, dx, dy):
        nx, ny = x + dx, y + dy
        count = 1
        while 0 <= nx < R and 0 <= ny < C:
            if (nx, ny) in o:
                return False
            if (nx, ny) in e:
                return True
            count += 1
            nx, ny = x + dx * count, y + dy * count
        return True

    def find_occupied_seat(x, y, dx, dy):
        nx, ny = x + dx, y + dy
        count = 1
        while 0 <= nx < R and 0 <= ny < C:
            if (nx, ny) in o:
                return True
            if (nx, ny) in e:
                return False
            count += 1
            nx, ny = x + dx * count, y + dy * count
        return False

    new_empty = deepcopy(e)
    new_occupied = deepcopy(o)
    for x, y in e:
        for dx, dy in [(-1,-1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
            if not find_empty_seat(x, y, dx, dy):
                break
        else:
            new_empty.remove((x, y))
            new_occupied.add((x, y))

    for x, y in o:
        count = 0
        for dx, dy in [(-1,-1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
            if find_occupied_seat(x, y, dx, dy):
                count += 1
        if count >= 5:
            new_occupied.remove((x,y))
            new_empty.add((x, y))

    return new_empty, new_occupied

prev = None
while True:
    empty, occupied = solve(empty, occupied)
    cur = len((occupied))
    if cur == prev:
        print(cur)
        print(f'time: {time.time() - start_time}')
        break
    prev = cur