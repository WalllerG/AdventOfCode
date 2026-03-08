from Util.util import read_input
data = read_input(24,True)
wires = {}

count = 0
for line in data:
    if len(line) == 0:
        break
    else:
        name, value = line.split(":")
        wires[name] = int(value)
    count += 1

operations = set()
for i in range(count+1, len(data)):
    operation = data[i].split(" ")
    op = (operation[0], operation[1], operation[2], operation[4])
    operations.add(op)

def compute(left, o, right, des):
    if o == "AND":
        wires[des] = wires[left] & wires[right]
    elif o == "OR":
        wires[des] = wires[left] | wires[right]
    elif o == "XOR":
        wires[des] = wires[left] ^ wires[right]


while len(operations) !=0 :
    cur = operations.pop()
    l, op, r, d = cur[0], cur[1], cur[2], cur[3]
    if l not in wires or r not in wires:
        operations.add((l, op, r, d))
    else:
        compute(l,op,r,d)

z_lst = []
for wire in wires.keys():
    if wire.startswith("z"):
        z_lst.append(wire)

z_lst.sort()
z_lst.reverse()
result = ""
for z in z_lst:
    result += str(wires[z])

ans = int(result, 2)
print(ans)










