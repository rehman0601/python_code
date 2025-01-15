def is_palindrome(s):
    s = s.lower().replace(" ", "")  # Ignore case and spaces
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])

# Test the function
string = input("Enter a string to check if it's a palindrome: ")
print(f"Is the string a palindrome? {is_palindrome(string)}")
