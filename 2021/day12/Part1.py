from collections import defaultdict
with open("input.txt") as f:
    data = f.read().split("\n")
graph = defaultdict(list)
for line in data:
    s, e = line.split("-")
    graph[s].append(e)
    graph[e].append(s)
def dfs(start, visited=None):
    if visited is None:
        visited = {start}
    total = 0
    if start == "end":
        return 1
    for neighbor in graph[start]:
        if neighbor not in visited and neighbor.islower():
            visited.add(neighbor)
            total += dfs(neighbor, visited)
            visited.remove(neighbor)
        elif neighbor.isupper():
            total += dfs(neighbor, visited)
    return total
print((dfs("start")))