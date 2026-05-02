from collections import defaultdict
with open('input.txt')as f:
    data = f.read().splitlines()

ans = 0
shiny = {}
graph = defaultdict(list, val=[])

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

count = 0
while count < 10:
    for key, val in graph.items():
        for _, v in val:
            if shiny.get(v, False):
                shiny[key] = True
    print(len(shiny))
    count += 1