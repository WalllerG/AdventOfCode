with open("input.txt") as f:
    data = f.read()
import string
alpha_map = {char: i for i, char in enumerate(string.ascii_letters, 1)}
ans = 0
line = data.split("\n")

for i in range(0, len(line), 3):
    a,b,c = line[i], line[i+1], line[i+2]
    x, y, z = set(list(a)), set(list(b)), set(list(c))
    for x in x:
        if x in y and x in z:
            ans += alpha_map[x]
print(ans)