with open("input.txt") as f:
    data = f.read()
p1, _ = data.split("\n\n")
workflows = {}

for line in p1.split("\n"):
    name, rest = line[:-1].split("{")
    rules = rest.split(",")
    workflows[name] = ([], rules.pop())
    for rule in rules:
        comparison, target = rule.split(":")
        key = comparison[0]
        comp = comparison[1]
        num = int(comparison[2:])
        workflows[name][0].append((key, comp, num, target))


def dfs(ranges, name = "in"):
    total = 0
    if name == "A":
        product = 1
        for l, h in ranges.values():
            product *= h - l + 1
        return product
    if name == "R":
        return 0

    rules, fallback = workflows[name]

    for key, comp, num, target in rules:
        l ,h = ranges[key]
        if comp == "<":
            T = (l, num-1)
            F = (num, h)
        else:
            T = (num+1, h)
            F = (l, num)
        if T[0] <= T[1]:
            copy = dict(ranges)
            copy[key] = T
            total += dfs(copy, target)
        if F[0] <= F[1]:
            ranges = dict(ranges)
            ranges[key] = F
        else:
            break
    else:
        total += dfs(ranges, fallback)

    return total

print(dfs({key: (1,4000) for key in "xmas"}))








