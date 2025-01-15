def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

# Test the function
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
print(f"GCD of {a} and {b} is {gcd(a, b)}")
