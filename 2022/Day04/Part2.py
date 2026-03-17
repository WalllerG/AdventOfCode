with open("input.txt") as f:
    data = f.read()
ans = 0
def is_overlap(a, b):
    if a[0] > b[1] or b[0] > a[1]:
        return False
    return True
for line in data.split("\n"):
    s1,s2 = line.split(",")
    a = [int (x) for x in s1.split("-")]
    b = [int (x) for x in s2.split("-")]
    if is_overlap(a,b):
        ans += 1
print(ans)
