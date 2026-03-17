with open("input.txt") as file:
    data = file.read()

largest = float("-inf")
for line in data.split("\n\n"):
    total = 0
    for food in line.split():
        total += int(food)
    if total > largest:
        largest = total
print(largest)


