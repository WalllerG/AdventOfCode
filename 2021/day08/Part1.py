with open("input.txt") as f:
    data = f.read().split("\n")
ans = 0
special = {2,3,4,7}
for line in data:
    _, output = line.split(" | ")
    outputs = output.split(" ")
    for out in outputs:
        if len(out) in special:
            ans += 1
print(ans)