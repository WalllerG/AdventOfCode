import re
with open('input.txt')as f:
    data = f.read().splitlines()

ans = 0

def evaluate(tokens):
    if isinstance(tokens, list):
        tokens = iter(tokens)
    
    values = []
    ops = []

    for token in tokens:
        if token == '(':
            values.append(evaluate(tokens))
        elif token == ')':
            break
        elif token in '+*':
            ops.append(token)
        else:
            values.append(int(token))

        if len(values) == 2:
            a = values.pop(0)
            b = values.pop(0)
            op = ops.pop(0)
            if op == '+':
                values.append(a + b)
            else:
                values.append(a * b)
                
    return values[0]

for line in data:
    tokens = re.findall(r'\d+|[+*()]', line)
    ans += evaluate(tokens)

print(ans)