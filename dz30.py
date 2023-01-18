
class Table:
    def __init__(self, length, width, rad):
        self.__length = length
        self.__width = width
        self.__rad = rad


class Curcle(Table):
    def __init__(self, length, width, rad):
        super().__init__(length, width, rad)

    @staticmethod
    def area(rad):
        return 3.14 * rad ** 2


class Rectangle(Table):
    def __init__(self, length, width, rad):
        super().__init__(length, width, rad)

    @staticmethod
    def area(length, width):
        return length * width


class Square(Table):
    def __init__(self, length, width, rad):
        super().__init__(length, width, rad)

    @staticmethod
    def area(length):
        return length ** 2


print(Curcle.area(20))
print(Rectangle.area(10, 20))
print(Square.area(20))
