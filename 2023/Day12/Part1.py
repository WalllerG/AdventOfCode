
from Util.util import read_input
data = read_input(True)
ans = 0

def check_damage(lst1, lst2):
    re = []
    cur = 0
    for op in lst1:
        if op == "#":
            cur += 1
        else:
            if cur > 0:
                re.append(cur)
            cur = 0
    if cur > 0:
        re.append(cur)

    return re == lst2

def get_unknowns(l):
    ul = []
    for i in range(len(l)):
        if l[i] == "?":
            ul.append(i)
    return ul

def backtrack(unknowns, target, cur, lst):

    if cur == len(unknowns):
        if check_damage(lst, target):
            return 1
        return 0
    re = 0
    index = unknowns[cur]

    lst[index] = "."
    re += backtrack(unknowns, target, cur + 1, lst)

    lst[index] = "#"
    re += backtrack(unknowns, target, cur + 1, lst)


    return re

for line in data:
    unknown, target = line.split(" ")
    ul = get_unknowns(list(unknown))
    unknowns = list(unknown)
    nums = [int(x) for x in target.split(",")]
    ans += backtrack(ul, nums, 0, unknowns)
print(ans)




