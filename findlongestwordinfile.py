def find_longest_word(file_path):
    try:
        with open(file_path, 'r') as file:
            words = file.read().split()
        longest_word = max(words, key=len)
        print(f"The longest word in the file is: {longest_word}")
    except FileNotFoundError:
        print(f"Error: The file {file_path} does not exist.")
    except IOError as e:
        print(f"Error: An IO error occurred. {e}")

# Test the function
file_path = input("Enter the file path to find the longest word: ")
find_longest_word(file_path)
