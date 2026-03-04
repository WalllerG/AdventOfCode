from Util.util import read_input

data = read_input(15,True)
walls = set()
boxes = set()
moves = []
position = ()
result = 0

count = 0
for i in range(len(data)):
    lst = list(data[i])
    if len(lst) == 0:
        break
    for j in range(len(lst)):
        if lst[j] == "#":
            walls.add((i,j))
        elif lst[j] == "O":
            boxes.add((i,j))
        elif lst[j] == "@":
            position = (i,j)
    count += 1

for i in range(count+1, len(data)):
    lst = list(data[i])
    for j in range(len(lst)):
        moves.append(lst[j])

for move in moves:
    if move == '<':
        np = (position[0],position[1]-1)
        if np in walls:
            continue
        elif np in boxes:
            count = 1
            while True:
                npb = (np[0],np[1]-count)
                if npb in walls:
                    count = 0
                    break
                elif npb in boxes:
                    count += 1
                else:
                    break
            if count > 0:
                boxes.remove(np)
                boxes.add((npb[0],npb[1]))
                position = np
        else:
            position = np

    elif move == '>':
        np = (position[0],position[1]+1)
        if np in walls:
            continue
        elif np in boxes:
            count = 1
            while True:
                npb = (np[0],np[1]+count)
                if npb in walls:
                    count = 0
                    break
                elif npb in boxes:
                    count += 1
                else:
                    break
            if count > 0:
                boxes.remove(np)
                boxes.add((npb[0],npb[1]))
                position = np
        else:
            position = np

    elif move == 'v':
        np = (position[0]+1,position[1])
        if np in walls:
            continue
        elif np in boxes:
            count = 1
            while True:
                npb = (np[0]+count,np[1])
                if npb in walls:
                    count = 0
                    break
                elif npb in boxes:
                    count += 1
                else:
                    break
            if count > 0:
                boxes.remove(np)
                boxes.add((npb[0],npb[1]))
                position = np
        else:
            position = np

    elif move == '^':
        np = (position[0]-1,position[1])
        if np in walls:
            continue
        elif np in boxes:
            count = 1
            while True:
                npb = (np[0]-count,np[1])
                if npb in walls:
                    count = 0
                    break
                elif npb in boxes:
                    count += 1
                else:
                    break
            if count > 0:
                boxes.remove(np)
                boxes.add((npb[0],npb[1]))
                position = np
        else:
            position = np

for box in boxes:
    result += 100 * box[0] + box[1]

print(result)