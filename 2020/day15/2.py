from collections import defaultdict
with open('input.txt')as f:
    data = list(map(int, f.read().split(',')))

memo = {}
turn = 0
for num in data:
    turn += 1
    memo[num] = [turn]
    
last = data[-1]
for _ in range(30000000-len(data)):
    turn += 1
    if len(memo[last]) == 1:
        last = 0
        memo[0].append(turn)
    else:
        last = memo[last][-1] - memo[last][len(memo[last])-2]
        if last in memo:
            memo[last].append(turn)
        else:
            memo[last] = [turn]
            
print(last)