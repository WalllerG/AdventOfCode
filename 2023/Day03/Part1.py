from Util.util import read_input
data = read_input(3,True)

symbol = []
nums = []
ans = 0

for i in range(len(data)):
    line = list(data[i])
    num = ""
    coors = []
    is_next = False
    for j in range(len(line)):
        if line[j].isdigit():
            is_next = True
            num += line[j]
            coors.append((i, j))
        elif not line[j].isdigit() and line[j] != ".":
            symbol.append((i,j))
            if is_next:
                nums.append((num, coors))
                is_next = False
            num = ""
            coors = []
        elif line[j] == ".":
            if is_next:
                nums.append((num, coors))
                is_next = False
            num = ""
            coors = []
    if is_next:
        nums.append((num, coors))


n = False
for num, coors in nums:
    for coor in coors:
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)]:
            nx, ny = coor[0] + dx, coor[1] + dy
            if 0 <= nx < len(data) and 0 <= ny < len(data[0]) and (nx, ny) in symbol:
                ans += int(num)
                n = True
                print(num)
                break
        if n:
            n = False
            break

print(ans)




