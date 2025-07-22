class Square:
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size ** 2

    def __eq__(self, other):
        return self.area() == other.area()

    def __ne__(self, other):
        return self.area() != other.area()

    def __lt__(self, other):
        return self.area() < other.area()

    def __le__(self, other):
        return self.area() <= other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __ge__(self, other):
        return self.area() >= other.area()

s1 = Square(4.7)
print("Area s1:", s1.area())
s2 = Square(2)
print("Area s2:", s2.area())
s3 = Square(67)
print("Area s3:", s3.area())
print("s1 == s2:", s1 == s2)
print("s1 < s2:", s1 < s2)
print("s3 <= s1:", s3 <= s1)