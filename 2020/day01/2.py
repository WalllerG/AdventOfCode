with open('input.txt')as f:
    data = set(int(line) for line in f.read().splitlines())

for n1 in data:
    for n2 in data:
        for n3 in data:
            if n1 != n2 and n2 != n3 and n3 != n1 and n1 + n2 + n3 == 2020:
                print(n1 * n2 * n3)
                exit(0)