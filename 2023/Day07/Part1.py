from functools import cmp_to_key
from Util.util import read_input

data = read_input(True)
wining = {}
ranks = {}
ans = 0
card_ranks = {"A": 13, "2": 1, "3": 2, "4": 3, "5": 4, "6": 5, "7": 6, "8": 7, "9": 8, "T": 9, "J": 10, "Q": 11, "K": 12}
for line in data:
    hand= line.split(" ")
    wining[hand[0]] = int(hand[1])

def get_type(h):
    rank = 0
    card_m = {"A": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0, "T": 0, "J": 0, "Q": 0, "K": 0}
    cards = list(h)
    for card in cards:
        card_m[card] += 1
    if 5 in card_m.values():
        return 5
    if 4 in card_m.values():
        return 4
    if 3 in card_m.values():
        if 2 in card_m.values():
            return 3
        else:
            return 2
    for v in card_m.values():
        if v == 2:
            rank += 1
    if rank == 2:
        return 1
    if rank == 1:
        return 0
    return -1

for win in wining:
    r = get_type(win)
    ranks[win] = r

def compare(hand1, hand2):
    v1, v2 = hand1[1], hand2[1]
    hand1 = list(hand1[0])
    hand2 = list(hand2[0])
    if v1 > v2:
        return 1
    elif v1 < v2:
        return -1
    else:
        for h1, h2 in zip(hand1, hand2):
            if card_ranks[h1] > card_ranks[h2]:
                return 1
            elif card_ranks[h1] == card_ranks[h2]:
                continue
            else:
                return -1
        return 0

sorted_cards = dict(sorted(ranks.items(), key=cmp_to_key(compare)))
print(sorted_cards)
cur = 1
for card in sorted_cards:
    sorted_cards[card] = cur
    cur += 1

for card in sorted_cards.keys():
    ans += sorted_cards[card] * wining[card]
print(ans)






