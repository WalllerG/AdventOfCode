import heapq
import re
from collections import defaultdict
with open("input.txt") as f:
    data = f.read().split("\n\n")
monkeys = defaultdict(list)
inspected_times = {key: 0 for key in [0,1,2,3,4,5,6,7]}
operations = {}
test = {}
targets = {}
count = 0
for monkey in data:
    info = monkey.split("\n")
    goal = []
    for line in info:
        if "Starting" in line:
            items = re.findall(r"\d+", line)
            for item in items:
                monkeys[count].append(int(item))
        if "Operation" in line:
            _, ops  = line.split(" = ")
            op = (ops.split(" ")[1], ops.split(" ")[2])
            operations[count] = op
        if "Test" in line:
            divide = line.split(" ")[-1]
            test[count] = int(divide)
        if "If true" in line:
            goal.append(int(line.split(" ")[-1]))
        if "If false" in line:
            goal.append(int(line.split(" ")[-1]))
    targets[count] = goal
    count += 1

def get_worry_level(operation, old):
    symbol, todo = operation
    if todo.isdigit():
        if symbol == "+":
            return (old + int(todo)) // 3
        elif symbol == "*":
            return (old * int(todo)) // 3
        return None
    else:
        if symbol == "+":
            return old * 2 // 3
        elif symbol == "*":
            return old ** 2 // 3
        return None

for i in range(20):
    for m in monkeys:
        t = test[m]
        true,false = targets[m]
        op = operations[m]
        while monkeys[m]:
            item = monkeys[m].pop(0)
            cur_worry = get_worry_level(op, item)
            if cur_worry % t == 0:
                monkeys[true].append(cur_worry)
            else:
                monkeys[false].append(cur_worry)
            inspected_times[m] += 1
most_active = heapq.nlargest(2, inspected_times.values())
print(most_active[0] * most_active[1])
