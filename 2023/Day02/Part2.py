from Util.util import read_input
data = read_input(2,True)

ans = 0

for line in data:
    is_possible = True
    Id, parts = line.split(": ")
    part = parts.split("; ")
    r_large = float("-inf")
    b_large = float("-inf")
    g_large = float("-inf")
    for p in part:
        nums = p.split(", ")
        for num in nums:
            s = num.split(" ")
            if s[1] == "red":
                if int(s[0]) > r_large:
                    r_large = int(s[0])
            elif s[1] == "green":
                if int(s[0]) > g_large:
                    g_large = int(s[0])
            elif s[1] == "blue":
                if int(s[0]) > b_large:
                    b_large = int(s[0])
    ans += (r_large * b_large * g_large)

print(ans)