with open("input.txt") as f:
    data = f.read().strip().split("\n\n")
    image_string, grid_raw = data
algo = list(image_string.strip())
points = set()
lines = grid_raw.splitlines()
for r, line in enumerate(lines):
    for c, char in enumerate(line):
        if char == "#":
            points.add((r, c))
background = "0"
for step in range(50):
    new_points = set()
    rows = [p[0] for p in points]
    cols = [p[1] for p in points]
    min_r, max_r = min(rows), max(rows)
    min_c, max_c = min(cols), max(cols)
    for r in range(min_r - 1, max_r + 2):
        for c in range(min_c - 1, max_c + 2):
            binary_str = ""
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    nr, nc = r + dr, c + dc
                    if min_r <= nr <= max_r and min_c <= nc <= max_c:
                        binary_str += "1" if (nr, nc) in points else "0"
                    else:
                        binary_str += background
            index = int(binary_str, 2)
            if algo[index] == "#":
                new_points.add((r, c))
    points = new_points
    if background == "0":
        background = "1" if algo[0] == "#" else "0"
    else:
        background = "1" if algo[511] == "#" else "0"
print(len(points))

