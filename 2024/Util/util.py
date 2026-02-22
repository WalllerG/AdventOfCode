import os
def read_input(day: int, test: bool = False) -> list[str]:
    file_name = "input.txt" if test else "test.txt"

    file_path = file_name

    try:
        with open(file_path, 'r') as file:
            return file.read().splitlines()
    except FileNotFoundError:
        # This helps you debug by showing exactly where Python is looking
        print(f"Error: The file {file_path} was not found in {os.getcwd()}")
        return []