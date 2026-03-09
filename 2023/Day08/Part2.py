import copy
import math
import re

with open("input.txt") as f:
    data = f.read().strip()

ans = 0
nodes = {}
p1, p2 = data.split('\n\n')
direction = [0 if char == 'L' else 1 for char in p1]
d_copy = copy.deepcopy(direction)

for node in p2.split('\n'):
    pattern = re.findall(r"[A-Z]{3}", node)
    nodes[pattern[0]] = (pattern[1], pattern[2])

a_nodes = ["XSA","VVA", "TTA", "AAA", "NBA", "MHA"]
frequency = {}
is_all = True
for node in a_nodes:
    current = node
    ans = 0
    d_copy = copy.deepcopy(direction)
    while len(direction) > 0:
        dic = d_copy.pop(0)
        if current.endswith("Z"):
            frequency[node] = ans
            break
        current = nodes[current][dic]
        d_copy.append(dic)
        ans += 1

print(math.lcm(*frequency.values()))





