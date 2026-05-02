with open('input.txt')as f:
    data = f.read().split('\n\n')

ans = 0

for group in data:
    yes = set()
    for line in group.splitlines():
        yes |= set(line)
    ans += len(yes)

print(ans)