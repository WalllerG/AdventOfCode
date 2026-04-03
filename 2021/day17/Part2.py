import re
with open("input.txt") as f:
    x_min, x_max, y_min, y_max = map(int, re.findall(r"-?\d+", f.read()))
def simulate(vx, vy):
    curr_x, curr_y = 0, 0
    max_y_reached = 0
    while curr_x <= x_max and curr_y >= y_min:
        curr_x += vx
        curr_y += vy
        max_y_reached = max(max_y_reached, curr_y)
        if vx > 0:
            vx -= 1
        elif vx < 0:
            vx += 1
        vy -= 1
        if x_min <= curr_x <= x_max and y_min <= curr_y <= y_max:
            return True, max_y_reached
    return False, 0
highest_y = 0
hits = 0
for vx in range(1, x_max + 1):
    for vy in range(y_min, abs(y_min)):
        success, top = simulate(vx, vy)
        if success:
            highest_y = max(highest_y, top)
            hits += 1
print(hits)
