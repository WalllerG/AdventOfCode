with open('input.txt')as f:
    data = f.read().splitlines()

ans = 0

for line in data:
    bound, char, seq = line.split(' ')
    low, hi = list(map(int, bound.split('-')))
    char = char[0]
    count = seq.count(char)
    if low <= count <= hi:
        ans += 1

print(ans)