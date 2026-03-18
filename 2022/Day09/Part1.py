with open("input.txt") as f:
    data = f.read().split("\n")

moves = {
    "R": (0, 1),
    "L": (0, -1),
    "U": (-1, 0),
    "D": (1, 0)
}
visited = {(0,0)}
h = (0,0)
t = (0,0)
def is_following(head, tail):
    cx, cy = head
    if tail == head:
        return True
    for dx, dy in [(0,1),(1,0),(0,-1),(-1,0),(-1,-1),(-1,1),(1,-1),(1,1)]:
        tx, ty = cx + dx, cy + dy
        if (tx, ty) == tail:
            return True
    return False
for line in data:
    direc, nums = line.split(" ")
    for i in range(int(nums)):
        hx, hy = h
        hx, hy = hx + moves[direc][0], hy + moves[direc][1]
        h = (hx, hy)
        if is_following(h, t):
            continue
        tx, ty = hx + (-1 * moves[direc][0]), hy + (-1 * moves[direc][1])
        t = (tx, ty)
        if (tx, ty) not in visited:
            visited.add((tx, ty))
print(len(visited))