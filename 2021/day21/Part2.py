import functools
with open("input.txt") as f:
    data = f.read().split('\n')
p1 = int(data[0].split(' ')[-1])
p2 = int(data[1].split(' ')[-1])
score1 = 0
score2 = 0
ROLL_DISTRIBUTION = {3: 1, 4: 3, 5: 6, 6: 7, 7: 6, 8: 3, 9: 1}
@functools.lru_cache(None)
def count_wins(p1_pos, p1_score, p2_pos, p2_score, is_p1_turn):
    if p1_score >= 21:
        return 1, 0
    if p2_score >= 21:
        return 0, 1
    total_p1_wins = 0
    total_p2_wins = 0
    if is_p1_turn:
        for roll_sum, freq in ROLL_DISTRIBUTION.items():
            new_pos = (p1_pos + roll_sum - 1) % 10 + 1
            new_score = p1_score + new_pos
            p1_w, p2_w = count_wins(new_pos, new_score, p2_pos, p2_score, False)
            total_p1_wins += p1_w * freq
            total_p2_wins += p2_w * freq
    else:
        for roll_sum, freq in ROLL_DISTRIBUTION.items():
            new_pos = (p2_pos + roll_sum - 1) % 10 + 1
            new_score = p2_score + new_pos
            p1_w, p2_w = count_wins(p1_pos, p1_score, new_pos, new_score, True)
            total_p1_wins += p1_w * freq
            total_p2_wins += p2_w * freq

    return total_p1_wins, total_p2_wins
print(max(count_wins(p1, score1, p2, score2, True)))