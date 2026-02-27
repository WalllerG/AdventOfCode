from Util.util import read_input

data = read_input(7,True)

numsMap = {}

for line in data:
    target = int (line.split(":")[0])
    nums_str = line.split(":")[1]
    nums = [int(x) for x in nums_str.split()]
    numsMap[target] = nums

def backTrack(entry: tuple, count: int, current: int) -> bool:

    key, value = entry
    if count == len(value):
        return current == key

    next_num = value[count]
    if backTrack(entry, count + 1, current * next_num):
        return True
    if backTrack(entry, count + 1, current + next_num):
        return True

    return False


entries = list(numsMap.items())
result = 0
for entry in entries:
    if backTrack(entry, 1, entry[1][0]):
        result += entry[0]


print(result)

