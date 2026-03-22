with open("input.txt") as f:
    data = f.read().split("\n")
ans = 0
SNAFU = {
    2:"2",
    1:"1",
    0:"0",
    -1:"-",
    -2:"="
}
def convert(n, ind):
    if n == "2":
        return 2 * 5 ** ind
    elif n == "1":
        return 5 ** ind
    elif n == "0":
        return 0
    elif n == "=":
        return -2 * 5 ** ind
    else:
        return -1 * 5 ** ind

def convert_back(decimal):
    to_do = []
    cur = decimal
    while cur > 0:
        to_convert = cur % 5
        if to_convert > 2:
            to_convert = cur % -5
            cur = -(cur // -5)
            to_do.insert(0, SNAFU[to_convert])
            continue
        else:
            cur = cur // 5
            to_do.insert(0, SNAFU[to_convert])
    print("".join(to_do))

for line in data:
    num = 0
    for index, char in enumerate(line):
        num += convert(char,(len(line)-1)-index)
    ans += num

convert_back(ans)


