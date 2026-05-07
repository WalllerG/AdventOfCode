with open('input.txt') as f:
    p1, p2 = f.read().split('\n\n')

d1 = [int(line) for line in p1.splitlines()[1:]]
d2 = [int(line) for line in p2.splitlines()[1:]]

def play_game(p1, p2):
    seen = set()
    
    while p1 and p2:
        state = (tuple(p1), tuple(p2))
        if state in seen:
            return 1, p1
        seen.add(state)

        c1 = p1.pop(0)
        c2 = p2.pop(0)

        if len(p1) >= c1 and len(p2) >= c2:
            winner, _ = play_game(p1[:c1], p2[:c2])
        else:
            winner = 1 if c1 > c2 else 2

        if winner == 1:
            p1.extend([c1, c2])
        else:
            p2.extend([c2, c1])

    return (1, p1) if p1 else (2, p2)

winner_id, final_deck = play_game(d1, d2)
ans = sum(card * i for i, card in enumerate(reversed(final_deck), 1))

print(ans)