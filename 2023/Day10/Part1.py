from Util.util import read_input
data = read_input(True)

grid = []
s = ()
for i in range(len(data)):
    row = list(data[i])
    for j in range(len(row)):
        if row[j] == 'S':
            s = (i, j)
    grid.append(row)

def findLoop(start):
    queue = [(start, "-", "left")]
    length = 0
    while queue:
        cur = queue.pop()
        (x, y), cs, prev = cur[0], cur[1], cur[2]
        if (x, y) == s:
            return length
        if cs == '-':
            if prev == "left":
                nx, ny = x, y-1
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                    queue.append(((nx, ny),grid[nx][ny],prev))
                    length += 1
            elif prev == "right":
                nx, ny = x, y+1
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                    queue.append(((nx, ny),grid[nx][ny],prev))
                    length += 1

        if cs == '|':
            if prev == "down":
                nx, ny = x+1, y
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                    queue.append(((nx, ny),grid[nx][ny],prev))
                    length += 1
            elif prev == "up":
                nx, ny = x-1, y
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                    queue.append(((nx, ny),grid[nx][ny],prev))
                    length += 1

        if cs == 'L':
            if prev == "down":
                nx, ny = x, y+1
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                    queue.append(((nx, ny),grid[nx][ny],"right"))
                    length += 1
            elif prev == "left":
                nx, ny = x-1, y
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                    queue.append(((nx, ny),grid[nx][ny],"up"))
                    length += 1

        if cs == 'F':
            if prev == "left":
                nx, ny = x+1, y
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                    queue.append(((nx, ny),grid[nx][ny],"down"))
                    length += 1
            elif prev == "up":
                nx, ny = x, y+1
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                    queue.append(((nx, ny),grid[nx][ny],"right"))
                    length += 1

        if cs == '7':
            if prev == "right":
                nx, ny = x + 1, y
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                    queue.append(((nx, ny), grid[nx][ny], "down"))
                    length += 1
            elif prev == "up":
                nx, ny = x, y-1
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                    queue.append(((nx, ny), grid[nx][ny], "left"))
                    length += 1

        if cs == 'J':
            if prev == "down":
                nx, ny = x, y-1
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                    queue.append(((nx, ny), grid[nx][ny], "left"))
                    length += 1
            elif prev == "right":
                nx, ny = x-1, y
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                    queue.append(((nx, ny), grid[nx][ny], "up"))
                    length += 1
    return -1
print(findLoop((s[0],s[1]-1)))