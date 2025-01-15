def sum_list(lst):
    if not lst:
        return 0
    return lst[0] + sum_list(lst[1:])

# Test the recursive sum function
lst = list(map(int, input("Enter a list of numbers separated by space: ").split()))
print(f"Sum of the list is {sum_list(lst)}")
