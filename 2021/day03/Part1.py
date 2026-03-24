with open("input.txt") as f:
    data = list(f.read().split("\n"))
most = ""
least = ""
count = 0
while count < len(data[0]):
    z = 0
    o = 0
    for num in data:
        if int(num[count]) == 1:
            o += 1
        else:
            z += 1
    if o > z:
        most += "1"
        least += "0"
    else:
        most += "0"
        least += "1"
    count += 1
print(int(most, 2) * int(least, 2))
