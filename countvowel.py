def count_vowels(s):
    vowels = 'aeiou'
    if len(s) == 0:
        return 0
    return (1 if s[0].lower() in vowels else 0) + count_vowels(s[1:])

# Test the function
string = input("Enter a string: ")
print(f"Number of vowels in the string: {count_vowels(string)}")
