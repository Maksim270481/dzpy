class Auto:
    def __init__(self, name, year, manufacturer, mosh, color, price):
        self.name = name
        self.year = year
        self.manufacturer = manufacturer
        self.mosh = mosh
        self.color = color
        self.price = price

    @staticmethod
    def verif_name(name):
        if not isinstance(name, str):
            raise TypeError('Название модели может принимать только строчные символы.')

    @staticmethod
    def verif_year(yr):
        if not isinstance(yr, int):
            raise TypeError('Год выпуска может принимать только числоые значения.')

    @staticmethod
    def verif_manufacturer(mn):
        if not isinstance(mn, str):
            raise TypeError('Название производителя может принимать только строчные символы.')

    @staticmethod
    def verif_mosh(mh):
        if not isinstance(mh, str):
            raise TypeError('Значение мощности может принимать только строчные символы.')

    @staticmethod
    def verif_color(color):
        if not isinstance(color, str):
            raise TypeError('Цвет машины может принимать только строчные символы.')

    @staticmethod
    def verif_price(price):
        if not isinstance(price, int):
            raise TypeError('Стоимость автомобиля может принимать только числоые значения.')

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.verif_name(name)
        self.__name = name

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year):
        self.verif_year(year)
        self.__year = year

    @property
    def manufacturer(self):
        return self.__manufacturer

    @manufacturer.setter
    def manufacturer(self, manufacturer):
        self.verif_manufacturer(manufacturer)
        self.__manufacturer = manufacturer

    @property
    def mosh(self):
        return self.__mosh

    @mosh.setter
    def mosh(self, mosh):
        self.verif_mosh(mosh)
        self.__mosh = mosh

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        self.verif_color(color)
        self.__color = color

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        self.verif_price(price)
        self.__price = price


machine = Auto('X7 M50i', 2021, 'BMW', '530 л.с.', 'white', 10790000)
print('========== Данные автомобиля: ==========')
print(f'Название модели: {machine.name}')
print(f'Год выпуска: {machine.year}')
print(f'Производитель: {machine.manufacturer}')
print(f'Мощность двигателя: {machine.mosh}')
print(f'Цвет: {machine.color}')
print(f'Цена: {machine.price}')
print('='*40)
