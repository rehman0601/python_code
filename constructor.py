class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def display_details(self):
        print(f"Car Details: {self.year} {self.make} {self.model}")

# Create an instance and display its details
car = Car("Toyota", "Camry", 2022)
car.display_details()
