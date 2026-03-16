from Util.util import read_input
data = read_input(True)

coor_map = {}
bricks = []
cube = []
for i in range(len(data)):
    s, e = data[i].split("~")
    sx, sy, sz = s.split(",")
    ex, ey, ez = e.split(",")
    bricks.append((int(sx), int(sy), int(sz), int(ex), int(ey), int(ez)))

sort_bricks = sorted(bricks, key=lambda x: x[-1])
print(sort_bricks)







