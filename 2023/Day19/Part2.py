import functools
from collections import defaultdict
with open("test.txt") as f:
    data = f.read()
ans = 0
p1, p2 = data.split("\n\n")
condition_map = defaultdict(list)
graph = defaultdict(list)
def get_range(s):
    if "<" in s:
        return 1, int(s.split("<")[-1]) - 1
    elif ">" in s:
        return int(s.split(">")[-1]) + 1, 4000
    return 1




for workflow in p1.split("\n"):
    workflow = workflow.strip("}")
    a, conditions = workflow.split("{")
    for condition in conditions.split(","):
        graph[a].append(condition.split(":")[-1])
        condition_map[a].append(condition.split(":")[0])


@functools.lru_cache()
def recursive(cur, result, range_map):

    total = 0
    if cur == "A":
        return result
    if cur == "R":
        return 0

    for flow, cons in zip(graph[cur], condition_map[cur]):
        new_range = get_range(cons)
        total += recursive(flow, result * new_range)
    return total

print(recursive("in", 1))





