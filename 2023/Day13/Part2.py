with open("input.txt", "r") as file:
    data = file.read().strip()

ans = 0
def check_symmetric(grid, prev=0):
    for i in range(1, len(grid)):
        top = grid[:i]
        bottom = grid[i:]
        top_reverse = top[::-1]
        if all(t == b for t, b in zip(top_reverse, bottom)):
            val = i * 100
            if val != prev: return val

    cols = list(zip(*grid))
    for c in range(1, len(cols)):
        left = cols[:c]
        right = cols[c:]
        left_reverse = left[::-1]
        if all(l == r for l, r in zip(left_reverse, right)):
            if c != prev: return c
    return 0

for mirror in data.split('\n\n'):
    gr = [list(line) for line in mirror.split('\n')]
    go_next = False
    ov = check_symmetric(gr)
    for x in range(len(gr)):
        for y in range(len(gr[x])):
            old_char = gr[x][y]
            gr[x][y] = '#' if old_char == '.' else '.'
            nv = check_symmetric(gr,ov)
            if nv > 0:
                ans += nv
                go_next = True
                break
            gr[x][y] = old_char
        if go_next:
            break
print(ans)








