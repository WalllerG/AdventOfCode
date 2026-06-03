with open('input.txt')as f:
    data = f.readlines()

ans = 0

for line in data:
    l, w, h = list(map(int, line.split('x')))
    ans += (2 * l * w) + (2 * h * w) + (2 * l * h) + min(l * w, l * h, w * h)

print(ans)