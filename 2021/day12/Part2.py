from collections import defaultdict
with open("input.txt") as f:
    data = f.read().split("\n")
graph = defaultdict(list)
for line in data:
    s, e = line.split("-")
    graph[s].append(e)
    graph[e].append(s)

def dfs(start, visited, doubled):
    total = 0
    if start == "end":
        return 1
    for neighbor in graph[start]:
        if neighbor == "start":
            continue
        if neighbor.islower():
            if neighbor not in visited:
                new_visited = visited | {neighbor}
                total += dfs(neighbor, new_visited, doubled)
            elif not doubled:
                total += dfs(neighbor, visited, True)
        elif neighbor.isupper():
            total += dfs(neighbor, visited, doubled)
    return total
print((dfs("start", {"start"}, False)))