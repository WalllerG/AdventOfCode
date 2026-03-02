from Util.util import read_input

data = read_input(10, True)
result = 0
trailheads = []

grid = []
for line in data:
    lst = list(line)
    grid.append(lst)

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == "0":
            trailheads.append([i, j])

def backtrack (current,trail_tails):
    num = int(grid[current[0]][current[1]])
    if grid[current[0]][current[1]] == "9":
        trail_tails.append(9)

    up = current[0]-1
    down = current[0]+1
    left = current[1]-1
    right = current[1]+1

    if -1 < up < len(grid) and int (grid[up][current[1]]) - num == 1:
        backtrack([up,current[1]],trail_tails)
    if -1 < down < len(grid) and int (grid[down][current[1]]) - num == 1:
        backtrack([down,current[1]],trail_tails)
    if -1 < left < len(grid) and int (grid[current[0]][left]) - num == 1:
        backtrack([current[0],left],trail_tails)
    if -1 < right < len(grid) and int (grid[current[0]][right]) - num == 1:
        backtrack([current[0],right],trail_tails)

for head in trailheads:
    lst = []
    backtrack(head,lst)
    result += len(lst)

print(result)
