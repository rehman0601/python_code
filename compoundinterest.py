principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual interest rate (in %): "))
time = float(input("Enter the time period (in years): "))
compound_frequency = int(input("Enter the number of times interest is compounded per year: "))

amount = principal * (1 + rate / (compound_frequency * 100))**(compound_frequency * time)
compound_interest = amount - principal

print(f"Compound Interest: {compound_interest:.2f}")
