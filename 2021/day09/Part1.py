with open("input.txt") as f:
    data = f.read().split("\n")
grid = [list(line) for line in data]
ans = 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        is_lowpoint = True
        for  dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = i + dx, j + dy
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                if int(grid[nx][ny]) <= int(grid[i][j]):
                    is_lowpoint = False
                    break
        if is_lowpoint:
            ans += int(grid[i][j]) + 1
print(ans)

