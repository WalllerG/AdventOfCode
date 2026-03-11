with open("input.txt") as f:
    data = f.readline()
ans = 0
def parse(s):
    cur = 0
    for char in s:
        cur += ord(char)
        cur = cur * 17 % 256
    return cur

for seq in data.split(","):
    ans += parse(seq)
print(ans)

