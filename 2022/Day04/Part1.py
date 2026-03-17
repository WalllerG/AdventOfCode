with open("input.txt") as f:
    data = f.read()
ans = 0
def fully_contain(a, b):
    if b[0] >= a[0] and b[1] <= a[1]:
        return True
    elif a[0] >= b[0] and a[1] <= b[1]:
        return True
    return False
for line in data.split("\n"):
    s1,s2 = line.split(",")
    a = [int (x) for x in s1.split("-")]
    b = [int (x) for x in s2.split("-")]
    if fully_contain(a,b):
        ans += 1
print(ans)
