import functools
with open("input.txt") as f:
    data = list(map(int, f.read().split(",")))
@functools.lru_cache()
def count(timer, days_left):
    if days_left <= timer:
        return 1
    remaining = days_left - timer - 1
    return count(6, remaining) + count(8, remaining)
print(sum(count(fish, 256) for fish in data))