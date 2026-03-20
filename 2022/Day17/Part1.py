with open("input.txt") as f:
    data = f.read()

jets = [1 if x == ">" else -1 for x in data]
rocks_type = [
    [0,1,2,3],
    [1, 1j, 1 + 1j, 2 + 1j, 1 + 2j],
    [0, 1 ,2, 2+1j, 2+2j],
    [0, 1j, 2j, 3j],
    [0, 1, 1j, 1+1j]
]
solid = {x - 1j for x in range(7)}
height = 0
rc = 0
rock_index = 0
rock = {x + 2 + (height +3) * 1j for x in rocks_type[rock_index]}
while rc < 2022:
    for jet in jets:
        moved  = {x + jet for x in rock}
        if all(0 <= x.real < 7 for x in moved) and not (moved & solid):
            rock = moved
        moved = {x -1j for x in rock}
        if moved & solid:
            solid |= rock
            rc += 1
            height = max(x.imag for x in solid) + 1
            if rc >= 2022:
                break
            rock_index = (rock_index + 1) % 5
            rock = {x + 2 + (height + 3) * 1j for x in rocks_type[rock_index]}
        else:
            rock = moved
print(height)