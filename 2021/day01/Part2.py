with open("input.txt") as f:
    data = list(map(int, f.read().split("\n")))
ans = 0
groups = []
for i in range(len(data)-2):
    num = sum(data[i:i+3])
    groups.append(num)
for i in range(len(groups)-1):
    if groups[i+1] > groups[i]:
        ans += 1
print(ans)

