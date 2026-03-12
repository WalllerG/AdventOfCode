from Util.util import read_input
data = read_input(True)

ans = 0
b = 0
cx, cy = 0, 0
coors = [(cx, cy)]
for line in data:
    _, _, color = line.split(" ")
    color = color[2:-1]
    hexi = color[:-1]
    dx, dy = {
        "0": (0, 1),
        "1": (1, 0),
        "2": (0, -1),
        "3": (-1, 0),
    }[color[-1]]
    cx += dx * int("".join(hexi), 16)
    cy += dy * int("".join(hexi), 16)
    b += int("".join(hexi), 16)
    coors.append((cx, cy))

A = abs(sum(coors[i][0] * (coors[i-1][1] - coors[(i + 1)% len(coors)][1]) for i in range(len(coors)))) // 2
i = A - b // 2 + 1
print(i + b)



