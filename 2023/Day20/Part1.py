from collections import defaultdict
from Util.util import read_input
data = read_input(True)
modulos = {}
flip_flops = {}
inputs = defaultdict(list)
conjunction_memo ={}

for line in data:
    p1,target = line.split(" -> ")
    if p1.startswith("b"):
        targets = list(target.split(", "))
        modulos[p1] = ("b", targets)
        for target in targets:
            inputs[target].append(p1)
    else:
        kind, name = p1[0], p1[1:]
        if kind == "%":
            flip_flops[name] = False
        targets = list(target.split(", "))
        modulos[name] = (kind, targets)
        for target in targets:
            inputs[target].append(name)

for n, mo in modulos.items():
    con_dict = {}
    if mo[0] == "&":
        for inp in inputs[n]:
            con_dict[inp] = False
        conjunction_memo[n] = con_dict

low_pulse = 0
high_pulse = 0
for i in range(1000):
    queue = [("broadcaster", 0)]
    while queue:
        cur_mod, pulse = queue.pop(0)
        if pulse == 0:
            low_pulse += 1
        if pulse == 1:
            high_pulse += 1

        if cur_mod == "rx":
            continue
        type, targets = modulos[cur_mod][0], modulos[cur_mod][1]
        if type == "b":
            for target in targets:
                queue.append((target, 0))
        if type == "%":
            if pulse == 0:
                for target in targets:
                    if target != "rx":
                        if modulos[target][0] == "&":
                            conjunction_memo[target][cur_mod] = not conjunction_memo[target][cur_mod]
                    if not flip_flops[cur_mod]:
                        queue.append((target, 1))
                    elif flip_flops[cur_mod]:
                        queue.append((target, 0))
                flip_flops[cur_mod] = not flip_flops[cur_mod]
            elif pulse == 1:
                continue

        if type == "&":
            if set(conjunction_memo[cur_mod].values()) != {True}:
                for target in targets:
                    if target != "rx":
                        if modulos[target][0] == "&":
                            if not conjunction_memo[target][cur_mod]:
                                conjunction_memo[target][cur_mod] = True
                    queue.append((target, 1))
            else:
                for target in targets:
                    if target != "rx":
                        if modulos[target][0] == "&":
                            if conjunction_memo[target][cur_mod]:
                                conjunction_memo[target][cur_mod] = False
                    queue.append((target, 0))


print(low_pulse * high_pulse)


