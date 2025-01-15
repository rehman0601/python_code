def search_in_file(file_path, search_term):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
        
        found = False
        for i, line in enumerate(lines, 1):
            if search_term in line:
                print(f"Line {i}: {line.strip()}")
                found = True
        
        if not found:
            print(f"The term '{search_term}' was not found in the file.")
    except FileNotFoundError:
        print(f"Error: The file {file_path} does not exist.")
    except IOError as e:
        print(f"Error: An IO error occurred. {e}")

# Test the function
file_path = input("Enter the file path to search in: ")
search_term = input("Enter the substring to search for: ")
search_in_file(file_path, search_term)
