from numpy.ma.core import bitwise_xor
from Util.util import read_input

data = read_input(17, True)

p1 = [[data[0]],[data[1]],[data[2]]]
p2 = [int (x) for x in data[4].split(":")[1].split(",")]
registers = {"A": int (data[0].split(":")[1]), "B": int (data[1].split(":")[1]), "C": int (data[2].split(":")[1])}
program = []
for i in range(0,len(p2)-1,2):
    program.append((p2[i],p2[i+1]))

opcode_5_output = []

count = 0
while count < len(program):
    opcode = program[count][0]
    operand = program[count][1]
    if opcode == 0:
        numerator = registers["A"]
        if 0 <= operand <= 3:
            registers["A"] = numerator // pow(2, operand)
        elif operand == 4:
            value = registers["A"]
            registers["A"] = numerator // pow(2, value)
        elif operand == 5:
            value = registers["B"]
            registers["A"] = numerator // pow(2, value)
        elif operand == 6:
            value = registers["C"]
            registers["A"] = numerator // pow(2, value)

    elif opcode == 1:
        value = registers["B"]
        registers["B"] = bitwise_xor(value, operand)

    elif opcode == 2:
        if 0 <= operand <= 3:
            registers["B"] = operand % 8
        elif operand == 4:
            value = registers["A"]
            registers["B"] = value % 8
        elif operand == 5:
            value = registers["B"]
            registers["B"] = value % 8
        elif operand == 6:
            value = registers["C"]
            registers["B"] = value % 8

    elif opcode == 3:
        value = registers["A"]
        p2j = operand // 2
        if value != 0:
            count = p2j
            continue

    elif opcode == 4:
        v1 = registers["B"]
        v2 = registers["C"]
        registers["B"] = bitwise_xor(v1, v2)

    elif opcode == 5:
        if 0 <= operand <= 3:
            result = operand % 8
            opcode_5_output.append(result)
        elif operand == 4:
            value = registers["A"]
            result = value % 8
            opcode_5_output.append(result)
        elif operand == 5:
            value = registers["B"]
            result = value % 8
            opcode_5_output.append(result)
        elif operand == 6:
            value = registers["C"]
            result = value % 8
            opcode_5_output.append(result)
    elif opcode == 6:
        numerator = registers["A"]
        if 0 <= operand <= 3:
            registers["B"] = numerator // pow(2, operand)
        elif operand == 4:
            value = registers["A"]
            registers["B"] = numerator // pow(2, value)
        elif operand == 5:
            value = registers["B"]
            registers["B"] = numerator // pow(2, value)
        elif operand == 6:
            value = registers["C"]
            registers["B"] = numerator // pow(2, value)

    elif opcode == 7:
        numerator = registers["A"]
        if 0 <= operand <= 3:
            registers["C"] = numerator // pow(2, operand)
        elif operand == 4:
            value = registers["A"]
            registers["C"] = numerator // pow(2, value)
        elif operand == 5:
            value = registers["B"]
            registers["C"] = numerator // pow(2, value)
        elif operand == 6:
            value = registers["C"]
            registers["C"] = numerator // pow(2, value)

    count += 1

ans = ",".join(str(j) for j in opcode_5_output)
print(ans)