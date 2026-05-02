from functools import lru_cache
with open('input.txt')as f:
    data = set(map(int, f.read().splitlines()))

device = max(data)

@lru_cache
def dfs(cur):
    total = 0
    xs = [cur+1, cur+2, cur+3]
    if cur == device:
        return 1
    for x in xs:
        if x in data:
            total += dfs(x)
    return total

print(dfs(0))