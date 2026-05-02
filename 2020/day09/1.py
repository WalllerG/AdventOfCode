with open('input.txt')as f:
    data = list(map(int, f.read().splitlines()))

index = 0
start = 25
def solve(cur, target):
    all = set()
    for i in range(cur, cur+25):
        for j in range(i+1, cur+25):
            all.add(data[i] + data[j])
    return target in all

while solve(index, data[start]):
    index += 1
    start += 1

print(data[start])