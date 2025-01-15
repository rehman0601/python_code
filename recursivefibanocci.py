def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)

# Test the recursive Fibonacci function
n = int(input("Enter the Fibonacci number to calculate: "))
print(f"The {n}-th Fibonacci number is {fib(n)}")
