import re
with open("input.txt") as f:
    data = f.read().splitlines()
final_cuboids = {}
for line in data:
    state, coors = line.split(" ")
    nums = list(map(int, re.findall(r"-?\d+", coors)))
    new_c = ((nums[0], nums[1]), (nums[2], nums[3]), (nums[4], nums[5]))
    updates = {}
    for (ex_c), count in final_cuboids.items():
        ix = (max(new_c[0][0], ex_c[0][0]), min(new_c[0][1], ex_c[0][1]))
        iy = (max(new_c[1][0], ex_c[1][0]), min(new_c[1][1], ex_c[1][1]))
        iz = (max(new_c[2][0], ex_c[2][0]), min(new_c[2][1], ex_c[2][1]))
        if ix[0] <= ix[1] and iy[0] <= iy[1] and iz[0] <= iz[1]:
            updates[(ix, iy, iz)] = updates.get((ix, iy, iz), 0) - count
    if state == "on":
        updates[new_c] = updates.get(new_c, 0) + 1
    for c, count in updates.items():
        final_cuboids[c] = final_cuboids.get(c, 0) + count
total_on = 0
for (x, y, z), count in final_cuboids.items():
    volume = (x[1] - x[0] + 1) * (y[1] - y[0] + 1) * (z[1] - z[0] + 1)
    total_on += volume * count
print(total_on)