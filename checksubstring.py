s = input("Enter a string: ")
sub = input("Enter a substring to check: ")

if sub in s:
    print(f"The substring '{sub}' is present in the string.")
else:
    print(f"The substring '{sub}' is not present in the string.")
