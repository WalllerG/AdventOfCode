import ast
import sys
sys.setrecursionlimit(10000000)
with open("input.txt") as f:
    data = f.read().split("\n\n")
indices = 0
ans = 0
def compare(left, right):
    if isinstance(left, int) and isinstance(right, int):
        if left < right: return -1
        if left > right: return 1
        return 0
    if isinstance(left, list) and isinstance(right, list):
        for l, r in zip(left, right):
            res = compare(l, r)
            if res != 0: return res
        if len(left) < len(right): return -1
        if len(left) > len(right): return 1
        return 0
    if isinstance(left, int):
        return compare([left], right)
    else:
        return compare(left, [right])
for i, pairs in enumerate(data, 1):
    up, down = pairs.split("\n")
    a = ast.literal_eval(up)
    b = ast.literal_eval(down)

    if compare(a, b) == -1:
        ans += i
print(ans)