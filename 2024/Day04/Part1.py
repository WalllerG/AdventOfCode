from Util.util import read_input
import re
from collections import defaultdict
lines = read_input(4, True)
result = 0
cols = []

def get_grid (files: list) -> list[list[str]]:
    grids = []
    for i in range(0, len(lines)):
        grid = []
        for j in range(0, len(lines[0])):
            grid.append(lines[i][j])
        grids.append(grid)
    return grids


def get_all_diagonals(grid: list[list[str]]) -> tuple[list[str], list[str]]:
    rows = len(grid)
    cols = len(grid[0])

    asc_buckets = defaultdict(list)
    desc_buckets = defaultdict(list)

    for r in range(rows):
        for c in range(cols):
            char = grid[r][c]
            asc_buckets[r + c].append(char)
            desc_buckets[r - c].append(char)

    ascending = ["".join(asc_buckets[k]) for k in sorted(asc_buckets.keys())]

    descending = ["".join(desc_buckets[k]) for k in sorted(desc_buckets.keys(), reverse=True)]

    return ascending, descending

grid = get_grid(lines)
desc_lines, asc_lines = get_all_diagonals(grid)

for desc_line, asc_line in zip(desc_lines, asc_lines):
    patterns = re.findall(r"SAMX", desc_line)
    patterns2 = re.findall(r"SAMX", asc_line)
    patterns1 = re.findall(r"XMAS", desc_line)
    patterns3 = re.findall(r"XMAS", asc_line)
    result += len(patterns1) + len(patterns2) + len(patterns3) + len(patterns)

for i in range(0, len(lines[0])):
    col = []
    for j in range(0, len(lines)):
        col.append(lines[j][i])
    line = "".join(col)
    cols.append(line)

for col in cols:
    patterns = re.findall(r"SAMX", col)
    patterns1 = re.findall(r"XMAS", col)
    result += len(patterns) + len(patterns1)


for line in lines:
    patterns = re.findall(r"SAMX", line)
    patterns1 = re.findall(r"XMAS", line)
    result += len(patterns) + len(patterns1)

print(result)

