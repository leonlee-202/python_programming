class Square:
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        if size > 0:
            print("Square is valid")
        self.__size = size

s = Square(4)
print()
