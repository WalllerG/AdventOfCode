with open('input.txt')as f:
    data = f.read().splitlines()

directions = {'E':(0, 1), 'S':(-1, 0), 'W':(0, -1), 'N':(1, 0), }
S = (0, 0)
way_point = (1, 10)

def rotate(num, d, wx, wy):
    times = num // 90
    for _ in range(times):
        if d == 'L':
            wx, wy = wy, -1 * wx
        elif d == 'R':
            wx, wy = -1 * wy, wx

    return (wx, wy)

for line in data:
    op, moves = line[0], int(line[1:])
    x, y = S
    wx, wy = way_point
    if op in directions:
        dx, dy = directions[op]
        nx, ny = wx + dx * moves, wy + dy * moves
        way_point = (nx, ny)
    else:
        if op in 'RL':
            way_point = rotate(moves, op, wx, wy)
        else:
            nx, ny = x + wx * moves, y + wy * moves
            S = (nx, ny)
            
    print(S ,way_point)

print(sum(abs(i) for i in S))