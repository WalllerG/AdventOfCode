with open("input.txt") as f:
    data = f.read().split("\n")
jobs = {}
mission = []
for line in data:
    if len(line.split(" ")) == 4:
        name, ops = line.split(": ")
        targets = ops.split(" ")
        mission.append((name, targets))
    else:
        name, num = line.split(": ")
        jobs[name] = int(num)
while mission:
    current_mission = mission.pop(0)
    t1 = current_mission[1][0]
    op = current_mission[1][1]
    t2 = current_mission[1][2]
    if t1 not in jobs or t2 not in jobs:
        mission.append(current_mission)
    else:
        if op == "+":
            jobs[current_mission[0]] = jobs[t1] + jobs[t2]
        elif op == "-":
            jobs[current_mission[0]] = jobs[t1] - jobs[t2]
        elif op == "*":
            jobs[current_mission[0]] = jobs[t1] * jobs[t2]
        elif op == "/":
            jobs[current_mission[0]] = jobs[t1] // jobs[t2]
print(jobs["root"])