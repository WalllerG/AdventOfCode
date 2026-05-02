with open('input.txt')as f:
    data = f.read().splitlines()

best = 0
candidates = set(r*8 + c for c in range(8) for r in range(128))

for line in data:
    row = [0, 127]
    col = [0, 7]
    for char in line:
        if char == 'F':
            row[1] = (row[1]+row[0]-1) // 2
        elif char == 'B':
            row[0] = (row[1]+row[0]+1) // 2
        elif char == 'L':
            col[1] = (col[1]+col[0]-1) // 2
        elif char == 'R':
            col[0] = (col[1]+col[0]+1) // 2
    id = row[0] * 8 + col[0]
    candidates.remove(id)

print(candidates)