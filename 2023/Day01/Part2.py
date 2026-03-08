from re import findall

from Util.util import read_input
data = read_input(1,True)

ans =0
def convert(s):
    if s == "one":
        return "1"
    elif s == "two":
        return "2"
    elif s == "three":
        return "3"
    elif s == "four":
        return "4"
    elif s == "five":
        return "5"
    elif s == "six":
        return "6"
    elif s == "seven":
        return "7"
    elif s == "eight":
        return "8"
    elif s == "nine":
        return "9"
    return None


for line in data:
    res = ""
    nums = findall(r"(?=(one|two|three|four|five|six|seven|eight|nine|\d))", line)
    if not nums[0].isdigit():
        res += convert(nums[0])
    else :
        res += nums[0]
    if not nums[-1].isdigit():
         res += convert(nums[-1])
    else:
        res += nums[-1]
    ans += int(res)
print(ans)

