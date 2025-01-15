def count_words_in_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        words = content.split()
        print(f"Number of words in the file: {len(words)}")
    except FileNotFoundError:
        print(f"Error: The file {file_path} does not exist.")

# Test the function
file_path = input("Enter the file path to count words: ")
count_words_in_file(file_path)
