from Util.util import read_input

data = read_input(18, False)

grid = []
for i in range(7):
    row = []
    for j in range(7):
        row.append(".")
    grid.append(row)
count = 0

for coor in data:
    if count == 12:
        break
    cd = coor.split(",")
    x = int (cd[0])
    y = int (cd[1])
    grid[y][x] = "#"
    count += 1


for row in grid:
    print("".join(row))
