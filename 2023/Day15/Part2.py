import re
from collections import defaultdict

with open("input.txt") as f:
    data = f.readline()
ans = 0
hashmap = defaultdict(list)
box_num_map = {}
focal_length_map = {}
index_map = defaultdict(int)

def get_box_num(line):
    for line in line.split(","):
        chars = re.findall(r"([a-z]+)", line)
        box_num_map[chars[0]] = parse(chars[0])

def parse(s):
    cur = 0
    for char in s:
        cur += ord(char)
        cur = cur * 17 % 256
    return cur

get_box_num(data)
for seq in data.split(","):
    pattern = re.findall(r"([a-z]+)([=-])(\d+)?",seq)

    for c, op, lens in pattern:
        if op == "=":
            box_num = box_num_map[c]
            if c not in hashmap[box_num]:
                if len(hashmap[box_num]) == 0:
                    hashmap[box_num].append(c)
                    index_map[c] = 1
                    focal_length_map[c] = lens
                else:
                    last_index = index_map[hashmap[box_num][-1]]
                    last = hashmap[box_num][-1]
                    index_map[c] = last_index + 1
                    focal_length_map[c] = lens
                    hashmap[box_num].append(c)
            else:
                focal_length_map[c] = lens
        elif op == "-":
            box_num = box_num_map[c]
            if c not in hashmap[box_num]:
                continue
            else:
                cur_ind  = index_map[c]
                if len(hashmap[box_num]) == 1:
                    hashmap[box_num].remove(c)
                    index_map.pop(c)
                    focal_length_map.pop(c)
                else:
                    for i in range(cur_ind,len(hashmap[box_num])):
                        index_map[hashmap[box_num][i]] = index_map[hashmap[box_num][i]] - 1
                    hashmap[box_num].remove(c)
                    index_map.pop(c)
                    focal_length_map.pop(c)

for key in hashmap:
    for c in hashmap[key]:
        a = key+1
        index = index_map[c]
        focal_length = int(focal_length_map[c])
        ans += a * focal_length * index
print(ans)




