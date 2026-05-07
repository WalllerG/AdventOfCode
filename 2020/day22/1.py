from collections import deque
with open('input.txt')as f:
    p1, p2 = f.read().split('\n\n')

p1_deck = deque([int(line) for line in p1.splitlines()[1:]])
p2_deck = deque([int(line) for line in p2.splitlines()[1:]])
round = 0
ans = 0

while p1_deck and p2_deck:
    round += 1
    top1 = p1_deck.popleft()
    top2 = p2_deck.popleft()
    if top1 > top2:
        p1_deck.append(top1)
        p1_deck.append(top2)
    elif top2 > top1:
        p2_deck.append(top2)
        p2_deck.append(top1)

winner = p1_deck if len(p1_deck) != 0 else p2_deck

for i, card in enumerate(range(len(winner)-1, -1, -1), start=1):
    ans += i * winner[card]

print(ans)