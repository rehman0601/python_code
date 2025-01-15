def append_to_file(file_path, text):
    try:
        with open(file_path, 'a') as file:
            file.write(text + '\n')
        print(f"Text appended to {file_path}")
    except IOError as e:
        print(f"Error: An IO error occurred. {e}")

# Test the function
file_path = input("Enter the file path to append to: ")
text = input("Enter the text to append: ")
append_to_file(file_path, text)
