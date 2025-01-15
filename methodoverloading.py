class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):
    def speak(self):
        print("Woof!")

# Create instances of Animal and Dog and call speak
animal = Animal()
dog = Dog()

animal.speak()  # Outputs "Animal makes a sound"
dog.speak()     # Outputs "Woof!"
