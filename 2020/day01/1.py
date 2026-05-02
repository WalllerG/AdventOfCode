with open('input.txt')as f:
    data = set(int(line) for line in f.read().splitlines())

for n1 in data:
    for n2 in data:
        if n1 != n2 and n1 + n2 == 2020:
            print(n1 * n2)
            exit(0)