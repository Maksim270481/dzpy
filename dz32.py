import random


class Cat:
    def __init__(self, name, pol):
        self.name = name
        self.pol = pol

    def __str__(self):
        if self.pol == 'M':
            return f'{self.name} is good boy!!!'
        elif self.pol == 'F':
            return f'{self.name} is good girl!!!'
        else:
            return f'{self.name} is good Kitty!!!'

    def __repr__(self):
        return f'Cat(name="{self.name}", sex="{self.pol}")'

    def __add__(self, other):
        if self.pol != other.pol:
            return [Cat('No name', random.choice(['M', 'F'])) for _ in range(1, random.randint(2, 7))]
        else:
            return 'Types are not support!'


c1 = Cat('Tom', 'M')
print(c1)
c2 = Cat('Elsa', 'F')
print(c1 + c2)