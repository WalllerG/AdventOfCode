with open("input.txt") as f:
    data = list(map(int, f.read().split("\n")))
ans = 0
for i in range(len(data)-1):
    if data[i+1] > data[i]:
        ans += 1
print(ans)
