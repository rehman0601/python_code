numbers = list(map(int, input("Enter unique integers separated by space: ").split()))

# Find the second largest element
def second_largest(arr):
    
    # Initialize two variables to store the largest and second largest elements
    largest = second_largest = int(arr[0])
    
    # Traverse through the list
    for num in arr:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest:
            second_largest = num
    
    return second_largest


unique_numbers = list(set(numbers))  # Remove duplicates
unique_numbers.sort()

if len(unique_numbers) >= 2:
    print(f"The second largest element is: {second_largest(unique_numbers)}")
else:
    print("There is no second largest element.")
