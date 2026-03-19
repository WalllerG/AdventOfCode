with open("input.txt") as f:
    data = f.read().split("\n")
rocks = set()
ans = 0
for line in data:
    path = line.split(" -> ")
    for i in range(len(path) - 1):
        x1, y1 = path[i].split(",")
        x2, y2 = path[i + 1].split(",")
        if x1 == x2:
            if int(y1) > int(y2):
                ny = int(y1)
                for _ in range(abs(int(y1) - int(y2)) + 1):
                    rocks.add((int(x1), ny))
                    ny -= 1
            else:
                ny = int(y1)
                for _ in range(abs(int(y1) - int(y2)) + 1):
                    rocks.add((int(x1), ny))
                    ny += 1
        else:
            if int(x1) > int(x2):
                nx = int(x1)
                for _ in range(abs(int(x1) - int(x2)) + 1):
                    rocks.add((nx, int(y1)))
                    nx -= 1
            else:
                nx = int(x1)
                for _ in range(abs(int(x1) - int(x2)) + 1):
                    rocks.add((nx, int(y1)))
                    nx += 1

edge = max(rocks, key=lambda c: c[1])[1]

def falling_sand(pos):
    current = pos
    while True:
        x, y = current
        down = (x, y + 1)
        down_l = (x - 1, y + 1)
        down_r = (x + 1, y + 1)
        if y == edge + 1:
            return current
        if down not in rocks:
            current = down
        elif down_l not in rocks:
            current = down_l
        elif down_r not in rocks:
            current = down_r
        else:
            return current

while True:
    if (499,1) in rocks and (500,1) in rocks and (501,1) in rocks:
        break
    sand_pos = falling_sand((500, 0))
    rocks.add(sand_pos)
    ans += 1
print(ans+1)