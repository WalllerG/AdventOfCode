import itertools
from collections import deque

from Util.util import read_input

data = read_input(21, True)

ans = 0
codes = []
numeric_p = []
num_keyboard =[
    ["7","8","9"],
    ["4","5","6"],
    ["1","2","3"],
    [".","0","A"],
]

dir_keyboard = [
    [".","^","A"],
    ["<","v",">"],
]

for line in data:
    codes.append(line)
    numeric_p.append(int(line[:3]))


def find_all_sequences(keyboard, start_coords, target_char):
    rows = len(keyboard)
    cols = len(keyboard[0])
    r_start, c_start = start_coords

    queue = deque([(r_start, c_start, "")])
    distances = {(r_start, c_start): 0}
    all_shortest_paths = []
    min_len = float('inf')

    while queue:
        r, c, path = queue.popleft()

        if keyboard[r][c] == target_char:
            if len(path) <= min_len:
                min_len = len(path)
                all_shortest_paths.append(path + "A")
            continue

        if len(path) >= min_len:
            continue

        for dr, dc, symbol in [(0, 1, ">"), (0, -1, "<"), (1, 0, "v"), (-1, 0, "^")]:
            nr, nc = r + dr, c + dc

            if 0 <= nr < rows and 0 <= nc < cols and keyboard[nr][nc] != ".":
                new_path = path + symbol

                if (nr, nc) not in distances or len(new_path) <= distances[(nr, nc)]:
                    distances[(nr, nc)] = len(new_path)
                    queue.append((nr, nc, new_path))

    return all_shortest_paths


def get_sequence(keyboard, co, start_pos):
    current_pos = start_pos
    all_parts = []

    for char in co:
        paths = find_all_sequences(keyboard, current_pos, char)
        all_parts.append(paths)

        for r in range(len(keyboard)):
            for c in range(len(keyboard[0])):
                if keyboard[r][c] == char:
                    current_pos = (r, c)


    return ["".join(p) for p in itertools.product(*all_parts)]


def get_final_sequence(c):
    res = ""
    first_s = get_sequence(num_keyboard, c, (3, 2))
    second_s = []
    final_s = []
    shortest = float('inf')
    for s in first_s:
        sub_s1 = get_sequence(dir_keyboard, s, (0, 2))
        for s1 in sub_s1:
            second_s.append(s1)
    for s in second_s:
        sub_s1 = get_sequence(dir_keyboard, s, (0, 2))
        for s1 in sub_s1:
            if len(s1) < shortest:
                final_s.append(s1)
                shortest = len(s1)
    shortest = float('inf')
    for s in final_s:
        if len(s) < shortest:
            res = s
            shortest = len(s)

    return res

for code, num in zip(codes, numeric_p):
    ans += len(get_final_sequence(code)) * num
print(ans)










