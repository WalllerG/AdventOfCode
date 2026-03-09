import re
from Util.util import read_input

data = read_input(True)
ans = 1
times = {}

time = [int(x) for x in re.findall(r'\d+', data[0])]
distance = [int(x) for x in re.findall(r'\d+', data[1])]

for t, d in zip(time, distance):
    times[t] = d

for k, v in times.items():
    way = 0
    for i in range (0, k):
        speed = k - i
        dis = i * speed
        if dis > v:
            way += 1
    ans *= way

print(ans)
