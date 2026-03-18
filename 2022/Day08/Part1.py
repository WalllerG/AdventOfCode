with open("input.txt") as f:
    grid = [[int(x) for x in line] for line in f.read().splitlines()]
rows, cols = len(grid), len(grid[0])
visible_count = 0
for r in range(rows):
    for c in range(cols):
        current_height = grid[r][c]
        if r == 0 or r == rows - 1 or c == 0 or c == cols - 1:
            visible_count += 1
            continue
        is_visible = False
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc
            blocked = False
            while 0 <= nr < rows and 0 <= nc < cols:
                if grid[nr][nc] >= current_height:
                    blocked = True
                    break
                nr += dr
                nc += dc
            if not blocked:
                is_visible = True
                break
        if is_visible:
            visible_count += 1
print(visible_count)