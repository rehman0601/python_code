file_path = input("Enter the path of the text file to read: ")

try:
    with open(file_path, 'r') as file:
        contents = file.read()
        print(contents)
except FileNotFoundError:
    print(f"The file at {file_path} does not exist.")
