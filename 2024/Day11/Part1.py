from collections import Counter

from Util.util import read_input

data = read_input(11, True)
stone_counts = Counter(map(int, data[0].split()))

def solve(counts, blinks):
    for _ in range(blinks):
        new_counts = Counter()
        for stone, qty in counts.items():

            if stone == 0:
                new_counts[1] += qty

            elif len(str(stone)) % 2 == 0:
                s = str(stone)
                mid = len(s) // 2
                left = int(s[:mid])
                right = int(s[mid:])
                new_counts[left] += qty
                new_counts[right] += qty

            else:
                new_counts[stone * 2024] += qty

        counts = new_counts

    return sum(counts.values())

print(solve(stone_counts, 25))