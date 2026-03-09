
from Util.util import read_input
data = read_input(True)

ans = 0
red_max = 12
green_max = 13
blue_max = 14
count = 1

for line in data:
    is_possible = True
    Id, parts = line.split(": ")
    part = parts.split("; ")
    for p in part:
        nums = p.split(", ")
        for num in nums:
            s = num.split(" ")
            if s[1] == "red":
                if int(s[0]) > red_max:
                    is_possible = False
                    break
            elif s[1] == "green":
                if int(s[0]) > green_max:
                    is_possible = False
                    break
            elif s[1] == "blue":
                if int(s[0]) > blue_max:
                    is_possible = False
                    break
    if is_possible:
        ans += count
    count += 1
print(ans)