from Util.util import read_input

data = read_input(12, True)

price = 0
grid= []

for i in range(len(data)):
    lst = list(data[i])
    grid.append(lst)

def findAllNeighbors(p):
    neighbors = []
    up = (p[0] - 1, p[1])
    down = (p[0] + 1, p[1])
    left = (p[0], p[1] - 1)
    right = (p[0], p[1] + 1)
    if -1 < p[0] - 1 < len(grid) and -1 < p[1] < len(grid[0]):
        neighbors.append(up)
    if -1 < p[0] + 1 < len(grid) and -1 < p[1] < len(grid[0]):
        neighbors.append(down)
    if -1 < p[0] < len(grid) and -1 < p[1] - 1 < len(grid[0]):
        neighbors.append(left)
    if -1 < p[0] < len(grid) and -1 < p[1] + 1 < len(grid[0]):
        neighbors.append(right)

    return neighbors

def dfs(start):
    queue = [start]
    plant_type = grid[start[0]][start[1]]
    region = set()
    is_one = True
    while queue:
        current = queue.pop()
        for neighbor in findAllNeighbors(current):
            if neighbor not in region and grid[neighbor[0]][neighbor[1]] == plant_type:
                region.add(neighbor)
                queue.append(neighbor)
                is_one = False
        if is_one:
            region.add(current)

    return region

def perimeter(s):
    result = 0
    for plant in s:
        peri = 4
        for neighbor in findAllNeighbors(plant):
            if neighbor in s:
                peri -= 1
        result += peri
    return result

candidates = {(i,j) for i in range(len(grid)) for j in range(len(grid[i]))}

while candidates:
    region = dfs(candidates.pop())
    candidates -= region
    price += len(region) * perimeter(region)

print(price)


