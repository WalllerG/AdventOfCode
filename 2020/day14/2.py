import re
import itertools

with open('input.txt') as f:
    data = f.read().splitlines()

mask = None
memo = {}

for line in data:
    if line.startswith('mask ='):
        mask = line.split(' = ')[1]
        continue
    address, val = list(map(int, re.findall(r'\d+', line)))
    addr_bin = list(bin(address)[2:].zfill(36))
    floating_indices = []
    for i in range(36):
        if mask[i] == '1':
            addr_bin[i] = '1'
        elif mask[i] == 'X':
            addr_bin[i] = 'X'
            floating_indices.append(i)
    for combo in itertools.product(['0', '1'], repeat=len(floating_indices)):
        temp_addr = list(addr_bin)
        for idx, bit in zip(floating_indices, combo):
            temp_addr[idx] = bit
        final_address = int("".join(temp_addr), 2)
        memo[final_address] = val

print(sum(memo.values()))