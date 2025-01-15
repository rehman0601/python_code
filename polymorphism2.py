class Circle:
    def draw(self):
        print("Drawing a circle")

class Triangle:
    def draw(self):
        print("Drawing a triangle")

class Rectangle:
    def draw(self):
        print("Drawing a rectangle")

# Test polymorphism
shapes = [Circle(), Triangle(), Rectangle()]
for shape in shapes:
    shape.draw()
