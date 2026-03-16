from collections import deque
from Util.util import read_input
data = read_input(True)

bricks = [list(map(int, line.replace("~",",").split(","))) for line in data]
bricks.sort(key=lambda x: x[2])
def overlap(a, b):
    return max(a[0], b[0]) <= min(a[3], b[3]) and max(a[1], b[1]) <= min(a[4], b[4])

for i, brick in enumerate(bricks):
    max_z = 1
    for check in bricks[:i]:
        if overlap(brick,check):
            max_z = max(max_z, check[5] + 1)
    height = brick[5] - brick[2]
    brick[2] = max_z
    brick[5] = max_z + height

bricks.sort(key=lambda x: x[2])
k_support_v = {i: set() for i in range(len(bricks))}
v_support_k = {i: set() for i in range(len(bricks))}

for j, higher in enumerate(bricks):
    for i, lower in enumerate(bricks[:j]):
        if overlap(lower, higher) and higher[2] == lower[5] + 1:
            k_support_v[i].add(j)
            v_support_k[j].add(i)

ans = 0
for i in range(len(bricks)):
    q = deque(j for j in k_support_v[i] if len(v_support_k[j]) == 1)
    falling = set(q)
    falling.add(i)
    while q:
        j = q.popleft()
        for k in k_support_v[j] - falling:
            if v_support_k[k] <= falling:
                q.append(k)
                falling.add(k)
    ans += len(falling) - 1
print(ans)


















