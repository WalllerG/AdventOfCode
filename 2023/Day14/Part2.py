from Util.util import read_input
data = read_input(True)
ans = 0

gd = [list(line) for line in data]

def roll_cycle(grid):
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            dx, dy = -1, 0
            nx, ny = x + dx, y + dy
            if grid[x][y] == 'O':
                cx, cy = x, y
                while 0 <= nx < len(grid) and 0 <= ny < len(grid[nx]):
                    if grid[nx][ny] != '#' and grid[nx][ny] != 'O':
                        grid[nx][ny] = 'O'
                        grid[cx][cy] = '.'
                        nx, ny = nx + dx, ny + dy
                        cx, cy = cx + dx, cy + dy
                    else:
                        break
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            dx, dy = 0, -1
            nx, ny = x + dx, y + dy
            if grid[x][y] == 'O':
                cx, cy = x, y
                while 0 <= nx < len(grid) and 0 <= ny < len(grid[nx]):
                    if grid[nx][ny] != '#' and grid[nx][ny] != 'O':
                        grid[nx][ny] = 'O'
                        grid[cx][cy] = '.'
                        nx, ny = nx + dx, ny + dy
                        cx, cy = cx + dx, cy + dy
                    else:
                        break
    for x in range(len(grid)-1,-1,-1):
        for y in range(len(grid[x])):
            dx, dy = 1, 0
            nx, ny = x + dx, y + dy
            if grid[x][y] == 'O':
                cx, cy = x, y
                while 0 <= nx < len(grid) and 0 <= ny < len(grid[nx]):
                    if grid[nx][ny] != '#' and grid[nx][ny] != 'O':
                        grid[nx][ny] = 'O'
                        grid[cx][cy] = '.'
                        nx, ny = nx + dx, ny + dy
                        cx, cy = cx + dx, cy + dy
                    else:
                        break
    for x in range(len(grid)):
        for y in range(len(grid[x])-1,-1,-1):
            dx, dy = 0, 1
            nx, ny = x + dx, y + dy
            if grid[x][y] == 'O':
                cx, cy = x, y
                while 0 <= nx < len(grid) and 0 <= ny < len(grid[nx]):
                    if grid[nx][ny] != '#' and grid[nx][ny] != 'O':
                        grid[nx][ny] = 'O'
                        grid[cx][cy] = '.'
                        nx, ny = nx + dx, ny + dy
                        cx, cy = cx + dx, cy + dy
                    else:
                        break
    return grid


for i in range(132):
    gd = roll_cycle(gd)
ind = len(gd)
for i in range(len(gd)):
    s = "".join(gd[i])
    rocks = s.count('O')
    ans += rocks * ind
    ind-=1
print(ans)









