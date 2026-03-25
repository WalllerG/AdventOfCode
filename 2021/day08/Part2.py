with open("input.txt") as f:
    data = f.read().split("\n")
ans = 0
for line in data:
    patterns_str, output_str = line.split(" | ")
    patterns = ["".join(sorted(p)) for p in patterns_str.split()]
    outputs = ["".join(sorted(o)) for o in output_str.split()]
    mapping = {}
    rev_mapping = {}
    for p in patterns:
        if len(p) == 2:
            mapping[1] = set(p)
        elif len(p) == 4:
            mapping[4] = set(p)
        elif len(p) == 3:
            mapping[7] = set(p)
        elif len(p) == 7:
            mapping[8] = set(p)
    final_map = {}
    for p in patterns:
        val = 0
        s = set(p)
        length = len(p)
        if length == 2:
            val = 1
        elif length == 3:
            val = 7
        elif length == 4:
            val = 4
        elif length == 7:
            val = 8
        elif length == 5:
            if len(s & mapping[1]) == 2:
                val = 3
            elif len(s & mapping[4]) == 3:
                val = 5
            else:
                val = 2
        elif length == 6:
            if len(s & mapping[1]) == 1:
                val = 6
            elif len(s & mapping[4]) == 4:
                val = 9
            else:
                val = 0
        final_map[p] = str(val)
    res = "".join(final_map[o] for o in outputs)
    ans += int(res)
print(ans)
