import os


def read_input(day: int, test: bool = False) -> list[str]:
    file_name = "input.txt" if test else "test.txt"
    file_path = os.path.join("/Users/walter/Desktop/AdventOfCode/2024/", f"Day{day}", file_name)

    try:
        with open(file_path, 'r') as file:
            return file.read().splitlines()
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return []