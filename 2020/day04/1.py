with open('input.txt')as f:
    data = f.read().split('\n\n')

ans = 0
for person in data:
    count = 0
    cid = False
    for line in person.splitlines():
        if 'cid' in line:
            cid = True
        count += len(line.split(' '))
    if count == 8:
        ans += 1
    elif count == 7 and not cid:
        ans += 1

print(ans)