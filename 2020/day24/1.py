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
        continue
    black.remove((x, y))

print(len(black))