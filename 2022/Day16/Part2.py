from functools import cache
import re
from collections import deque
with open("input.txt") as f:
    data = f.read().split("\n")
tunnels = {}
tunnels_state = {}
flow_rates = {}
mins = 30
for line in data:
    flow_rate, leads2 = line.split("; ")
    name = flow_rate.split(" ")[1]
    fr = re.findall(r"\d+", flow_rate)[0]
    targets = re.findall(r'[A-Z]{2,}', leads2)
    tunnels[name] = targets
    tunnels_state[name] = False
    if int(fr) != 0:
        flow_rates[name] = int(fr)

def find_shortest(s, e):
    queue = deque([(s, 0)])
    seen = set()
    seen.add(s)
    while queue:
        cur, step = queue.popleft()
        if cur == e:
            return step
        for target in tunnels[cur]:
            if target not in seen:
                queue.append((target, step+1))
                seen.add(target)
    return -1

important_valves = list(flow_rates.keys()) + ["AA"]
distances = {}
for s in important_valves:
    for e in important_valves:
        if s != e:
            distances[(s, e)] = find_shortest(s, e)

valve_to_idx = {name: i for i, name in enumerate(flow_rates.keys())}

@cache
def dfs(cur, time_left, mask):
    max_p = 0
    for next_valve, flow in flow_rates.items():
        valve_bit = 1 << valve_to_idx[next_valve]
        if not (mask & valve_bit):
            dist = distances[(cur, next_valve)]
            new_time = time_left - dist - 1
            if new_time > 0:
                p_released = new_time * flow
                res = p_released + dfs(next_valve, new_time, mask | valve_bit)
                max_p = max(max_p, res)
    return max_p

b = (1 << len(flow_rates)) - 1
m = float("-inf")
for i in range(b + 1):
    m = max(m, dfs("AA", 26, i) + dfs("AA", 26, b ^ i))
print(m)