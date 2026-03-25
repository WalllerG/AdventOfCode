with open("input.txt") as f:
    data = list(map(int, f.read().split(",")))
possible = set(i for i in range(min(data),max(data)+1))
cost = float("inf")
for p in possible:
    cur = 0
    for num in data:
        if num > p:
            cur += num - p
        else:
            cur += p - num
    cost = min(cost, cur)
print(cost)




