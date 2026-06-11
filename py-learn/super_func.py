import math

class Shape:
    def __init__(self, color, filled):
        self.color = color
        self.filled = filled

    def describe(self):
        print(f"It is {self.color} and {'filled' if self.filled else 'not filled'}.")


class Circle(Shape):
    def __init__(self, color, filled, radius):
        super().__init__(color, filled)
        self.radius = radius
    def describe(self):
        super().describe()
        print(f"It is a circle with area of  {round(math.pi * self.radius ** 2, 2)}.")


class Square(Shape):
    def __init__(self, color, filled, width):
        super().__init__(color, filled)
        self.width = width


class Triangle(Shape):
    def __init__(self, color, filled, width, height):
        super().__init__(color, filled)
        self.width = width
        self.height = height


circle = Circle("red", True, 5)
square = Square("blue", False, 10)
triangle = Triangle("green", True, 8, 6)

# print(circle.color)
# print(square.filled)
# print(triangle.width)
# print(triangle.height)

circle.describe()
square.describe()
triangle.describe()
