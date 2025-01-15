class Car:
    def __init__(self, make="Unknown", model="Unknown", year=2000):
        self.make = make
        self.model = model
        self.year = year
    
    def display_details(self):
        print(f"Car Details: {self.year} {self.make} {self.model}")

# Create instances with and without providing arguments
car1 = Car("Tesla", "Model S", 2022)
car2 = Car()

car1.display_details()
car2.display_details()
