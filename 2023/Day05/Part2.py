import re
file_path = "input.txt"
with open(file_path, 'r') as file:
    data = file.read()

segment = data.split('\n\n')
intervals = []
for s in re.findall(r'(\d+) (\d+)', segment[0]):
    x1, delta = map(int, s)
    x2 = x1 + delta
    intervals.append((x1, x2, 1))

min_loc = float('inf')

while intervals:
    x1, x2, index = intervals.pop()

    if index == 8:
        min_loc = min(x1, min_loc)
        continue

    for conversion in re.findall(r'(\d+) (\d+) (\d+)', segment[index]):
        dest, start, delta = map(int, conversion)
        end = start + delta
        diff = dest - start
        if x1 >= end or x2 <= start:
            continue
        if x1 < start:
            intervals.append((x1, start, index))
            x1 = start
        if x2 > end:
            intervals.append((end, x2, index))
            x2 = end
        intervals.append((x1+diff, x2+diff, index+1))
        break

    else:
        intervals.append((x1, x2, index+1))

print(min_loc)