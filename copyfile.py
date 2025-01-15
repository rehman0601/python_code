def copy_file(source_path, destination_path):
    try:
        with open(source_path, 'r') as source_file:
            content = source_file.read()
        with open(destination_path, 'w') as dest_file:
            dest_file.write(content)
        print(f"Copied content from {source_path} to {destination_path}")
    except FileNotFoundError:
        print(f"Error: The file {source_path} does not exist.")

# Test the function
source_path = input("Enter the source file path: ")
destination_path = input("Enter the destination file path: ")
copy_file(source_path, destination_path)
