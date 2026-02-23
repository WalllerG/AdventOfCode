from Util.util import read_input
import re

data = read_input(3, False)

matches = re.findall(r"mul\((\d+),(\d+)\)", data[0])

result = 0
for x, y in matches:
    result += (int(x) * int(y))

print(result)

