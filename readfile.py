def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        print(content)
    except FileNotFoundError:
        print(f"Error: The file {file_path} does not exist.")

# Test the function
file_path = input("Enter the file path to read: ")
read_file(file_path)