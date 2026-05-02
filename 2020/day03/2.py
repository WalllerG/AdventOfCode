with open('input.txt')as f:
    grid = f.read().splitlines()

slopes = [(1,1),(3,1),(5,1),(7,1),(1,2)]
total = 1

def get_trees(right, down):
    x = 0
    y = 0
    ans = 0
    wrap = len(grid[0])
    while y < len(grid)-1:
        x = (x + right) % wrap
        y += down
        if grid[y][x] == '#':
            ans += 1
    return ans

for right, down in slopes:
    total *= get_trees(right, down)
    
print(total)