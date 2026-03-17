with open("input.txt") as f:
    data = f.read()
line = list(data)
start_pos = 4
for i in range(len(line)):
    if len(set(line[i:start_pos])) == 4:
        print(start_pos)
        break
    start_pos += 1

