with open('input.txt')as f:
    data = f.read()

x, y = 0, 0
seen = {(x, y)}
directions = {'>':(0, 1),'<':(0, -1),'v':(1, 0),'^':(-1, 0)}

for char in data:
    dx, dy = directions[char]
    x, y = x + dx, y + dy
    seen.add((x, y))

print(len(seen))