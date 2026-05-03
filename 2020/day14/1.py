import re
from collections import defaultdict
with open('input.txt')as f:
    data = f.read().splitlines()

cur = None
memo = defaultdict(int)

for line in data:
    if line.startswith('mask ='):
        cur = list(line.split(' = ')[1])
        continue
    address, val = list(map(int, re.findall(r'\d+', line)))
    copy = cur[::-1]
    val = bin(val)[2:][::-1]
    for i in range(len(val)):
        if copy[i] == 'X':
            copy[i] = val[i]
    for i in range(len(copy)):
        if copy[i] == 'X':
            copy[i] = '0'
    copy = copy[::-1]
    memo[address] = int("".join(copy), 2)

print(sum(memo.values()))
