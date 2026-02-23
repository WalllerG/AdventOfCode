
from Util.util import read_input
import re

data = read_input(3, True)
result = 0
for line in data:
    combined_pattern = r"mul\((\d+),(\d+)\)|do\(\)|don't\(\)"
    matches = re.finditer(combined_pattern, line)
    for match in matches:
        full_match = match.group(0)
        enable = False
        disable = False
        if full_match == "do()":
            enable = True
            disable = False
        elif full_match == "don't()":
            disable = True
            enable = False
        else :
            if enable:
                x, y = match.groups()
                result += int(x) * int(y)



print(result)

