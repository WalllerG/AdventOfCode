with open("input.txt") as file:
    data = file.read()

foods = set()
largest = float("-inf")
for line in data.split("\n\n"):
    total = 0
    for food in line.split():
        total += int(food)
    foods.add(total)

no1 = max(foods)
foods.remove(no1)
no2 = max(foods)
foods.remove(no2)
no3 = max(foods)
foods.remove(no3)
print(no1 + no2 + no3)


