def string_to_int(s):
    try:
        result = int(s)
        print(f"Converted integer: {result}")
    except ValueError:
        print("Error: The provided string could not be converted to an integer.")

# Test the function
string = input("Enter a string to convert to an integer: ")
string_to_int(string)
