import time
with open('input.txt')as f:
    data = list(map(int, f.read().splitlines()))

start_time = time.time()
index = 0
contiguous = 0
start = 25

def solve(cur, target):
    all = set()
    for i in range(cur, cur+25):
        for j in range(i+1, cur+25):
            all.add(data[i] + data[j])
    return target in all

def find_sum(cur, target):
    sum = 0
    mini = 10 ** 9
    maxi = -1
    for i in range(cur, len(data)):
        mini = min(mini, data[i])
        maxi = max(maxi, data[i])
        sum += data[i]
        if sum == target:
            return (mini + maxi)
        if sum > target:
            return None
        
while solve(index, data[start]):
    index += 1
    start += 1

invalid = data[start]
    
while find_sum(contiguous, invalid) == None:
    contiguous += 1

print(find_sum(contiguous, invalid))
print(f'time: {time.time() - start_time}')
