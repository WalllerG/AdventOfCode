from copy import deepcopy
with open('input.txt')as f:
    grid = f.read().splitlines()

R = len(grid)
C = len(grid[0])

empty = set((r, c) for r in range(R) for c in range(C) if grid[r][c] == 'L')
occupied = set()

def solve(e, o):
    new_empty = deepcopy(e)
    new_occupied = deepcopy(o)
    for x, y in e:
        for dx, dy in [(-1,-1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < R and 0 <= ny < C and (nx, ny) in o:
                break
        else:
            new_empty.remove((x, y))
            new_occupied.add((x, y))

    for  x, y in o:
        count = 0
        for dx, dy in [(-1,-1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < R and 0 <= ny < C and (nx, ny) in o:
                count += 1
        if count >= 4:
            new_occupied.remove((x,y))
            new_empty.add((x, y))

    return new_empty, new_occupied

prev = None
while True:
    empty, occupied = solve(empty, occupied)
    cur = len((occupied))
    if cur == prev:
        print(cur)
        break
    prev = cur