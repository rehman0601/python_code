number = input("Enter a number: ")

# Calculate the sum of digits
digit_sum = sum(int(digit) for digit in number if digit.isdigit())
print(f"The sum of the digits is: {digit_sum}")
