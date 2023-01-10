class Rectangle:
    def __init__(self, x, y):
        self.x = self.y = 0
        if Rectangle.__check_value(x) and Rectangle.__check_value(y):
            self.__x = x
            print('Ширина прямоугольника: ', self.__x)
            self.__y = y
            print('Длина прямоугольника: ', self.__y)

    def __check_value(z):
        if isinstance(z, float) or isinstance(z, int):
            return True
        return False

    def set_coord(self, x, y):
        if Rectangle.__check_value(x) and Rectangle.__check_value(y):
            self.__x = x
            self.__y = y
        else:
            print('Стороны должны являться численными значениями')

    def get_s_rectangle(self, x, y):
        print('Площадь прямоугольника: ', self.__x * self.__y)

    def get_p_rectangle(self, x, y):
        print('Площадь прямоугольника: ', (self.__x + self.__y) * 2)

    def get_gipp_rectangle(self, x, y):
        print('Площадь прямоугольника: ', ((self.__x ** 2 + self.__y ** 2) ** 0.5).__round__(2))

    def print_rectangle(self, x, y):
        for i in range(self.__x):
            for j in range(self.__y):
                print('*', end='')
            print()


r1 = Rectangle(3, 9)
r1.get_s_rectangle(r1.x, r1.y)
r1.get_p_rectangle(r1.x, r1.y)
r1.get_gipp_rectangle(r1.x, r1.y)
r1.print_rectangle(r1.x, r1.y)
