class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Create an instance and print attributes
person = Person("Alice", 30)
print(f"Name: {person.name}, Age: {person.age}")