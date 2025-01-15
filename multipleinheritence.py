class Animal:
    def speak(self):
        print("Animal makes a sound")

class Swimmer:
    def swim(self):
        print("Swimmer swims in water")

class Dolphin(Animal, Swimmer):
    def communicate(self):
        print("Dolphin communicates with clicks")

# Test the class
dolphin = Dolphin()
dolphin.speak()  # From Animal
dolphin.swim()   # From Swimmer
dolphin.communicate()  # Own method
