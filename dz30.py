from math import pi


class Table:
    def __init__(self, width=None, length=None, rad=None):
        if rad is None:
            if length is None:
                self._width = self._length = width
            else:
                self._width = width
                self._length = length
        else:
            self._rad = rad

    def calc_area(self):
        raise NotImplementedError('')


class Curcle(Table):
    def calc_area(self):
        return round(pi * self._rad ** 2, 2)


class Rectangle(Table):
    def calc_area(self):
        return self._width * self._length


table = Rectangle(20)
print(table.__dict__)
print(table.calc_area())

table1 = Curcle(12, 34, 20)
print(table1.__dict__)
print(table1.calc_area())

table2 = Rectangle(20, 10)
print(table2.__dict__)
print(table2.calc_area())