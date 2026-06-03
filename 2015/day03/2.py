with open('input.txt')as f:
    data = list(f.read())

ax, ay = 0, 0
bx, by = 0, 0
seen = {(ax, ay)}
directions = {'>':(0, 1),'<':(0, -1),'v':(1, 0),'^':(-1, 0)}

for i in range(0, len(data)-1, 2):
    adx, ady = directions[data[i]]
    bdx, bdy = directions[data[i+1]]
    ax, ay = ax + adx, ay + ady
    bx, by = bx + bdx, by + bdy
    seen.add((ax, ay))
    seen.add((bx, by))

print(len(seen))