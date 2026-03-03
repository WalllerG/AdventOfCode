from Util.util import read_input

data = read_input(12, True)

price = 0
grid= []

for i in range(len(data)):
    lst = list(data[i])
    grid.append(lst)

def findAllValidNeighbors(p):
    neighbors = []
    plant_type = grid[p[0]][p[1]]
    up = (p[0] - 1, p[1])
    down = (p[0] + 1, p[1])
    left = (p[0], p[1] - 1)
    right = (p[0], p[1] + 1)
    if -1 < up[0] < len(grid) and -1 < up[1] < len(grid[0]) and grid[up[0]][up[1]] == plant_type:
        neighbors.append(up)
    if -1 < down[0] < len(grid) and -1 < down[1] < len(grid[0]) and grid[down[0]][down[1]] == plant_type:
        neighbors.append(down)
    if -1 < left[0] < len(grid) and -1 < left[1] < len(grid[0]) and grid[left[0]][left[1]] == plant_type:
        neighbors.append(left)
    if -1 < right[0] < len(grid) and -1 < right[1] < len(grid[0]) and grid[right[0]][right[1]] == plant_type:
        neighbors.append(right)

    return neighbors

def dfs(start):
    queue = [start]
    region = set()
    while queue:
        current = queue.pop()
        if len(findAllValidNeighbors(current)) == 0:
            region.add(current)
        else:
            for neighbor in findAllValidNeighbors(current):
                if neighbor not in region:
                    region.add(neighbor)
                    queue.append(neighbor)

    return region

def perimeters(s):
    result = 0
    for plant in s:
        peri = 4
        for neighbor in findAllValidNeighbors(plant):
             peri -= 1
        result += peri
    return result

candidates = {(i,j) for i in range(len(grid)) for j in range(len(grid[i]))}

while candidates:
    region = dfs(candidates.pop())
    candidates -= region
    price += len(region) * perimeters(region)

print(price)


