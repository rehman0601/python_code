import random

def random_select(lst):
    return random.choice(lst)

# Test the function
items = ["apple", "banana", "cherry", "date"]
selected_item = random_select(items)
print(f"Randomly selected item: {selected_item}")
