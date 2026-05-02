from copy import deepcopy
import time
with open('input.txt')as f:
    data = f.read().splitlines()

start_time = time.time()
swap = [i for i in range(len(data)) if data[i].split(' ')[0] == 'nop' or data[i].split(' ')[0] == 'jmp']
swap_index = 0
success = False

def change(s, index):
    new_data = deepcopy(s)
    to_change = new_data[index].split(' ')
    if to_change[0] == 'nop':
        to_change[0] = 'jmp'
    elif to_change[0] == 'jmp':
        to_change[0] = 'nop'
    new_data[index] = " ".join(to_change)
    return new_data

while not success:
    D = change(data, swap_index)
    times = {index: 0 for index in range(len(D))}
    cur = 0
    acc = 0
    while True:
        if cur == len(D):
            success = True
            print(f'success: {acc}')
            print(f'time: {time.time() - start_time}')
            break
        ins = D[cur]
        times[cur] += 1
        if any(v == 2 for v in times.values()):
            break
        op, num = ins.split(' ')
        num = int(num)
        if op == 'jmp':
            cur += num
            continue
        if op == 'acc':
            acc += num
        cur += 1
    swap_index += 1