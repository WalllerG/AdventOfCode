with open("input.txt") as f:
    data = f.read().split("\n")
grid = [list(line) for line in data]
low_points = []
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
            low_points.append((i, j))
def find_basins(lp):
    q = [lp]
    total = 1
    seen = {lp}
    while q:
        x, y = q.pop(0)
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                if int(grid[nx][ny]) < 9 and (nx, ny) not in seen:
                    q.append((nx, ny))
                    seen.add((nx, ny))
                    total += 1
    return total
basin_sizes = [find_basins(lp) for lp in low_points]
basin_sizes.sort(reverse=True)
print(basin_sizes[0] * basin_sizes[1] * basin_sizes[2])