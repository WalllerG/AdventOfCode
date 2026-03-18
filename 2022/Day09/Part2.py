with open("input.txt") as f:
    data = f.read().split("\n")
moves = {
    "R": (0, 1),
    "L": (0, -1),
    "U": (-1, 0),
    "D": (1, 0)
}
snaps = {key: [(0,0)] for key in range(10)}
for line in data:
    direc, nums = line.split(" ")
    for _ in range(int(nums)):
        hx, hy = snaps[0][-1]
        dx, dy = moves[direc]
        snaps[0].append((hx + dx, hy + dy))
        for j in range(1, 10):
            leader = snaps[j - 1][-1]
            follower = snaps[j][-1]
            diff_x = leader[0] - follower[0]
            diff_y = leader[1] - follower[1]
            if abs(diff_x) > 1 or abs(diff_y) > 1:
                move_x = (diff_x > 0) - (diff_x < 0)
                move_y = (diff_y > 0) - (diff_y < 0)
                new_pos = (follower[0] + move_x, follower[1] + move_y)
                snaps[j].append(new_pos)
            else:
                snaps[j].append(follower)
print(len(set(snaps[9])))
