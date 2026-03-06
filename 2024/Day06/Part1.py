from Util.util import read_input

data = read_input(6,False)

grid = []
for lines in data:
    grid.append(list(lines))
index = []
count = -1

up = False
down = False
left = False
right = False

for row in grid:
    count = count + 1
    if "^" in row or ">" in row or "<" in row or "v" in row:
        for i in range(len(row)):
            if row[i] == "^":
                index.append(count)
                index.append(i)
                up = True
                left = False
                down = False
                right = False
            elif row[i] == ">":
                index.append(count)
                index.append(i)
                right = True
                up = False
                left = False
                down = False
            elif row[i] == "<":
                index.append(count)
                index.append(i)
                left = True
                down = False
                right = False
                up = False
            elif row[i] == "v":
                index.append(count)
                index.append(i)
                down = True
                up = False
                left = False
                right = False

isOut = False
isNotOut = False
while not isOut:
    if up:
        for j in range(index[0], -1, -1):
            if grid[j][index[1]] == "#":
                right = True
                left = False
                down = False
                up = False
                isNotOut = True
                break
            if grid[j][index[1]] != "X":
                grid[j][index[1]] = "X"
        index[0] = j + 1
        if isNotOut:
            isNotOut = False
        else:
            isOut = True

    if right:
        for k in range(index[1], len(grid[0])):
            if grid[index[0]][k] == "#":
                right = False
                left = False
                down = True
                up = False
                isNotOut = True
                break
            if grid[index[0]][k] != "X":
                grid[index[0]][k] = "X"
        index[1] = k - 1
        if isNotOut:
            isNotOut = False
        else:
            isOut = True

    if down:
        for l in range(index[0], len(grid)):
            if grid[l][index[1]] == "#":
                down = False
                left = True
                up = False
                right = False
                isNotOut = True
                break
            if grid[l][index[1]] != "X":
                grid[l][index[1]] = "X"
        index[0] = l - 1
        if isNotOut:
            isNotOut = False
        else:
            isOut = True

    if left:
        for m in range(index[1], -1, -1):
            if grid[index[0]][m] == "#":
                right = False
                left = False
                down = False
                up = True
                isNotOut = True
                break
            if grid[index[0]][m] != "X":
                grid[index[0]][m] = "X"
        index[1] = m + 1
        if isNotOut:
            isNotOut = False
        else:
            isOut = True

result = 0
for row in grid:
    print(row)
    for col in row:
        if col == "X":
            result += 1

print(result)
