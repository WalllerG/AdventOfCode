from Util.util import read_input
data = read_input(1,True)

ans =0

for line in data:
    res = ""
    lst1 = list(line)
    lst2 = list(line)
    for i in range(len(lst1)):
        if lst1[i].isdigit():
            res += lst1[i]
            break
    for j in range(len(lst2)-1, -1, -1):
        if lst2[j].isdigit():
            res += (lst2[j])
            break
    ans += int(res)

print(ans)

