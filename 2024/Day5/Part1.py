from Util.util import read_input
data = read_input(5,False)
index = 0
IntMap = {}
while data[index] != "":
    line = data[index]
    pair = line.split("|")
    IntMap[pair[0]] = int(pair[1])
    index += 1
print(IntMap)
