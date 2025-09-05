class Rectangle:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

r1 = Rectangle()
print("Rectangle 1 - width:", r1.width, "height:", r1.height)

r2 = Rectangle(4, 5)
print("Rectangle 2 - width:", r2.width, "height:", r2.height)

r2.width = 10
r2.height = 7
print("Updated Rectangle 2 - width:", r2.width, "height:", r2.height)


