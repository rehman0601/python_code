import statistics

# List of numbers
numbers = [1, 2, 3, 4, 4, 5, 5, 5, 6, 7]

# Compute mean, median, and mode
mean = statistics.mean(numbers)
median = statistics.median(numbers)
mode = statistics.mode(numbers)

# Output results
print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Mode: {mode}")
