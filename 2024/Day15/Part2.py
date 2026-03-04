from Util.util import read_input

data = read_input(15,True)
grid = []
count = 0
start = ()
moves = []
result = 0

for i in range(len(data)):
    lst = list(data[i])
    row = []
    if len(lst) == 0:
        break
    for j in range(len(lst)):
        if lst[j] == "@":
            row.append("@")
            row.append(".")
            start = (i,j*2)
        elif lst[j] == "#":
            row.append("#")
            row.append("#")
        elif lst[j] == ".":
            row.append(".")
            row.append(".")
        elif lst[j] == "O":
            row.append("[")
            row.append("]")
    grid.append(row)
    count += 1

for i in range(count+1, len(data)):
    lst = list(data[i])
    for j in range(len(lst)):
        if lst[j] == "<":
            moves.append((0,-1))
        elif lst[j] == ">":
            moves.append((0,1))
        elif lst[j] == "v":
            moves.append((1,0))
        elif lst[j] == "^":
            moves.append((-1,0))


for move in moves:
    cx, cy = start
    dx, dy = move
    if grid[cx+dx][cy+dy] == "#":
        continue
    elif grid[cx+dx][cy+dy] == ".":
        grid[cx][cy] = "."
        grid[cx+dx][cy+dy] = "@"
        start = (cx+dx, cy+dy)
    else:
        no_move = False
        i = 0
        c2m = [start]
        while len(c2m) > i:
            x, y = c2m[i]
            nx, ny = x+dx, y+dy
            if grid[nx][ny] == "[":
                if (nx, ny) not in c2m:
                    c2m.append((nx, ny))
                    c2m.append((nx, ny+1))
            if grid[nx][ny] == "]":
                if (nx, ny) not in c2m:
                    c2m.append((nx, ny))
                    c2m.append((nx, ny-1))
            elif grid[nx][ny] == "#":
                no_move = True
                break
            i += 1
        if no_move:
            continue
        else:
            for j in range(len(c2m)-1, -1, -1):
                x, y = c2m[j]
                nx, ny = x+dx, y+dy
                grid[nx][ny] = grid[x][y]
                grid[x][y] = "."
            start = (cx + dx, cy + dy)

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == "[":
            result += 100 * i + j

print(result)









