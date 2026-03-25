with open("input.txt") as f:
    data = list(map(int, f.read().split(",")))
def solve(days, fishes):
    for i in range(days):
        for j in range(len(fishes)):
            new_timer = fishes[j] - 1
            if new_timer < 0:
                fishes[j] = 6
                fishes.append(8)
            else:
                fishes[j] = new_timer
    return len(fishes)
print(solve(80, data))