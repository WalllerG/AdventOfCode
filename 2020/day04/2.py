import re
with open('input.txt')as f:
    data = f.read().split('\n\n')

validations = {'byr':range(1920, 2003),
               'iyr':range(2010, 2021),
               'eyr':range(2020, 2031),
               'hgt-cm':range(150, 194), 
               'hgt-in':range(59, 77),
               'ecl':{'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}}

def hcl(s):
    if len(s) != 7:
        return False
    if s[0] != '#':
        return False
    for char in s[1:]:
        if char not in '0123456789abcdef':
            return False
    return True

def pid(s):
    if len(s) != 9:
        return False
    return True

ans = 0
for person in data:
    valid = True
    count = 0
    for line in person.splitlines():
        for part in line.split(' '):
            name, info = part.split(':')
            if name in ['iyr','eyr','byr']:
                count += 1
                if int(info) not in validations[name]:
                    valid = False
                    break
            elif name == 'hgt':
                count += 1
                height = int(re.findall(r'\d+',info)[0])
                if 'cm' in info:
                    if height not in validations[name+'-cm']:
                        valid = False
                        break
                elif 'in' in info:
                    if height not in validations[name+'-in']:
                        valid = False
                        break
                elif 'in' not in info and 'cm' not in info:
                    valid = False
                    break
            elif name == 'hcl':
                count += 1
                if not hcl(info):
                    valid = False
                    break
            elif name == 'ecl':
                count += 1
                if info not in validations[name]:
                    valid = False
                    break
            elif name == 'pid':
                count += 1
                if not pid(info):
                    valid = False
                    break
        if not valid:
            break
    if valid and count == 7:
        ans += 1

print(ans)