with open('input.txt')as f:
    grid = f.read().splitlines()

x = 0
y = 0
ans = 0
wrap = len(grid[0])

while y < len(grid)-1:
    x = (x + 3) % wrap
    y += 1
    if grid[y][x] == '#':
        ans += 1

print(ans)