with open("input.txt") as f:
    coors, folds = f.read().split("\n\n")
points_coor = set()
for coor in coors.split("\n"):
    points_coor.add(tuple(map(int, coor.split(","))))
def fold(direction, pos, points):
    points2add = set()
    points2remove = set()
    if direction == "y":
        for point in points:
            if point[1] < pos:
                continue
            else:
                new_point = (point[0], pos - (point[1] - pos))
                points2remove.add(point)
                points2add.add(new_point)
        return (points - points2remove) | points2add
    else:
        for point in points:
            if point[0] < pos:
                continue
            else:
                new_point = (pos - (point[0] - pos), point[1])
                points2remove.add(point)
                points2add.add(new_point)
        return (points - points2remove) | points2add

for f in folds.split("\n"):
    d, p = f.split(" ")[-1].split("=")
    points_coor = fold(d, int(p), points_coor)
    break
print(len(points_coor))