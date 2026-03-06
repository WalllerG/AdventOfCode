from Util .util import read_input

data = read_input(9, True)
line = list(data[0])
disk = []
count = 0
result = 0
hasMoved = []

for i in range(len(line)):
    lst = []
    if i % 2 == 0:
        for j in range(int (line[i])):
            lst.append(str (count))
        count += 1
        disk.append(lst)
    else :
        if int (line[i]) != 0:
            for j in range(int (line[i])):
                lst.append(".")
            disk.append(lst)


a = len(disk)-1
while disk[a][0] != "0":
    if set(disk[a]) != {"."}:
        if disk[a] not in hasMoved:
            for j in range(a):
                if set(disk[j]) == {"."} and len(disk[j]) == len (disk[a]):
                    hasMoved.append(disk[a])
                    temp = disk[j]
                    disk[j] = disk[a]
                    disk[a] = temp
                    break
                elif set(disk[j]) == {"."} and len(disk[j]) > len (disk[a]):
                    hasMoved.append(disk[a])
                    leftLst = disk[a]
                    rightLst = ["."] * (len (disk[j]) - len (disk[a]))
                    endLst = ["."] * len(disk[a])
                    disk[j] = leftLst
                    disk.insert(j+1, rightLst)
                    disk[a+1] = endLst
                    a += 1
                    break
    a -= 1

count = 0
for i in range(len(disk)):
    for j in range(len (disk[i])):
        if disk[i][j] != ".":
            result += count * int (disk[i][j])
        count += 1

print(result)








