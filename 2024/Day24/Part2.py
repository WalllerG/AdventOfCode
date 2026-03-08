from Util.util import read_input
data = read_input(24,True)
wires = {}
operations = set()

count = 0
for line in data:
    if len(line) == 0:
        break
    else:
        name, value = line.split(":")
        wires[name] = int(value)
    count += 1

for i in range(count+1, len(data)):
    operation = data[i].split(" ")
    ope = (operation[0], operation[1], operation[2], operation[4])
    operations.add(ope)

def find_swap_pairs(gates):
    swapped = set()
    for l, op, r, out in gates:
        if out.startswith('z') and op != 'XOR' and out != 'z45':
            swapped.add(out)

        if op == 'XOR':
            if not out.startswith('z') and not (l[0] in 'xy' and l[0] in 'xy'):
                swapped.add(out)

        if op == 'XOR' and (l[0] in 'xy' and r[0] in 'xy'):
            if "00" not in l and "00" not in r:
                for nl, nop, nr, n_out in gates:
                    if (out == nl or out == nr) and nop == 'OR':
                        swapped.add(out)

        if op == 'AND' and "00" not in l and "00" not in r:
            for nl, nop, nr, n_out in gates:
                if (out == nl or out == nr) and nop != 'OR':
                    swapped.add(out)

    return ",".join(sorted(swapped))

print(find_swap_pairs(operations))
