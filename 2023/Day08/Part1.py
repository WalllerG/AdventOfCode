import re
with open("input.txt") as f:
    data = f.read().strip()

ans = 0
nodes = {}
p1, p2 = data.split('\n\n')
direction = [0 if char == 'L' else 1 for char in p1]

for node in p2.split('\n'):
    pattern = re.findall(r"[A-Z]{3}", node)
    nodes[pattern[0]] = (pattern[1], pattern[2])

current = "AAA"
while len(direction) > 0:
    dic = direction.pop(0)
    if current == "ZZZ":
        print(ans)
        break
    current = nodes[current][dic]
    direction.append(dic)
    ans += 1





