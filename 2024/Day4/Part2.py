from Util.util import read_input
import re

lines = read_input(4, True)
result = 0
allShape = []
for i in range(0, len(lines)-2):
    for j in range(0, len(lines[0])-2):
        xShape = [lines[i][j], lines[i][j + 2], lines[i + 1][j + 1], lines[i + 2][j], lines[i + 2][j + 2]]
        line = "".join(xShape)
        allShape.append(line)

for line in allShape:
    patterns1 = re.findall(r"MSAMS", line)
    patterns2 = re.findall(r"MMASS", line)
    patterns3 = re.findall(r"SSAMM", line)
    patterns4 = re.findall(r"SMASM", line)
    result += len(patterns1) + len(patterns2) + len(patterns3) + len(patterns4)

print(result)


