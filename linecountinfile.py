def count_lines_in_file(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
        print(f"Number of lines in the file: {len(lines)}")
    except FileNotFoundError:
        print(f"Error: The file {file_path} does not exist.")

# Test the function
file_path = input("Enter the file path to count lines: ")
count_lines_in_file(file_path)
