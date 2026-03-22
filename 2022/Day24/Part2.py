from collections import deque
with open("input.txt") as f:
    data = f.read().split("\n")
blizzards = {}
grid = [list(line) for line in data]
s = (0,1)
e = (len(grid)-1,len(grid[0])-2)
W = len(grid[0]) - 2
H = len(grid) - 2
count = 0
for i in range(1, len(grid)-1):
    for j in range(1, len(grid[i])-1):
        count += 1
        if grid[i][j] == ">":
            blizzards[count] = [i, j, 0, 1]
        elif grid[i][j] == "<":
            blizzards[count] = [i, j, 0, -1]
        elif grid[i][j] == "v":
            blizzards[count] = [i, j, 1, 0]
        else:
            blizzards[count] = [i, j, -1, 0]

def is_safe(r, c, time):
    if (r, c) == s or (r, c) == e: return True
    if not (1 <= r <= H and 1 <= c <= W): return False
    if grid[r][(c - 1 - time) % W + 1] == ">": return False
    if grid[r][(c - 1 + time) % W + 1] == "<": return False
    if grid[(r - 1 - time) % H + 1][c] == "v": return False
    if grid[(r - 1 + time) % H + 1][c] == "^": return False
    return True

def solve(start, end, t):
    queue = deque([(start[0], start[1], t)])
    seen = {(start[0], start[1], t)}
    while queue:
        r, c, time = queue.popleft()
        if (r, c) == end:
            return time
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0), (0, 0)]:
            nr, nc = r + dr, c + dc
            new_time = time + 1

            if is_safe(nr, nc, new_time):
                state = (nr, nc, new_time)
                if state not in seen:
                    seen.add(state)
                    queue.append(state)
    return -1
time1 = solve(s, e, 0)
time2 = solve(e, s, time1)
time3 = solve(s, e, time2)
print(time3)