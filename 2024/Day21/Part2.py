from collections import deque
from functools import cache
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


key_paths = {}
all_p_n = [(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2),(3,1),(3,2)]
all_p_d = [(0,1),(0,2),(1,0),(1,1),(1,2)]

for start_p in all_p_n:
    for end_p in all_p_n:
            paths = find_all_sequences(num_keyboard, start_p, num_keyboard[end_p[0]][end_p[1]])
            key_paths[(num_keyboard[start_p[0]][start_p[1]],num_keyboard[end_p[0]][end_p[1]])] = paths

for start_p in all_p_d:
    for end_p in all_p_d:
        paths = find_all_sequences(dir_keyboard, start_p, dir_keyboard[end_p[0]][end_p[1]])
        key_paths[(dir_keyboard[start_p[0]][start_p[1]], dir_keyboard[end_p[0]][end_p[1]])] = paths


@cache
def get_min_length(sequence, level):
    if level == 0:
        return len(sequence)

    total_length = 0
    current_pos = 'A'

    for char in sequence:
        possible_paths = key_paths[(current_pos, char)]
        total_length += min(get_min_length(path, level - 1) for path in possible_paths)
        current_pos = char

    return total_length

for code, num in zip(codes, numeric_p):
    ans += get_min_length(code, 26) * num
print(ans)









