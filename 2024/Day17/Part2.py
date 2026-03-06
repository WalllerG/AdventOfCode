from Util.util import read_input

data = read_input(17, True)

p2 = [int (x) for x in data[4].split(":")[1].split(",")]

def solve(target, current_a):
    if not target:
        return current_a

    for next_three_bits in range(8):
        a = (current_a << 3) | next_three_bits

        b = (a % 8) ^ 1
        c = a // (2 ** b)
        result = (b ^ c ^ 4) % 8

        if result == target[-1]:
            sub_res = solve(target[:-1], a)
            if sub_res is not None:
                return sub_res
    return None


print(solve(p2,0))