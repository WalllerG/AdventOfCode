from Util.util import read_input

data = read_input(11, True)

num_of_Stones = data[0].split(" ")

def blinking (lst) -> list[str]:
    new_num_of_stones = []
    for stone in lst:
        if stone == "0":
            new_num_of_stones.append("1")
        elif len(stone) % 2 == 0:
            left = int(stone[:len(stone)//2])
            right = int(stone[len(stone)//2:])
            new_num_of_stones.append(str(left))
            new_num_of_stones.append(str(right))
        else:
            new_num = int (stone) * 2024
            new_num_of_stones.append(str(new_num))

    return new_num_of_stones

def recursion (count, num_of_stones, target) -> int:
    if count == target:
        return len(num_of_stones)
    else:
        new_num_of_stones = blinking(num_of_stones)
        return recursion(count + 1, new_num_of_stones, target)

print(recursion(0, num_of_Stones, 25))