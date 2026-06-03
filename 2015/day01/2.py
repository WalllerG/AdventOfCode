with open('input.txt')as f:
    data = f.read()

count = 0

for i, char in enumerate(data, start=1):
    if char == '(':
        count += 1
    else:
        count -= 1
    if count == -1:
        print(i)
        break
