from Util.util import read_input
data = read_input(24,True)
wires = {}
x_lst = ""
y_lst = ""
n2s = []
xor_wires = []

count = 0
for line in data:
    if len(line) == 0:
        break
    else:
        name, value = line.split(":")
        wires[name] = int(value)
        if name.startswith("x"):
            x_lst += value.strip()
        elif name.startswith("y"):
            y_lst += value.strip()
    count += 1

operations = set()
for i in range(count+1, len(data)):
    operation = data[i].split(" ")
    op = (operation[0], operation[1], operation[2], operation[4])
    operations.add(op)
    if operation[4].startswith("z") and operation[1] != "XOR":
        n2s.append(op)
    if not operation[4].startswith("z") and operation[1] == "XOR":
        xor_wires.append(op)

def compute(left, o, right, des):
    if o == "AND":
        wires[des] = wires[left] & wires[right]
    elif o == "OR":
        wires[des] = wires[left] | wires[right]
    elif o == "XOR":
        wires[des] = wires[left] ^ wires[right]

def wiring(op_lst):
    while len(op_lst) !=0 :
        cur = op_lst.pop()
        l, op, r, d = cur[0], cur[1], cur[2], cur[3]
        if l not in wires or r not in wires:
            operations.add((l, op, r, d))
        else:
            compute(l,op,r,d)


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
            for next_in1, next_op, next_in2, next_out in gates:
                if (out == next_in1 or out == next_in2) and next_op != 'OR':
                    swapped.add(out)

    return ",".join(sorted(swapped))

print(find_swap_pairs(operations))
