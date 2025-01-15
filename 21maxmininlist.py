numbers = [10, 20, 5, 40, 30]

# Find minimum
min_value = numbers[0]
for num in numbers:
    if num < min_value:
        min_value = num

# Find maximum
max_value = numbers[0]
for num in numbers:
    if num > max_value:
        max_value = num

print(f"Minimum value: {min_value}")
print(f"Maximum value: {max_value}")
