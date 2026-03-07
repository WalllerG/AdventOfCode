from numpy.ma.core import bitwise_xor

from Util.util import read_input

data = read_input(22, True)
sn = [int(x) for x in data]
prune = 16777216
ans = 0

def get_secret_num(num):
    current = num
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

    return current

for s in sn:
    ans += get_secret_num(s)
print(ans)
