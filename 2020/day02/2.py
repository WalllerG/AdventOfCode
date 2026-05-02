with open('input.txt')as f:
    data = f.read().splitlines()

ans = 0

for line in data:
    count = 0
    bound, char, seq = line.split(' ')
    index1, index2 = list(map(int, bound.split('-')))
    char = char[0]
    if seq[index1-1] == char:
        count += 1
    if seq[index2-1] == char:
        count += 1
    if count == 1:
        ans += 1

print(ans)