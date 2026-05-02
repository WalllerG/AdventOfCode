import re
with open('input.txt')as f:
    data = f.read().splitlines()

times = {index: 0 for index in range(len(data))}
cur = 0
acc = 0
while True:
    ins = data[cur]
    times[cur] += 1
    if any(v == 2 for v in times.values()):
        print(acc)
        break
    op, num = ins.split(' ')
    num = int(num)
    if op == 'jmp':
        cur += num
        continue
    if op == 'acc':
        acc += num
    cur += 1