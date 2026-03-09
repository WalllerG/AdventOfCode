from collections import defaultdict
from Util.util import read_input
data = read_input(True)

cards = defaultdict(int)

ans = 0
for i in range(len(data)):
    nums = data[i].split(":")[-1]
    win_nums, num_to_match = nums.strip().split("|")
    wns = [int(x) for x in win_nums.split()]
    to_match = [int(y) for y in num_to_match.split()]
    count = 0
    for wn in wns:
        if wn in to_match:
           count += 1

    for j in range(0, count):
        cards[i+j+1] += 1

    if count == 0:
        cards[i] += 0
    if count != 0:
        for k in range(0, cards[i]):
            count = 0
            for wn in wns:
                if wn in to_match:
                    count += 1

            for j in range(0, count):
                cards[i + j + 1] += 1


for v in cards.values():
    ans += v+1
print(ans)