file_path = input("Enter the path of the text file: ")

try:
    with open(file_path, 'r') as file:
        lines = file.readlines()
    print(f"The file contains {len(lines)} lines.")
except FileNotFoundError:
    print(f"The file at {file_path} does not exist.")
