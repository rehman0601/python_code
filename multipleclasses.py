class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

# Test the classes
rectangle = Rectangle(4, 5)
square = Square(4)

print(f"Rectangle area: {rectangle.area()}")
print(f"Square area: {square.area()}")
