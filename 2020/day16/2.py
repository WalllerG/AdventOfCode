import re
from collections import defaultdict
with open('input.txt')as f:
    tickets, my_ticket, nearby_tickets = f.read().split('\n\n')
    
my_ticket = list(map(int, my_ticket.splitlines()[1].split(',')))
all_ranges = set()
cols = [[num] for num in my_ticket]
seen = set()
orders = {}
fields = {}
freq = defaultdict(list)
ans = 1

for line in tickets.splitlines():
    id = line.split(':')[0]
    ranges = set()
    a, b, c, d = list(map(int, re.findall(r'\d+', line)))
    ranges |= set(range(a, b+1))
    ranges |= set(range(c, d+1))
    all_ranges |= set(range(a, b+1))
    all_ranges |= set(range(c, d+1))
    fields[id] = ranges

for line in nearby_tickets.splitlines()[1:]:
    for index, num in enumerate(list(map(int, line.split(',')))):
        if num in all_ranges:
            cols[index].append(num)

for index, col in enumerate(cols):
    for id, field in fields.items():
        if all(num in field for num in col):
            freq[id].append(index)
            
while len(seen) != 20:
    for id, group in freq.items():
        group = set(group)
        if len(group ^ seen) == 1 and len(group) > len(seen):
            orders[id] = list(group ^ seen)[0]
            seen |= group
            
for id, index in orders.items():
    if id.startswith('departure '):
        ans *= my_ticket[index]
        
print(ans)