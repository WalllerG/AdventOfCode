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
    neighbors.append(up)
    neighbors.append(down)
    neighbors.append(left)
    neighbors.append(right)
    return neighbors

def is_inbounds(p):
    return -1 < p[0] < len(grid) and -1 < p[1] < len(grid)

def dfs(start):
    queue = [start]
    plant_type = grid[start[0]][start[1]]
    region = set()

    is_one = True
    while queue:
        current = queue.pop()

        for neighbor in findAllNeighbors(current):
            if not is_inbounds(neighbor):
                continue
            if neighbor not in region and grid[neighbor[0]][neighbor[1]] == plant_type:
                region.add(neighbor)
                queue.append(neighbor)
                is_one = False
        if is_one:
            region.add(current)

    return region


def sides (region_set):
    corners = 0
    directions = [
        (-1, 0),  # Top
        (0, 1),  # Right
        (1, 0),  # Bottom
        (0, -1)  # Left
    ]

    for r, c in region_set:
        for i in range(4):
            d1 = directions[i]
            d2 = directions[(i + 1) % 4]

            n1 = (r + d1[0], c + d1[1])
            n2 = (r + d2[0], c + d2[1])
            diag = (r + d1[0] + d2[0], c + d1[1] + d2[1])

            if n1 not in region_set and n2 not in region_set:
                corners += 1

            if n1 in region_set and n2 in region_set and diag not in region_set:
                corners += 1

    return corners



candidates = {(i,j) for i in range(len(grid)) for j in range(len(grid[i]))}
while candidates:
    start = candidates.pop()
    region = dfs(start)
    candidates -= region
    price += sides(region) * len(region)

print(price)



