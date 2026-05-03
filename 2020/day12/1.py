with open('input.txt')as f:
    data = f.read().splitlines()

directions = {'E':(0, 1), 'S':(-1, 0), 'W':(0, -1), 'N':(1, 0), }
cur = 0
dirs = list(directions.values())
S = (0, 0)

for line in data:
    op, moves = line[0], int(line[1:])
    x, y = S
    if op in directions:
        dx, dy = directions[op]
        nx, ny = x + dx * moves, y + dy * moves
        S = (nx, ny)
    else:
        if op == 'R':
            cur = (cur + moves // 90) % 4
        elif op == 'L':
            cur = (cur - moves // 90) % 4
        elif op == 'F':
            dx, dy = dirs[cur]
            nx, ny = x + dx * moves, y + dy * moves
            S = (nx, ny)

print(sum(abs(i) for i in S))