import re
with open("input.txt") as f:
    data = f.readlines()
ans = 0

def find_max(costs, time_limit):
    ore_c, clay_c, obs_ore_c, obs_clay_c, geo_ore_c, geo_obs_c = costs
    max_ore_needed = max(ore_c, clay_c, obs_ore_c, geo_ore_c)

    memo = {}
    def dfs(t, o, c, ob, g, b1, b2, b3, b4):
        if t == 0:
            return g
        state = (t, o, c, ob, b1, b2, b3, b4)
        if state in memo:
            return memo[state]
        if o >= geo_ore_c and ob >= geo_obs_c:
            res = dfs(t - 1, o - geo_ore_c + b1, c + b2, ob - geo_obs_c + b3, g + b4, b1, b2, b3, b4 + 1)
        else:
            choices = []
            if o >= obs_ore_c and c >= obs_clay_c and b3 < geo_obs_c:
                choices.append(dfs(t - 1, o - obs_ore_c + b1, c - obs_clay_c + b2, ob + b3, g + b4, b1, b2, b3 + 1, b4))
            if o >= clay_c and b2 < obs_clay_c:
                choices.append(dfs(t - 1, o - clay_c + b1, c + b2, ob + b3, g + b4, b1, b2 + 1, b3, b4))
            if o >= ore_c and b1 < max_ore_needed:
                choices.append(dfs(t - 1, o - ore_c + b1, c + b2, ob + b3, g + b4, b1 + 1, b2, b3, b4))
            choices.append(dfs(t - 1, o + b1, c + b2, ob + b3, g + b4, b1, b2, b3, b4))
            res = max(choices)
        memo[state] = res
        return res
    return dfs(time_limit, 0, 0, 0, 0, 1, 0, 0, 0)

for i, line in enumerate(data):
    nums = list(map(int, re.findall(r"\d+", line.split(": ")[-1])))
    ans += (i+1) * find_max(nums, 24)
print(ans)