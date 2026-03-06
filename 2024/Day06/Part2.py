from Util.util import read_input

data = read_input(6,True)

grid = []
for lines in data:
    grid.append(list(lines))
index = []
count = -1

direction = set()

for row in grid:
    count = count + 1
    if "^" in row or ">" in row or "<" in row or "v" in row:
        for i in range(len(row)):
            if row[i] == "^":
                index.append(count)
                index.append(i)
                direction = (-1,0)
            elif row[i] == ">":
                index.append(count)
                index.append(i)
                direction = (0, 1)
            elif row[i] == "<":
                index.append(count)
                index.append(i)
                direction = (0, -1)
            elif row[i] == "v":
                index.append(count)
                index.append(i)
                direction = (1, 0)

storeDirection = (-1, 0)
pos = (index[0],index[1])


result = 0

visited_states = set()
is_loop = False


for k in range(len(grid)):
    for j in range(len(grid[0])):

        if grid[k][j] == "^" or grid[k][j] == "#":
            continue
        else:
            grid[k][j] = "O"

        while True:
            current_state = (pos, direction)

            if current_state in visited_states:
                result += 1
                grid[k][j] = "."
                direction = storeDirection
                pos = (index[0],index[1])
                visited_states.clear()
                break

            visited_states.add(current_state)

            next_r = pos[0] + direction[0]
            next_c = pos[1] + direction[1]
            if next_r > len(grid)-1 or next_r < 0 or next_c > len(grid[0])-1 or next_c < 0:
                visited_states.clear()
                pos = (index[0],index[1])
                direction = storeDirection
                grid[k][j] = "."
                break
            elif grid[next_r][next_c] != "#" and grid[next_r][next_c] != "O":
                pos = (next_r, next_c)
            else :
                if direction == (-1, 0):
                    direction = (0, 1)
                    pos = (next_r+1, next_c)

                elif direction == (0, 1):
                    direction = (1, 0)
                    pos = (next_r, next_c-1)

                elif direction == (1, 0):
                    direction = (0, -1)
                    pos = (next_r-1, next_c)

                elif direction == (0, -1):
                    direction = (-1, 0)
                    pos = (next_r, next_c+1)

print(result)