import time

# Define the decorator function
def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time of {func.__name__}: {end_time - start_time:.6f} seconds")
        return result
    return wrapper

# Use the decorator
@timer
def long_running_function():
    time.sleep(2)  # Simulate a function that takes 2 seconds to run

# Call the decorated function
long_running_function()
