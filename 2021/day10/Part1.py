with open("input.txt") as f:
    data = f.read().split("\n")
ans = 0
matches = {
    "{":"}",
    "(":")",
    "[":"]",
    "<":">"
}
scores = {
    "}":1197,
    ")":3,
    "]":57,
    ">":25137
}
def is_closed(s):
    queue = []
    for char in s:
        if char in "{[(<":
            queue.append(char)
        else:
            to_match = queue.pop()
            if char != matches[to_match]:
                return char
    return None
for line in data:
    c = is_closed(line)
    if c is not None:
        ans += scores[c]
print(ans)