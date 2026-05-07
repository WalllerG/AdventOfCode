from collections import defaultdict, deque
with open('input.txt')as f:
    rules, text = f.read().split('\n\n')

rules = deque(rules.splitlines())
text = text.splitlines()
memo = defaultdict(set)
ans = 0

while rules:
    cur = rules.popleft()
    success = False
    id, combo = cur.split(': ')
    id = int(id)
    if 'a' in combo or 'b' in combo:
        memo[id].add(combo[1:-1])
        success = True
    else:
            if '|' in combo:
                combo = combo.split(' | ')
                possible = list(map(int, combo[0].split(' '))) + list(map(int, combo[1].split(' ')))
                if all(num in memo for num in possible) and len(possible) == 4:
                    success = True
                    for letter1 in memo[possible[0]]:
                        for letter2 in memo[possible[1]]:
                            memo[id].add(letter1 + letter2)
                    for letter1 in memo[possible[2]]:
                        for letter2 in memo[possible[3]]:
                            memo[id].add(letter1 + letter2)

                elif all(num in memo for num in possible) and len(possible) == 2:
                    success = True
                    for letter1 in memo[possible[0]]:
                        memo[id].add(letter1)
                    for letter1 in memo[possible[1]]:
                        memo[id].add(letter1)

            else:
                possible = list(map(int, combo.split(' ')))
                if all(num in memo for num in possible) and len(possible) == 2:
                    success = True
                    for letter1 in memo[possible[0]]:
                        for letter2 in memo[possible[1]]:
                            memo[id].add(letter1 + letter2)

                elif all(num in memo for num in possible) and len(possible) == 1:
                    success = True
                    memo[id] = memo[possible[0]]
    if not success:
        rules.append(cur)

for message in text:
    if message in memo[0]:
        ans += 1

print(ans)
