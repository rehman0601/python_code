def recursive_sum(lst):
    if not lst:
        return 0
    return lst[0] + recursive_sum(lst[1:])

lst = list(map(int, input("Enter a list of numbers separated by space: ").split()))
print(f"Sum of the list is: {recursive_sum(lst)}")
