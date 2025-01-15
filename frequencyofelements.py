lst = list(map(int, input("Enter a list of numbers separated by space: ").split()))
freq_dict = {}

for num in lst:
    freq_dict[num] = freq_dict.get(num, 0) + 1

print("Frequency of elements:", freq_dict)
