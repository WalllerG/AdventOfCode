import re
with open('input.txt')as f:
    tickets, my_ticket, nearby_tickets = f.read().split('\n\n')
    
ranges = set()
ans = 0

for line in tickets.splitlines():
    a, b, c, d = list(map(int, re.findall(r'\d+', line)))
    ranges |= set(range(a, b+1))
    ranges |= set(range(c, d+1))
    
for line in nearby_tickets.splitlines()[1:]:
    for num in list(map(int, line.split(','))):
        if num not in ranges:
            ans += num
            
print(ans)