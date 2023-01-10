class Ploshad:
    __count = 0

    @staticmethod
    def get_count():
        return Ploshad.__count

    @staticmethod
    def geron(a, b, c):
        Ploshad.__count += 1
        return (a + b + c) / 2

    @staticmethod
    def ov(a, b):
        Ploshad.__count += 1
        return a * b / 2

    @staticmethod
    def square(a):
        Ploshad.__count += 1
        return a ** 2

    @staticmethod
    def rectangle(a, b):
        Ploshad.__count += 1
        return a * b

print('Площадь по формуле Герона: ', Ploshad.geron(3, 4, 5))
print('Площадь треугольника через основание и высоту: ', Ploshad.ov(6, 7))
print('Площадь квадрата: ', Ploshad.square(7))
print('Площадь прямоугольника: ', Ploshad.rectangle(2, 6))
print('Колисчество вызова методов: ', Ploshad.get_count())