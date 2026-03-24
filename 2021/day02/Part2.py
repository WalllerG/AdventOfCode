with open("input.txt") as f:
    data = f.read().split("\n")
x, y, aim = 0, 0, 0
for line in data:
    op, num = line.split(" ")
    if op == "forward":
        x += int(num)
        y += aim * int(num)
    elif op == "up": aim -= int(num)
    elif op == "down": aim += int(num)
print(x * y)