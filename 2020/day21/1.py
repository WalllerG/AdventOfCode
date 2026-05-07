from collections import defaultdict, deque
with open('input.txt')as f:
    data = f.read().splitlines()

graph = {}
possible = set()
arrangement = defaultdict(list)
result = {}
seen = set()

for line in data:
    ingredients, allergens = line.split(' (contains ')
    ingredients = ingredients.split(' ')
    allergens = allergens[:-1].split(', ')
    for allergen in allergens:
        if allergen not in graph:
            graph[allergen] = defaultdict(int)
        for ingredient in ingredients:
            graph[allergen][ingredient] += 1

for id, val in graph.items():
    count = max(val.values())
    for a in val:
        if val[a] >= count:
            possible.add(a)
            arrangement[id].append(a)

queue = deque([(a, val) for a, val in arrangement.items()])

while queue:
    ingredient, lst = queue.popleft()
    if len(lst) == 1:
        seen.add(lst[0])
        result[ingredient] = lst[0]
    else:
        for saw in seen:
            if saw in lst:
                lst.remove(saw)
        queue.append((ingredient, lst))

re = sorted(result)
print(",".join([result[a] for a in re]))

