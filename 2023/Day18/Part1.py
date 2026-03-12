from Util.util import read_input
import matplotlib.path as ground
import re
data = read_input(True)

ans = 0
edges = [(0,0)]
cur = (0,0)
l = 0
r = 0
u = 0
d = 0
for line in data:
    pattern = re.findall(r'[A-Z]\s\d+', line)
    op, moves = pattern[0].split(" ")[0], int (pattern[0].split(" ")[1])
    cur_x, cur_y = cur
    if op == "R":
        for i in range(moves):
            edges.append((cur_x, cur_y+i+1))
        cur = (cur_x, cur_y+moves)
        r += moves
    if op == "L":
        for i in range(moves):
            edges.append((cur_x, cur_y-i-1))
        cur = (cur_x, cur_y-moves)
        l -= moves
    if op == "U":
        for i in range(moves):
            edges.append((cur_x-i-1, cur_y))
        cur = (cur_x-moves, cur_y)
        u -= moves
    if op == "D":
        for i in range(moves):
            edges.append((cur_x+i+1, cur_y))
        cur = (cur_x+moves, cur_y)
        d += moves


print("finishing digging")
print(u, d)
print(l, r)
print(len(edges))
candidates = set((i, j)for i in range(d-u+1) for j in range(r-l+1))
left_over = candidates - set(edges)
path = ground.Path(edges)
for l in left_over:
    if path.contains_point(l):
        ans += 1
print(ans + len(edges))


