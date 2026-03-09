from Util.util import read_input
data = read_input(True)

ans = 0
for line in data:
    nums = line.split(":")[-1]
    win_nums, num_to_match = nums.strip().split("|")
    wns = [int(x) for x in win_nums.split()]
    to_match = [int(y) for y in num_to_match.split()]
    count = 0
    for wn in wns:
        if wn in to_match:
            if count == 0:
                count += 1
            else:
                count *= 2
    ans += count

print(ans)