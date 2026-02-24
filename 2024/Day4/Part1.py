from Util.util import read_input
import re
lines = read_input(4, False)

for line in lines:
    patterns = re.findall(r"SAMX|XMAS", line)
print(len(patterns))

