with open("input.txt") as f:
    data = f.read().split('\n')
p1 = int(data[0].split(' ')[-1])
p2 = int(data[1].split(' ')[-1])
score1 = 0
score2 = 0
rolled = 0
count = 1
while True:
    for i in range(count, count+99, 3):
        moves = 3 * i + 3
        rolled += 3
        if i % 2 != 0:
            p1 = (p1 + moves % 10) % 10 if p1 + moves % 10 != 10 else p1 + moves % 10
            score1 += p1
        else:
            p2 = (p2 + moves % 10) % 10 if p2 + moves % 10 != 10 else p2 + moves % 10
            score2 += p2
        if score1 >= 1000 or score2 >= 1000:
            print(score1, score2, rolled)
            print(min(score1, score2) * rolled)
            exit()
    count = count+99