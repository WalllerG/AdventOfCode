import re
import math
with open('input.txt')as f:
    data = f.read().splitlines()

ans = 0

def solve_simple(expr):
    parts = expr.split(' * ')
    sums = []
    for p in parts:
        sums.append(sum(map(int, p.split(' + '))))
    
    return math.prod(sums)

def evaluate(expr):
    while '(' in expr:
        expr = re.sub(r'\(([^()]+)\)', lambda m: str(solve_simple(m.group(1))), expr)
    return solve_simple(expr)

for line in data:
    line = " ".join(re.findall(r'\d+|[+*()]', line))
    ans += evaluate(line)

print(ans)