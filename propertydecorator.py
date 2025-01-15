class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature cannot be below absolute zero!")
        self._celsius = value

# Test the class
temp = Temperature(25)
print(f"Temperature: {temp.celsius}°C")
temp.celsius = 30
print(f"Updated Temperature: {temp.celsius}°C")
# Uncommenting the next line will raise an exception
# temp.celsius = -300
