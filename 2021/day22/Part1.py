import re
import itertools
with open("input.txt") as f:
    data = f.read().split("\n")
cubes = set()
def is_in_range(x, y, z):
    if x[0] >= -50 and x[1] <= 50 and y[0] >= -50 and y[1] <= 50 and z[0] >= -50 and z[1] <= 50:
        return True
    return False
for line in data:
    state, coors = line.split(" ")
    x_range = int(re.findall(r"-?\d+", coors)[0]), int(re.findall(r"-?\d+", coors)[1])
    y_range = int(re.findall(r"-?\d+", coors)[2]), int(re.findall(r"-?\d+", coors)[3])
    z_range = int(re.findall(r"-?\d+", coors)[4]), int(re.findall(r"-?\d+", coors)[5])
    if is_in_range(x_range, y_range, z_range):
        x_range, y_range, z_range = range(x_range[0], x_range[1]+1), range(y_range[0], y_range[1]+1), range(z_range[0],z_range[1]+1)
        if state == "on":
            combos = set(itertools.product(x_range, y_range, z_range))
            cubes.update(combos)
        else:
            combos = set(itertools.product(x_range, y_range, z_range))
            cubes.difference_update(combos)
print(len(cubes))