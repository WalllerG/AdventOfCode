with open('input.txt')as f:
    data = f.readlines()

ans = 0

for line in data:
    a, b, c = sorted(list(map(int, line.split('x'))))
    ans += (2 * (a + b)) + (a * b * c)

print(ans)