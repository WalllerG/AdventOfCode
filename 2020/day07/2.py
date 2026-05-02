from collections import defaultdict
with open('input.txt')as f:
    data = f.read().splitlines()

ans = 0
shiny = {}
graph = defaultdict(list)

for line in data:
    name, targets = line.split(' contain ')
    name = " ".join(name.split(' ')[0:2])
    targets = targets.split(', ')
    for bag in targets:
        if bag.split(' ')[0].isdigit():
            id = " ".join(bag.split(' ')[1:3])
            num = int(bag.split(' ')[0])
            if id == 'shiny gold':
                shiny[name] = True
            graph[name].append((num, id))

def dfs(cur):
    total = 0
    if cur not in graph:
        return 0
    for num, neighbour in graph[cur]:
        total += num * dfs(neighbour) + num
    return total

print(dfs('shiny gold'))