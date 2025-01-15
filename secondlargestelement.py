numbers = list(map(int, input("Enter unique integers separated by space: ").split()))

# Find the second largest element
unique_numbers = list(set(numbers))  # Remove duplicates
unique_numbers.sort()

if len(unique_numbers) >= 2:
    print(f"The second largest element is: {unique_numbers[-2]}")
else:
    print("There is no second largest element.")
