def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Test the recursive factorial function
n = int(input("Enter a number to compute its factorial: "))
print(f"Factorial of {n} is {factorial(n)}")
