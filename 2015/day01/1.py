with open('input.txt')as f:
    data = f.read()

ans = 0

for char in data:
    if char == '(':
        ans += 1
    else:
        ans -= 1

print(ans)