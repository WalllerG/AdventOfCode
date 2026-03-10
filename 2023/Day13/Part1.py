with open("input.txt", "r") as file:
    data = file.read().strip()

ans = 0
for grid in data.split('\n\n'):
    rows = grid.split('\n')
    for i in range(1, len(rows)):
        top =  rows[:i]
        bottom = rows[i:]
        top_reverse = top[::-1]
        if all(t == b for t, b in zip(top_reverse, bottom)):
            ans += i * 100

    cols = list(zip(*rows))
    for c in range(1, len(cols)):
        left = cols[:c]
        right = cols[c:]
        left_reverse = left[::-1]
        if all(l == r for l, r in zip(left_reverse, right)):
            ans += c

print(ans)







