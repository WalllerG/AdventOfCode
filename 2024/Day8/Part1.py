from Util.util import read_input

data = read_input(8,False)
signalMap = {}
grid = []

for i in range(len(data)):
    line = list(data[i])
    for j in range(len(line)):
        if len(set(line)) == 1:
            break
        elif line[j] not in signalMap and line[j] != ".":
            signalMap[line[j]] = []
            signalMap[line[j]].append([i,j])
        elif line[j] != ".":
            signalMap[line[j]].append([i,j])

for lines in data:
    row = []
    line = list(lines)
    for line in lines:
        row.append(line)
    grid.append(row)

print(signalMap)
