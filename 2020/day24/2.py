from copy import deepcopy
with open('input.txt')as f:
    data = f.read().splitlines()

start = (0, 0)
neighbours = {
    'e':  (0, 1),
    'w':  (0, -1),
    'se': (1, 0),
    'sw': (1, -1),
    'nw': (-1, 0),
    'ne': (-1, 1)
}
black = set()
white = set()

for line in data:
        index = 0
        x, y = start
        while index < len(line):
            if line[index].startswith('s') or line[index].startswith('n'):
                cur = line[index:index+2]
                dx, dy = neighbours[cur]
                x, y = x + dx, y + dy
                index += 2
            else:
                cur = line[index]
                dx, dy = neighbours[cur]
                x, y = x + dx, y + dy
                index += 1

        if (x, y) not in black:
            black.add((x, y))
            if (x, y) in white:
                white.remove((x, y))
        else:
            black.remove((x, y))
            white.add((x, y))

for _ in range(100):
    new_black = set()
    tiles_to_check = set()

    for x, y in black:
        tiles_to_check.add((x, y))
        for dx, dy in neighbours.values():
            tiles_to_check.add((x + dx, y + dy))
    
    for x, y in tiles_to_check:
        count = 0
        for dx, dy in neighbours.values():
            if (x + dx, y + dy) in black:
                count += 1
        
        if (x, y) in black:
            if count == 1 or count == 2:
                new_black.add((x, y))
        else:
            if count == 2:
                new_black.add((x, y))
    
    black = new_black
    
print(len(black))