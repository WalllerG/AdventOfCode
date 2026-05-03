from z3 import *
with open('input.txt')as f:
    data = f.read().splitlines()

buses = data[1].split(',')
time_stamp = {}
cur = 0
solver = Optimize()
ans = Int('ans')
solver.add(ans >= 0)

for bus in buses:
    if bus.isdigit():
        solver.add((ans + cur) % bus == 0)
        cur += 1
    else:
        cur += 1

solver.minimize(ans)
solver.check()
m = solver.model()

print(m)