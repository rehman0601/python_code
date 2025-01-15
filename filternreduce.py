from functools import reduce

# List of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use filter to get only odd numbers (filter out even numbers)
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))

# Use reduce to sum the odd numbers
sum_of_odds = reduce(lambda x, y: x + y, odd_numbers)

print(f"Odd numbers: {odd_numbers}")
print(f"Sum of odd numbers: {sum_of_odds}")
