import functools
import sys
from Util.util import read_input
data = read_input(True)
grid = [list(line) for line in data]
start = (0,1)
end = (len(grid)-1, len(grid[0])-2)
dir_map = {
    ">": (0,1),
    "<": (0,-1),
    "v": (1, 0),
    "^": (-1, 0),
}
sys.setrecursionlimit(5000)
@functools.lru_cache()
def solve():
    max_step = 0
    seen = set()
    def dfs(cur, c_step):
        (x, y), step = cur, c_step
        nonlocal max_step
        if cur == end:
            max_step = max(max_step, step)
            return
        seen.add(cur)
        if grid[x][y] in "<>v^":
            nx, ny = x + dir_map[grid[x][y]][0], y + dir_map[grid[x][y]][1]
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] != "#":
                if (nx, ny) not in seen:
                    dfs((nx, ny), step+1)
            seen.remove(cur)
        else:
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] != "#":
                    if (nx, ny) not in seen:
                        dfs((nx, ny), step+1)
            seen.remove(cur)

    dfs(start, 0)
    return max_step
print(solve())







