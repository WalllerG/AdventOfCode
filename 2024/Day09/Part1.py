from Util .util import read_input

data = read_input(9, True)
line = list(data[0])
disk = []
count = 0
result = 0

for i in range(len(line)):
    if i % 2 == 0:
        for j in range(int (line[i])):
            disk.append(str (count))
        count += 1
    else :
        for j in range(int (line[i])):
            disk.append(".")

def movedList (lst):
    try:
        first_dot = lst.index('.')
        remaining_part = lst[first_dot:]
        return all(item == '.' for item in remaining_part)

    except ValueError:
        return True

currentIndex = len(disk)-1

for i in range(len(disk)):
    if movedList (disk):
        break

    if disk[i] == ".":
        while disk[currentIndex] == ".":
            currentIndex -= 1
        disk[i] = disk[currentIndex]
        disk[currentIndex] = "."
        currentIndex -= 1

count1 = 0

while disk[count1] != ".":
    result += int(disk[count1]) * count1
    count1 += 1

print(result)