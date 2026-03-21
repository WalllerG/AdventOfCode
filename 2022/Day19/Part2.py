import re
def solve():
    with open("input.txt") as f:
        data = f.readlines()
    ans = 1
    for line in data[0:3]:
        nums = list(map(int, re.findall(r"\d+", line)))
        costs = nums[1:]

        global_max = 0
        memo = {}

        max_ore = max(costs[0], costs[1], costs[2], costs[4])
        max_clay = costs[3]
        max_obs = costs[5]

        def dfs(t, o, c, ob, g, b1, b2, b3, b4):
            nonlocal global_max

            if t == 0:
                global_max = max(global_max, g)
                return g

            potential_max = g + (b4 * t) + (t * (t - 1) // 2)
            if potential_max <= global_max:
                return 0

            o = min(o, t * max_ore - b1 * (t - 1))
            c = min(c, t * max_clay - b2 * (t - 1))
            ob = min(ob, t * max_obs - b3 * (t - 1))
            state = (t, o, c, ob, b1, b2, b3, b4)
            if state in memo:
                return memo[state]
            res = 0
            if o >= costs[4] and ob >= costs[5]:
                res = dfs(t - 1, o - costs[4] + b1, c + b2, ob - costs[5] + b3, g + b4, b1, b2, b3, b4 + 1)
            else:
                if o >= costs[2] and c >= costs[3] and b3 < max_obs:
                    res = max(res,
                              dfs(t - 1, o - costs[2] + b1, c - costs[3] + b2, ob + b3, g + b4, b1, b2, b3 + 1, b4))
                if o >= costs[1] and b2 < max_clay:
                    res = max(res, dfs(t - 1, o - costs[1] + b1, c + b2, ob + b3, g + b4, b1, b2 + 1, b3, b4))
                if o >= costs[0] and b1 < max_ore:
                    res = max(res, dfs(t - 1, o - costs[0] + b1, c + b2, ob + b3, g + b4, b1 + 1, b2, b3, b4))
                res = max(res, dfs(t - 1, o + b1, c + b2, ob + b3, g + b4, b1, b2, b3, b4))

            memo[state] = res
            return res
        score = dfs(32, 0, 0, 0, 0, 1, 0, 0, 0)
        ans *= score
    print(ans)
solve()