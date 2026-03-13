import re
from collections import defaultdict
with open("input.txt") as f:
    data = f.read()
ans = 0
p1, p2 = data.split("\n\n")
condition_map = defaultdict(list)
graph = defaultdict(list)
num_map = defaultdict(int)
def check(s, b):
    char = b.split("=")[0]
    n = int (b.split("=")[-1])
    if ">" not in s and "<" not in s:
        return False

    if "<" in s:
        s = s.split("<")
        if char != s[0]:
            return False
        else:
            return n < int(s[-1])

    else:
        s = s.split(">")
        if char != s[0]:
            return False
        else:
            return n > int(s[-1])


for workflow in p1.split("\n"):
    workflow = workflow.strip("}")
    a, conditions = workflow.split("{")
    for condition in conditions.split(","):
        graph[a].append(condition.split(":")[-1])
        condition_map[a].append(condition.split(":")[0])

for nums in p2.split("\n"):
    nums = nums[1:-1]
    cur = "in"
    while True:
        has_next = False
        for i in range(len(condition_map[cur])):
            for num in nums.split(","):
                if check(condition_map[cur][i], num):
                    cur = graph[cur][i]
                    has_next = True
                    break
            if has_next:
                break
        if not has_next:
            cur = graph[cur][-1]
        if cur == "R":
            break
        if cur == "A":
            ans += sum(map(int,re.findall(r'\d+',nums)))
            break
print(ans)





