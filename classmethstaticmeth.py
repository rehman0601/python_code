class Counter:
    count = 0

    @classmethod
    def increment(cls):
        cls.count += 1

    @staticmethod
    def display_message():
        print("This is a static method.")

# Test the class
Counter.increment()
Counter.increment()
print(f"Count: {Counter.count}")

Counter.display_message()
