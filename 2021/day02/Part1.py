with open("input.txt") as f:
    data = f.read().split("\n")
x, y = 0, 0
for line in data:
    op, num = line.split(" ")
    if op == "forward": x += int(num)
    elif op == "up": y -= int(num)
    elif op == "down": y += int(num)
print(x * y)