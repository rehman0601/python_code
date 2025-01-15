text = input("Enter text to write to the file: ")
file_path = input("Enter the name of the file to write to: ")

with open(file_path, 'w') as file:
    file.write(text)

print(f"Text written to {file_path}")
