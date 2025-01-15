class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print(f"{self.name} makes a sound")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
    
    def speak(self):
        print(f"{self.name} says Woof!")

# Create an instance of Dog and call speak
dog = Dog("Rex", "Golden Retriever")
dog.speak()
