import re
from Util.util import read_input

class Tile:
    def __init__(self, position, velocity):
        self.position = position
        self.velocity = velocity

    def move(self):
        new_x = self.position[0] + self.velocity[0]
        new_y = self.position[1] + self.velocity[1]
        if new_x < 0:
            new_x = 101 + new_x
        elif new_x >= 101:
            new_x = new_x - 101

        if new_y < 0:
            new_y = 103 + new_y
        elif new_y >= 103:
            new_y = new_y - 103

        self.position = (new_x, new_y)

data = read_input(14,test=True)

grid = []
for i in range(103):
    row = []
    for j in range(101):
        row.append(0)
    grid.append(row)

for line in data:
    p_v = line.split()
    pos = list(map(int, re.findall(r"(-?\d+)", p_v[0])))
    vol = list(map(int, re.findall(r"(-?\d+)", p_v[1])))
    tile = Tile(pos, vol)
    for x in range(100):
        tile.move()
    grid[tile.position[1]][tile.position[0]] += 1

left_top = 0
right_top = 0
left_bottom = 0
right_bottom = 0

mid_x = 101 // 2  # 50
mid_y = 103 // 2  # 51

for y in range(103):
    for x in range(101):
        count = grid[y][x]
        if count == 0: continue

        if x == mid_x or y == mid_y:
            continue

        if x < mid_x and y < mid_y:
            left_top += count
        elif x > mid_x and y < mid_y:
            right_top += count
        elif x < mid_x and y > mid_y:
            left_bottom += count
        elif x > mid_x and y > mid_y:
            right_bottom += count

print(left_top * right_top * left_bottom * right_bottom)

