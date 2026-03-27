from collections import defaultdict
with open("input.txt") as f:
    init, g = f.read().split("\n\n")
todo = {}
for line in g.split("\n"):
    line = line.split(" -> ")
    todo[line[0]] = line[1]
letters_count = defaultdict(int)
for char in init:
    letters_count[char] += 1
def find_pair(s):
    ps = []
    for i in range(0, len(s)-1):
        ps.append(s[i:i+2])
    return ps
counts = defaultdict(int)
for p in find_pair(init):
    counts[p] += 1

def dfs(step, c):
    if step == 0:
        return
    new_counts = defaultdict(int)
    for pair in c:
        goal, insert = pair, todo[pair]
        new_counts[pair[0] + insert] += c[pair]
        new_counts[insert + pair[1]] += c[pair]
        letters_count[insert] += c[pair]
    dfs(step-1, new_counts)
dfs(40, counts)
print(max(letters_count.values()) - min(letters_count.values()))






