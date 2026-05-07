from collections import defaultdict
import numpy as np
with open('input.txt')as f:
    tiles = f.read().split('\n\n')

matches = defaultdict(set)
edges = {}
ans = 1

for tile in tiles:
    id = int(tile.splitlines()[0].split(' ')[1][:-1])
    grid = np.array([list(line) for line in tile.splitlines()[1:]])
    x_edges = set()
    y_edges = set()

    for i in [0, len(grid)-1]:
        group = []
        for j in range(len(grid[0])):
            if grid[i][j] == '#':
                group.append(j)
        y_edges.add(tuple(group))

    for i in [0, len(grid)-1]:
        group = []
        for actual, j in enumerate(range(len(grid[0])-1, -1, -1)):
            if grid[i][j] == '#':
                group.append(actual)
        y_edges.add(tuple(group))

    for j in [0, len(grid[0])-1]:
        group = []
        for i in range(len(grid)):
            if grid[i][j] == '#':
                group.append(i)
        x_edges.add(tuple(group))

    for j in [0, len(grid[0])-1]:
        group = []
        for actual, i in enumerate(range(len(grid)-1, -1, -1)):
            if grid[i][j] == '#':
                group.append(actual)
        x_edges.add(tuple(group))

    grid = np.rot90(grid)

    for i in [0, len(grid)-1]:
        group = []
        for j in range(len(grid[0])):
            if grid[i][j] == '#':
                group.append(j)
        y_edges.add(tuple(group))

    for i in [0, len(grid)-1]:
        group = []
        for actual, j in enumerate(range(len(grid[0])-1, -1, -1)):
            if grid[i][j] == '#':
                group.append(actual)
        y_edges.add(tuple(group))

    for j in [0, len(grid[0])-1]:
        group = []
        for i in range(len(grid)):
            if grid[i][j] == '#':
                group.append(i)
        x_edges.add(tuple(group))

    for j in [0, len(grid[0])-1]:
        group = []
        for actual, i in enumerate(range(len(grid)-1, -1, -1)):
            if grid[i][j] == '#':
                group.append(actual)
        x_edges.add(tuple(group))

    edges[id] = [x_edges, y_edges]

for id, xy in edges.items():
    for id2, xy2 in edges.items():
        if id != id2:
            for x in xy[0]:
                if x in xy2[0]:
                    matches[id].add(id2)
                    matches[id2].add(id)
            for y in xy[1]:
                if y in xy2[1]:
                    matches[id].add(id2)
                    matches[id2].add(id)

for id in matches:
    if len(matches[id]) == 2:
        ans *= id

print(ans)