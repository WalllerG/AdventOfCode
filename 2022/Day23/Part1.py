from collections import defaultdict
with open("input.txt") as f:
    data = f.read().split("\n")
elves = set()
directions = {
    0: [(-1, 0), (-1, 1), (-1, -1)],
    1: [(1, 0), (1, 1), (1, -1)],
    2: [(0, -1), (-1, -1), (1, -1)],
    3: [(0, 1), (1, 1), (-1, 1)]
}
for i, line in enumerate(data):
    for j, char in enumerate(line):
        if char == "#":
            elves.add((i, j))
cur_dir_index = 0
for _ in range(10):
    pos2move = defaultdict(list)
    while True:
        for x, y in elves:
            has_elve = False
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]:
                nx, ny = x + dx, y + dy
                if (nx, ny) in elves:
                    has_elve = True
                    break
            if has_elve:
                # N
                can_move = True
                for dx, dy in directions[cur_dir_index]:
                    nx, ny = x + dx, y + dy
                    if (nx, ny) in elves:
                        can_move = False
                        break
                if can_move:
                    to_move = x + directions[cur_dir_index][0][0], y + directions[cur_dir_index][0][1]
                    pos2move[to_move].append((x, y))
                    continue
                # S
                can_move = True
                for dx, dy in directions[(cur_dir_index + 1) % 4]:
                    nx, ny = x + dx, y + dy
                    if (nx, ny) in elves:
                        can_move = False
                        break
                if can_move:
                    to_move = x + directions[(cur_dir_index + 1) % 4][0][0], y + directions[(cur_dir_index + 1) % 4][0][1]
                    pos2move[to_move].append((x, y))
                    continue
                # W
                can_move = True
                for dx, dy in directions[(cur_dir_index + 2) % 4]:
                    nx, ny = x + dx, y + dy
                    if (nx, ny) in elves:
                        can_move = False
                        break
                if can_move:
                    to_move = x + directions[(cur_dir_index + 2) % 4][0][0], y + directions[(cur_dir_index + 2) % 4][0][1]
                    pos2move[to_move].append((x, y))
                    continue
                # E
                can_move = True
                for dx, dy in directions[(cur_dir_index + 3) % 4]:
                    nx, ny = x + dx, y + dy
                    if (nx, ny) in elves:
                        can_move = False
                        break
                if can_move:
                    to_move = x + directions[(cur_dir_index + 3) % 4][0][0], y + directions[(cur_dir_index + 3) % 4][0][1]
                    pos2move[to_move].append((x, y))
                    continue
        for p2m in pos2move:
            if len(pos2move[p2m]) > 1:
                continue
            elves.remove(pos2move[p2m][0])
            elves.add(p2m)
        break
    cur_dir_index = (cur_dir_index + 1) % 4
ans = 0
a = min(elves, key=lambda k: k[0])[0]
b = max(elves, key=lambda k: k[0])[0]
c = min(elves, key=lambda k: k[1])[1]
d = max(elves, key=lambda k: k[1])[1]
for i in range(a, b+1):
    for j in range(c, d+1):
        if (i, j) not in elves:
            ans += 1
print(ans)


