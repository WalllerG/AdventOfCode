from Util.util import read_input

data = read_input(19, True)
ans = 0
color_stripes = data[0].split(", ")
towels = []
memo = {}

for i in range(2, len(data)):
    towels.append(data[i])

def count_ways(towel_suffix,s):
    if not towel_suffix:
        return 1

    if towel_suffix in memo:
        return memo[towel_suffix]

    total_ways = 0
    for stripe in s:
        if towel_suffix.startswith(stripe):
            total_ways += count_ways(towel_suffix[len(stripe):], s)

    memo[towel_suffix] = total_ways
    return total_ways


for towel in towels:
    ans += count_ways(towel, color_stripes)

print(ans)




