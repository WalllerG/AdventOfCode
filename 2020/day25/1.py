import time
with open('input.txt')as f:
    card, door = [int(line) for line in f.read().splitlines()]

start_time = time.time()

def get_key(num):
    loop_size = 1
    while True:
        val = pow(7, loop_size, 20201227)
        if val == num:
            return loop_size
        loop_size += 1

card_key = get_key(card)
door_key = get_key(door)

print(pow(card, door_key, 20201227))
print(f'time: {time.time()-start_time}')

    

