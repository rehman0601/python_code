source_file = input("Enter the source file path: ")
destination_file = input("Enter the destination file path: ")

try:
    with open(source_file, 'r') as src:
        content = src.read()
    with open(destination_file, 'w') as dest:
        dest.write(content)
    print(f"Content copied from {source_file} to {destination_file}")
except FileNotFoundError:
    print(f"One of the files could not be found.")
