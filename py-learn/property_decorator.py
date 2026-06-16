class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return f"{self._width:.1f} cm²"

    @property
    def height(self):
        return f"{self._height:.1f} cm²"

    @width.setter
    def width(self, value):
        if value > 0:
            self._width = value
        else:
            print("Width must greater than 0.")

    @height.setter
    def height(self, value):
        if value > 0:
            self._height = value
        else:
            print("Height must greater than 0.")

    @width.deleter
    def width(self):
        del self._width
        print("Width has been deleted.")

    @height.deleter
    def height(self):
        del self._height
        print("Height has been deleted.")


rectangle = Rectangle(5, 10)
rectangle.width = 25
rectangle.height = 12
print(rectangle.width)
print(rectangle.height)
del rectangle.width
del rectangle.height
