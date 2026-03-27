import functools
from collections import defaultdict
with open("input.txt") as f:
    init, g = f.read().split("\n\n")
steps = 0
letters_count = defaultdict(int)
for char in init:
    letters_count[char] += 1
todo = [tuple(x for x in line.split(" -> ")) for line in g.split("\n")]
def find_pair(s):
    ps = []
    for i in range(0, len(s)-1):
        ps.append(s[i:i+2])
    return ps
@functools.lru_cache()
def dfs(step, s):
    if step == 0:
        return
    pairs = find_pair(s)
    new_s = s
    for i, pair in enumerate(pairs):
        for goal, insert in todo:
            if goal in pair:
                letters_count[insert] += 1
                new_s = list(new_s)
                new_s.insert((i * 2)+1, insert)
                new_s = "".join(new_s)
    dfs(step-1, new_s)
dfs(10, init)
print(max(letters_count.values()) - min(letters_count.values()))






