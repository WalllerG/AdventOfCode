from Util.util import read_input

data = read_input(25, True)
ans = 0
locks = []
keys = []

for i in range(0, len(data)-6, 8):
    a = data[i]
    b = data[i+1]
    c = data[i+2]
    d = data[i+3]
    e = data[i+4]
    f = data[i+5]
    g = data[i+6]
    val = [0,0,0,0,0]
    if a[0] == "#":
        lst = list(b)
        for j in range(len(lst)):
            if lst[j] == "#":
                val[j] += 1
        lst = list(c)
        for j in range(len(lst)):
            if lst[j] == "#":
                val[j] += 1
        lst = list(d)
        for j in range(len(lst)):
            if lst[j] == "#":
                val[j] += 1
        lst = list(e)
        for j in range(len(lst)):
            if lst[j] == "#":
                val[j] += 1
        lst = list(f)
        for j in range(len(lst)):
            if lst[j] == "#":
                val[j] += 1
        lst = list(g)
        for j in range(len(lst)):
            if lst[j] == "#":
                val[j] += 1

        locks.append(val)


    elif a[0] == ".":

        lst = list(f)
        for j in range(len(lst)):
            if lst[j] == "#":
                val[j] += 1
        lst = list(e)
        for j in range(len(lst)):
            if lst[j] == "#":
                val[j] += 1
        lst = list(d)
        for j in range(len(lst)):
            if lst[j] == "#":
                val[j] += 1
        lst = list(c)
        for j in range(len(lst)):
            if lst[j] == "#":
                val[j] += 1
        lst = list(b)
        for j in range(len(lst)):
            if lst[j] == "#":
                val[j] += 1

        keys.append(val)

for lock in locks:
    for key in keys:
        unlock = [x + y for x, y in zip(lock, key)]
        if any(num > 5 for num in unlock):
            continue
        else:
            ans += 1
print(ans)

