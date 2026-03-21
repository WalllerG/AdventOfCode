with open("input.txt") as f:
    data = list(map(int, f.read().splitlines()))
for i in range(len(data)):
    data[i] *= 811589153
ans = 0
indexed_data = list(enumerate(data))
working_list = list(indexed_data)
n = len(data)
for i in range(10):
    for item in indexed_data:
        val = item[1]
        if val == 0:
            continue
        old_idx = working_list.index(item)
        working_list.pop(old_idx)
        new_idx = (old_idx + val) % (n - 1)
        working_list.insert(new_idx, item)
final_values = [x[1] for x in working_list]
zero_idx = final_values.index(0)
ans = sum(final_values[(zero_idx + i) % n] for i in [1000, 2000, 3000])
print(ans)