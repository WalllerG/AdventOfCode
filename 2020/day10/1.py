from collections import deque
with open('input.txt')as f:
    data = set(map(int, f.read().splitlines()))

device = max(data)+3

def dfs(cur, d1, d3, seen=set()):
    x1, x2, x3 = cur+1, cur+2, cur+3
    if cur == device - 3:
        return d1 * (d3 + 1)
    if x1 not in seen and x1 in data:
        seen.add(x1)
        return dfs(x1, d1+1, d3, seen)
    elif x2 not in seen and x2 in data:
        seen.add(x2)
        return dfs(x2, d1, d3, seen)
    elif x3 not in seen and x3 in data:
        seen.add(x3)
        return dfs(x3, d1, d3+1, seen) 

print(dfs(0, 0, 0))
