class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        print(f"Hello, my name is {self.name}")

# Create an instance and call the greet method
person = Person("Alice", 30)
person.greet()
