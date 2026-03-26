with open("input.txt") as f:
    data = f.read().split("\n")
ans = []
matches = {
    "{":"}",
    "(":")",
    "[":"]",
    "<":">"
}
scores = {
    "}":3,
    ")":1,
    "]":2,
    ">":4
}
def is_closed(s):
    queue = []
    incomplete = ""
    for char in s:
        if char in "{[(<":
            queue.append(char)
        else:
            to_match = queue.pop()
            if char != matches[to_match]:
                return -1
    while queue:
        add = queue.pop()
        incomplete += matches[add]
    return incomplete
for line in data:
    ch = is_closed(line)
    if ch != -1:
        re = 0
        for c in ch:
            re = re * 5 + scores[c]
        ans.append(re)
ans = sorted(ans)
print(ans[(len(ans) - 1) // 2])