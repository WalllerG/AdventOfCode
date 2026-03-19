import ast
from functools import cmp_to_key
with open("input.txt", "r") as f:
    data = [line.strip() for line in f if line.strip()]
data.append("[[2]]")
data.append("[[6]]")
lst2sort = []
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
for line in data:
    line = ast.literal_eval(line)
    lst2sort.append(line)
lst2sort.sort(key=cmp_to_key(compare))
idx1 = lst2sort.index([[2]]) + 1
idx2 = lst2sort.index([[6]]) + 1
print(idx1 * idx2)
