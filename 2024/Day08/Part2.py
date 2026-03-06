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
        if len(signalMap[signal]) > 1:
            grid[signalMap[signal][i][0]][signalMap[signal][i][1]] = True
        for j in range(i+1, len(signalMap[signal])):
            if signalMap[signal][j][1] <= signalMap[signal][i][1]:
                count = 1

                XcoorDiff = abs(signalMap[signal][j][0] - signalMap[signal][i][0])
                YcoorDiff = abs(signalMap[signal][j][1] - signalMap[signal][i][1])


                rightXcoor = signalMap[signal][i][0] - XcoorDiff
                rightYcoor = signalMap[signal][i][1] + YcoorDiff
                leftXcoor = signalMap[signal][j][0] + XcoorDiff
                leftYcoor = signalMap[signal][j][1] - YcoorDiff

                while -1 < leftXcoor < len(grid[0]) and -1 < leftYcoor < len(grid):

                    if grid[leftXcoor][leftYcoor] == False:
                        grid[leftXcoor][leftYcoor] = True


                    count += 1
                    leftXcoor = signalMap[signal][j][0] + (count * XcoorDiff)
                    leftYcoor = signalMap[signal][j][1] - (count * YcoorDiff)


                count = 1

                while -1 < rightXcoor < len(grid[0]) and -1 < rightYcoor < len(grid):

                    if grid[rightXcoor][rightYcoor] == False:
                        grid[rightXcoor][rightYcoor] = True

                    count += 1
                    rightXcoor = signalMap[signal][i][0] - (count * XcoorDiff)
                    rightYcoor = signalMap[signal][i][1] + (count * YcoorDiff)


            elif signalMap[signal][j][1] > signalMap[signal][i][1]:
                count = 1

                XcoorDiff = abs(signalMap[signal][j][0] - signalMap[signal][i][0])
                YcoorDiff = abs(signalMap[signal][j][1] - signalMap[signal][i][1])

                rightXcoor = signalMap[signal][j][0] + XcoorDiff
                rightYcoor = signalMap[signal][j][1] + YcoorDiff
                leftXcoor = signalMap[signal][i][0] - XcoorDiff
                leftYcoor = signalMap[signal][i][1] - YcoorDiff

                while -1 < leftXcoor < len(grid[0]) and -1 < leftYcoor < len(grid):

                    if grid[leftXcoor][leftYcoor] == False:
                        grid[leftXcoor][leftYcoor] = True

                    count += 1
                    leftXcoor = signalMap[signal][j][0] - (count * XcoorDiff)
                    leftYcoor = signalMap[signal][j][1] - (count * YcoorDiff)

                count = 1

                while -1 < rightXcoor < len(grid[0]) and -1 < rightYcoor < len(grid):

                    if grid[rightXcoor][rightYcoor] == False:
                        grid[rightXcoor][rightYcoor] = True

                    count += 1
                    rightXcoor = signalMap[signal][j][0] + (count * XcoorDiff)
                    rightYcoor = signalMap[signal][j][1] + (count * YcoorDiff)

for row in grid:
    for column in row:
        if column == True:
            result += 1

print(result)
