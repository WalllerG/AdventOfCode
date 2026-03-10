from Util.util import read_input
data = read_input(True)

gr = [list(line) for line in data]
ans = 0
def go_north(grid):
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
    return grid

ind = len(gr)
gr = go_north(gr)
for i in range(len(gr)):
    s = "".join(gr[i])
    rocks = s.count('O')
    ans += rocks * ind
    ind-=1
print(ans)


