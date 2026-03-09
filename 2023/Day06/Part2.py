import re
from Util.util import read_input
data = read_input(True)
ans = 0

time = [int(x) for x in re.findall(r'\d+', data[0])]
distance = [int(x) for x in re.findall(r'\d+', data[1])]

t = ""
d = ""
for t1 in time:
    t += str(t1)
for t2 in distance:
    d += str(t2)
t = int (t)
d = int (d)

for i in range(t):
    speed = t - i
    dis = speed * i
    if dis > d:
        ans += 1
print(ans)