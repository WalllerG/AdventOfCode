
from Util.util import read_input

data = read_input(23,True)

cache = {}
for line in data:
    l, r = line.split("-")
    if l not in cache and r not in cache:
        cache[l] = [r]
        cache[r] = [l]
    elif l not in cache and r in cache:
        cache[l] = [r]
        cache[r].append(l)
    elif r not in cache and l in cache:
        cache[l].append(r)
        cache[r] = [l]
    else:
        cache[l].append(r)
        cache[r].append(l)


LAN = set()
for comp in cache.keys():
    connected = cache[comp]
    for con in connected:
        sub_con = cache[con]
        for sub in sub_con:
            t = (comp, con, sub)
            is_in = False
            if comp in cache[sub]:
                if len(LAN) == 0:
                    LAN.add(t)
                else:
                    for l in LAN:
                        if set(t) == set(l):
                            is_in = True
                            break
                    if not is_in:
                        LAN.add(t)

ans = 0
for t in LAN:
    for c in t:
        if c.startswith("t"):
            ans += 1
            break
print(ans)








