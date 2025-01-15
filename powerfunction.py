def power(base, exp):
    if exp == 0:
        return 1
    else:
        return base * power(base, exp - 1)

# Test the power function
base = int(input("Enter the base: "))
exp = int(input("Enter the exponent: "))
print(f"{base}^{exp} = {power(base, exp)}")
