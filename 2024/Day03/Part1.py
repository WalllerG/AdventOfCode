from Util.util import read_input
import re

data = read_input(3, True)
result = 0
for line in data:
    matches = re.findall(r"mul\((\d+),(\d+)\)", line)
    for x, y in matches:
        result += (int(x) * int(y))

print(result)

