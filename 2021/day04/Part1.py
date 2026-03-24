from collections import defaultdict
with open("input.txt") as f:
    data = f.read().split("\n\n")
nums = list(map(int, data[0].split(",")))
boards_info = data[1:]
boards = defaultdict(list)
for i, board in enumerate(boards_info):
    for row in board.split("\n"):
        boards[i].append(list(map(int, row.strip().split())))

def check_win(grid):
    complete_row = False
    complete_col = False
    for r in grid:
        if set(r) == {-1}:
            complete_row = True
            break
    cols = list(zip(*grid))
    for c in cols:
        if set(c) == {-1}:
            complete_col = True
            break
    if complete_row or complete_col:
        return True
    return False

for num in nums:
    for board, vals in boards.items():
        for i in range(len(vals)):
            for j in range(len(vals[i])):
                if vals[i][j] == num:
                    vals[i][j] = -1
        if check_win(vals):
            print(num)
            print(vals)
            print(num * sum(sum(v for v in val if v != -1) for val in vals))
            exit()



