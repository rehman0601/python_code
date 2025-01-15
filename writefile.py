def write_to_file(file_path, text):
    try:
        with open(file_path, 'w') as file:
            file.write(text)
        print(f"Text written to {file_path}")
    except Exception as e:
        print(f"Error: {e}")

# Test the function
file_path = input("Enter the file path to write: ")
text = input("Enter the text to write to the file: ")
write_to_file(file_path, text)
