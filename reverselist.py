numbers = [10, 20, 30, 40, 50]

# Reverse the list in-place
for i in range(len(numbers) // 2):
    numbers[i], numbers[len(numbers) - 1 - i] = numbers[len(numbers) - 1 - i], numbers[i]

print("Reversed list:", numbers)
