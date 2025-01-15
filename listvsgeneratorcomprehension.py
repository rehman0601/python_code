import time

# List comprehension (creates a list in memory)
start_time = time.time()
list_comprehension = [x * 2 for x in range(1, 10000001)]
list_time = time.time() - start_time

# Generator expression (creates an iterator, not a list)
start_time = time.time()
generator_expression = (x * 2 for x in range(1, 10000001))
gen_time = time.time() - start_time

print(f"List comprehension took: {list_time:.6f} seconds")
print(f"Generator expression took: {gen_time:.6f} seconds")
