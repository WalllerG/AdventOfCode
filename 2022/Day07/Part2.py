from collections import defaultdict
with open("input.txt") as f:
    data = f.read().split('\n')
directories = defaultdict(int)
i = 0
ans = 0
path = []
for l in data:
    line = l.split(" ")
    if len(line) == 3:
        if line[1] == "cd" and line[2] != "..":
            path.append(line[2])
        else:
            path.pop()
    else:
        if line[0].isdigit():
            for i in range(1, len(path) + 1):
                full_path = "/".join(path[:i])
                directories[full_path] += int(line[0])
    i += 1
used = directories["/"]
print(ans)
saves = []
for directory, size in directories.items():
    if used - size <= 40000000:
        saves.append(size)
print(min(saves))