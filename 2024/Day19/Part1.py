from Util.util import read_input

data = read_input(19, True)
ans = 0
color_stripes = data[0].split(", ")
towels = []

for i in range(2, len(data)):
    towels.append(data[i])

def is_possible (t):
    queue = [""]
    fail_state = set()
    while queue:
        current = queue.pop()
        if current == t:
            return True
        for color in color_stripes:
            next_state = current + color
            if next_state == t:
                return True
            if next_state not in queue and len(next_state) <= len(t) and next_state == t[:len(next_state)] and next_state not in fail_state:
                queue.append(next_state)
            else :
                fail_state.add(next_state)
    return False

for towel in towels:
    if is_possible(towel):
        ans += 1
print(ans)

