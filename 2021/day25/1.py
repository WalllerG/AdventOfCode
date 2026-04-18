from copy import deepcopy
with open('input.txt')as f:
    grid = [list(line) for line in f.read().splitlines()]

R = len(grid)
C = len(grid[0])
step = 0

while True:
    step += 1
    G = deepcopy(grid)
    move = False
    for i in range(R):
        for j in range(C):
            if grid[i][j] == '>':
                if grid[i][(j+1) % C] == '.':
                    G[i][(j+1) % C] = '>'
                    G[i][j] = '.'
                    move = True
    grid = G
    G = deepcopy(grid)
    for i in range(R):
        for j in range(C):
            if grid[i][j] == 'v':
                if grid[(i+1)%R][j] == '.':
                    G[(i+1)%R][j] = 'v'
                    G[i][j] = '.'
                    move = True
    grid = G
    if move == False:
        print(step)
        break