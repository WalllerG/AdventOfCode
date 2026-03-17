import re
from collections import defaultdict

with open("input.txt") as f:
    data = f.read()
stack_map = defaultdict(list)
p1, p2 = data.split("\n\n")
stack_map[1] = ["V", "Q", "W", "M", "B", "N", "Z", "C"]
stack_map[2] = ["B", "C", "W", "R", "Z", "H"]
stack_map[3] = ["J", "R", "Q", "F"]
stack_map[4] = ["T", "M", "N", "F", "H", "W", "S", "Z"]
stack_map[5] = ["P", "Q", "N", "L", "W", "F", "G"]
stack_map[6] = ["W", "P", "L"]
stack_map[7] = ["J", "Q", "C", "G", "R", "D", "B", "V"]
stack_map[8] = ["W", "B", "N", "Q", "Z"]
stack_map[9] = ["J", "T", "G", "C", "F", "L", "H"]
ans = ""
for line in p2.split("\n"):
    nums = re.findall(r"\d+", line)
    to_move = int(nums[0])
    start = int(nums[1])
    dest = int(nums[2])
    lst2move = stack_map[start][0:to_move]
    stack_map[start] = stack_map[start][to_move:len(stack_map[start])]
    stack_map[dest] = lst2move + stack_map[dest]
for val in stack_map.values():
    ans += val[0]
print(ans)


