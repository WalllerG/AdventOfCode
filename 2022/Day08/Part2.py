with open("input.txt") as f:
    grid = [[int(x) for x in line] for line in f.read().splitlines()]
rows, cols = len(grid), len(grid[0])
max_scenic_score = 0
for r in range(rows):
    for c in range(cols):
        current_height = grid[r][c]
        total_score = 1
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            view_distance = 0
            nr, nc = r + dr, c + dc
            while 0 <= nr < rows and 0 <= nc < cols:
                view_distance += 1
                if grid[nr][nc] >= current_height:
                    break
                nr += dr
                nc += dc
            total_score *= view_distance
        max_scenic_score = max(max_scenic_score, total_score)
print(max_scenic_score)