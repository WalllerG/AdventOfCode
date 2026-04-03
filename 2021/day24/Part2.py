import sys
sys.setrecursionlimit(2000)
with open("input.txt") as f:
    blocks = f.read().split("inp w\n")[1:]
params = []
for block in blocks:
    lines = block.splitlines()
    a = int(lines[3].split()[-1])
    b = int(lines[4].split()[-1])
    c = int(lines[14].split()[-1])
    params.append((a, b, c))

memo = {}

def run_logic(z, digit, p):
    a, b, c = p
    x = (z % 26) + b
    z //= a
    if x != digit:
        z = z * 26 + digit + c
    return z


def find_model(idx, current_z, find_max=True):
    state = (idx, current_z)
    if state in memo:
        return memo[state]

    if idx == 14:
        return "" if current_z == 0 else None
    remaining_reductions = sum(1 for i in range(idx, 14) if params[i][0] == 26)
    if current_z >= (26 ** (remaining_reductions + 1)):
        return None

    digits = range(9, 0, -1) if find_max else range(1, 10)

    for d in digits:
        next_z = run_logic(current_z, d, params[idx])
        result = find_model(idx + 1, next_z, find_max)
        if result is not None:
            memo[state] = str(d) + result
            return memo[state]
    memo[state] = None
    return None

smallest = find_model(0, 0, find_max=False)
print(smallest)
