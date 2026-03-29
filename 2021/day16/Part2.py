import math
with open("input.txt") as f:
    data = f.read()
total_versions = 0
binary_string = "".join([bin(int(c, 16))[2:].zfill(4) for c in data.strip()])
def parse_literal(bits, pointer):
    binary_value = ""
    while True:
        chunk = bits[pointer: pointer + 5]
        pointer += 5
        binary_value += chunk[1:]
        if chunk[0] == '0':
            break
    return int(binary_value, 2), pointer

def parse_packet(bits, pointer):
    global total_versions
    version = int(bits[pointer: pointer + 3], 2)
    type_id = int(bits[pointer + 3: pointer + 6], 2)
    pointer += 6
    total_versions += version
    if type_id == 4:
        value, pointer = parse_literal(bits, pointer)
        return value, pointer
    else:
        length_id = bits[pointer]
        pointer += 1
        sub_packet_values = []

        if length_id == '0':
            total_sub_bits = int(bits[pointer: pointer + 15], 2)
            pointer += 15
            start_ptr = pointer
            while pointer < start_ptr + total_sub_bits:
                val, pointer = parse_packet(bits, pointer)
                sub_packet_values.append(val)

        else:
            num_sub_packets = int(bits[pointer: pointer + 11], 2)
            pointer += 11
            for _ in range(num_sub_packets):
                val, pointer = parse_packet(bits, pointer)
                sub_packet_values.append(val)

        return execute_operation(type_id, sub_packet_values), pointer

def execute_operation(type_id, values):
    if type_id == 0: return sum(values)
    if type_id == 1: return math.prod(values)
    if type_id == 2: return min(values)
    if type_id == 3: return max(values)
    if type_id == 5: return 1 if values[0] > values[1] else 0
    if type_id == 6: return 1 if values[0] < values[1] else 0
    if type_id == 7: return 1 if values[0] == values[1] else 0
    return 0

fv, fp = parse_packet(binary_string, 0)
print(fv)