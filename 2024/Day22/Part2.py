from collections import defaultdict
from numpy.ma.core import bitwise_xor
from Util.util import read_input

data = read_input(22, True)
sn = [int(x) for x in data]
prune = 16777216
ans = 0

def get_secret_num(num):
    current = num

    seq = [current % 10]
    for _ in range(2000):
        mult = current * 64
        cs_1 = bitwise_xor(current,mult) % prune
        current = cs_1

        div = current // 32
        cs_2 = bitwise_xor(current,div) % prune
        current = cs_2

        mult2 = current * 2048
        cs_3 = bitwise_xor(current,mult2) % prune
        current = cs_3

        seq.append(int (current % 10))

    return seq

def get_change_seq (s_num):
    s = get_secret_num(s_num)
    changes = []
    for i in range(len(s)-1):
        diff = s[i+1] - s[i]
        changes.append(diff)
    return changes

score =  defaultdict(int)
for s in sn:
    seen = set()
    sequence = get_secret_num(s)
    changes = get_change_seq(s)
    for i in range (2000 - 3):
        z = tuple(changes[i:i+4])
        if z not in seen:
            score[z] += sequence[i+4]
            seen.add(z)

print(max(score.values()))













