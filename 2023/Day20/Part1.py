from Util.util import read_input
data = read_input(False)
modulos = {}
flip_flops = {}
inputs = {}
for line in data:
    p1,target = line.split(" -> ")
    if p1.startswith("b"):
        targets = list(target.split(", "))
        modulos[p1] = ("b", targets)
        for target in targets:
            inputs[target] = p1
    else:
        kind, name = p1[0], p1[1:]
        if kind == "%":
            flip_flops[name] = False
        targets = list(target.split(", "))
        modulos[name] = (kind, targets)
        for target in targets:
            inputs[target] = name

low_pulse = 0
high_pulse = 0
for i in range(1):
    low_pulse += 1
    queue = [("broadcaster", 0)]
    while queue:
        cur_mod, pulse = queue.pop(0)
        if cur_mod == "output":
            if pulse == 0:
                low_pulse += 1
            else:
                high_pulse += 1
            continue
        type, targets = modulos[cur_mod][0], modulos[cur_mod][1]
        if type == "b":
            for target in targets:
                queue.append((target, 0))
                low_pulse += 1
        if type == "%":
            for target in targets:
                if pulse == 0 and not flip_flops[cur_mod]:
                    flip_flops[cur_mod] = not flip_flops[cur_mod]
                    queue.append((target, 1))
                    high_pulse += 1
                elif pulse == 0 and flip_flops[cur_mod]:
                    flip_flops[cur_mod] = not flip_flops[cur_mod]
                    queue.append((target, 0))
                    low_pulse += 1
                elif pulse == 1:
                    continue
        if type == "&":
            for target in targets:
                if pulse == 0:
                    queue.append((target, 1))
                    high_pulse += 1
                else:
                    queue.append((target, 0))
                    low_pulse += 1

print(low_pulse , high_pulse)


