class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):
    def speak(self):
        print("Woof!")

# Create an instance of Dog and call speak
dog = Dog()
dog.speak()
