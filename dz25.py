class Book:
    name = 'name'
    year = '00.00.0000'
    publisher = 'publisher'
    genre = 'genre'
    author = 'author'
    price = 'price'

    def print_info(self):
        print('Сведения о книге'.center(40, '-'))
        print(f' Название: {self.name}\n Год издания: {self.year}\n Издатель: {self.publisher}\n '
              f'Жанр: {self.genre}\n Автор: {self.author}\n Стоимость: {self.price}')
        print('-'*40)

    def input_info(self, name, year, publisher, genre, author, price):
        self.name = name
        self.year = year
        self.publisher = publisher
        self.genre = genre
        self.author = author
        self.price = price

    def set_name(self, name):
        if isinstance(name, str):
            self.name = name

    def get_name(self):
        return self.name

    def set_year(self, year):
        if isinstance(year, str):
            self.year = year

    def get_year(self):
        return self.year

    def set_publisher(self, publisher):
        if isinstance(publisher, str):
            self.publisher = publisher

    def get_publisher(self):
        return self.publisher

    def set_genre(self, genre):
        if isinstance(genre, str):
            self.genre = genre

    def get_genre(self):
        return self.genre

    def set_author(self, author):
        if isinstance(author, str):
            self.author = author

    def get_author(self):
        return self.author

    def set_price(self, price):
        if isinstance(price, str):
            self.price = price

    def get_price(self):
        return self.price


b1 = Book()
b1.print_info()
b1.input_info('...', '...', '...', '...', 'А.С.Пушкин', '100 руб')
b1.print_info()
b1.set_author('Л.Н.Толстой')
print(b1.get_author())
print(b1.get_year())
