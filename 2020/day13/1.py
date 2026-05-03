import re
with open('input.txt')as f:
    data = f.read().splitlines()

start_time = int(data[0])
buses = list(map(int, re.findall(r'\d+', data[1])))
best = (10 ** 9, None)

for bus in buses:
    wait = (start_time // bus + 1) * bus - start_time
    if wait < best[0]:
        best = (wait, bus)

print(best[0] * best[1])