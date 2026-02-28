from Util.util import read_input

data = read_input(8,True)
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
        mappedLine = False
        row.append(mappedLine)
    grid.append(row)

result = 0

for signal in signalMap:
    for i in range(len(signalMap[signal])):
        for j in range(i+1, len(signalMap[signal])):
            if signalMap[signal][j][1] <= signalMap[signal][i][1]:
                rightXcoor = signalMap[signal][i][0] - abs(signalMap[signal][j][0] - signalMap[signal][i][0])
                rightYcoor = signalMap[signal][i][1] + abs(signalMap[signal][j][1] - signalMap[signal][i][1])
                leftXcoor = signalMap[signal][j][0] + abs(signalMap[signal][j][0] - signalMap[signal][i][0])
                leftYcoor = signalMap[signal][j][1] - abs(signalMap[signal][j][1] - signalMap[signal][i][1])

                if -1 < leftXcoor < len(grid[0]) and -1 < leftYcoor < len(grid):
                    if grid[leftXcoor][leftYcoor] == False:
                        grid[leftXcoor][leftYcoor] = True
                        result += 1
                if -1 < rightXcoor < len(grid[0]) and -1 < rightYcoor < len(grid):
                    if grid[rightXcoor][rightYcoor] == False:
                        grid[rightXcoor][rightYcoor] = True
                        result += 1

            elif signalMap[signal][j][1] > signalMap[signal][i][1]:
                rightXcoor = signalMap[signal][j][0] + abs(signalMap[signal][j][0] - signalMap[signal][i][0])
                rightYcoor = signalMap[signal][j][1] + abs(signalMap[signal][j][1] - signalMap[signal][i][1])
                leftXcoor = signalMap[signal][i][0] - abs(signalMap[signal][j][0] - signalMap[signal][i][0])
                leftYcoor = signalMap[signal][i][1] - abs(signalMap[signal][j][1] - signalMap[signal][i][1])

                if -1 < leftXcoor < len(grid[0]) and -1 < leftYcoor < len(grid):
                    if grid[leftXcoor][leftYcoor] == False:
                        grid[leftXcoor][leftYcoor] = True
                        result += 1
                if -1 < rightXcoor < len(grid[0]) and -1 < rightYcoor < len(grid):
                    if grid[rightXcoor][rightYcoor] == False:
                        grid[rightXcoor][rightYcoor] = True
                        result += 1


print(result)
