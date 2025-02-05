class Shape:
    def draw(self):
        pass

class Circle(Shape):
    def draw(self):
        print("Drawing a Circle")

class Square(Shape):
    def draw(self):
        print("Drawing a Square")

class Triangle(Shape):
    def draw(self):
        print("Drawing a Triangle")

# Create a list of shapes and call draw() on each
shapes = [Circle(), Square(), Triangle()]
for shape in shapes:
    shape.draw()
