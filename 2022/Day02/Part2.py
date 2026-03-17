with open("input.txt") as f:
    data = f.read()
ans = 0
def rock_paper_scissors(l,r):
    if l == "A":
        if r == "X":
            return 3
        elif r == "Y":
            return 4
        elif r == "Z":
            return 8
    elif l == "B":
        if r == "X":
            return 1
        elif r == "Y":
            return 5
        elif r == "Z":
            return 9
    elif l == "C":
        if r == "X":
            return 2
        elif r == "Y":
            return 6
        elif r == "Z":
            return 7
    return -1
for line in data.split("\n"):
    line = line.split(" ")
    ans +=  rock_paper_scissors(line[0], line[1])
print(ans)