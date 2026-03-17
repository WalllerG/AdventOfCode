with open("input.txt") as f:
    data = f.read()
import string
alpha_map = {char: i for i, char in enumerate(string.ascii_letters, 1)}
ans = 0
for line in data.split("\n"):
    a, b = line[:len(line) // 2], line[len(line) // 2:]
    left = set(list(a))
    right = set(list(b))
    for x in left:
        if x in right:
            ans += alpha_map[x]
print(ans)
