with open("input.txt", "r") as file:
    data = file.read()

ans = 0
for grid in data.split('\n\n'):
    rows = grid.split('\n')

    r_for_row = 0
    r_for_col = 0
    is_row = False
    for i in range(len(rows)-1):
        last = rows[-1]
        cur = rows[i]
        if cur == last:
            j = len(rows)-1
            while i < j:
                i += 1
                j -= 1
            r_for_row = i
            ans += r_for_row * 100
            break

    cols = list(zip(*rows))
    for i in range(len(cols) - 1):
        last = cols[-1]
        cur = cols[i]
        if cur == last:
            j = len(cols) - 1
            while i < j:
                i += 1
                j -= 1
            r_for_col = i
            ans += r_for_col
            break


print(ans)







