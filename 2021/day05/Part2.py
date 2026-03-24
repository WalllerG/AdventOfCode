from collections import defaultdict
with open('input.txt') as f:
    data = f.read().split("\n")
points = defaultdict(int)
ans = 0
for line in data:
    p1, p2 = line.split(" -> ")
    p1 = list(map(int, p1.split(",")))
    p2 = list(map(int, p2.split(",")))
    if p1[0] == p2[0]:
        if p1[1] < p2[1]:
            for i in range(p1[1], p2[1] + 1):
                points[(p1[0], i)] += 1
        else:
            for i in range(p1[1], p2[1] - 1, -1):
                points[(p2[0], i)] += 1
    elif p1[1] == p2[1]:
        if p1[0] < p2[0]:
            for i in range(p1[0], p2[0] + 1):
                points[(i, p1[1])] += 1
        else:
            for i in range(p1[0], p2[0] - 1, -1):
                points[(i, p1[1])] += 1
    else:
        if p1[0] < p2[0] and p1[1] < p2[1]:
            for i in range(p1[0], p2[0] + 1):
                points[(i, p1[1] + i - p1[0])] += 1
        elif p1[0] < p2[0] and p1[1] > p2[1]:
            for i in range(p1[0], p2[0] + 1):
                points[(i, p1[1] - (i - p1[0]))] += 1
        elif p1[0] > p2[0] and p1[1] < p2[1]:
            for i in range(p2[0], p1[0] + 1):
                points[(i, p2[1] - (i - p2[0]))] += 1
        else:
            for i in range(p2[0], p1[0] + 1):
                points[(i, p2[1] + i - p2[0])] += 1
for val in points.values():
    if val > 1:
        ans += 1
print(ans)