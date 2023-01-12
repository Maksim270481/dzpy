# -------------- det and set------------

# class Acount:
#     rate_usd = 0.013
#     rate_eur = 0.011
#     suffix = 'RUB'
#     suffix_usd = 'USD'
#     suffix_eur = 'EUR'
#
#     def __init__(self, num, surname, precent, value=0):
#         self.__num = num
#         self.__surname = surname
#         self.__precent = precent
#         self.__value = value
#         print(f'счет #{self.__num}, принадлежащий {self.__surname} был открыт.')
#         print('-' * 50)
#
#     def __del__(self):
#         print('*' * 50)
#         print(f'счет #{self.__num} на фамилию {self.__surname} был зыкрыт.')
#
#     def set_num(self, num):
#         self.__num = num
#
#     def get_num(self):
#         return self.__num
#
#     def set_surname(self, surname):
#         self.__surname = surname
#
#     def get_surname(self):
#         return self.__surname
#
#     def set_precent(self, precent):
#         self.__precent = precent
#
#     def get_precent(self):
#         return self.__precent
#
#     def set_value(self, value):
#         self.__value = value
#
#     def get_value(self):
#         return self.__value
#
#     def print_balance(self):
#         print(f'текущий баланс {self.__value} {Acount.suffix}')
#
#     def print_info(self):
#         print('информация о счете')
#         print('-' * 20)
#         print(f'#{self.__num}')
#         print(f'владелец: {self.__surname}')
#         self.print_balance()
#         print(f'проценты: {self.__precent:.0%}')
#         print('-' * 20)
#
#     @staticmethod
#     def convert(value, rate):
#         return value * rate
#
#     def convert_to_usd(self):
#         usd_val = Acount.convert(self.__value, Acount.rate_usd)
#         print(f'состояние счета {usd_val} {Acount.suffix_usd}')
#
#     def convert_to_eur(self):
#         usd_val = Acount.convert(self.__value, Acount.rate_eur)
#         print(f'состояние счета {usd_val} {Acount.suffix_eur}')
#
#     @classmethod
#     def set_usd_rate(cls, rate):
#         cls.rate_usd = rate
#
#     @classmethod
#     def set_eur_rate(cls, rate):
#         cls.rate_eur = rate
#
#     def edit_owner(self, surname):
#         self.__surname = surname
#
#     def add_precents(self):
#         self.__value += self.__value * self.__precent
#         print('Проценты были начислены!')
#         self.print_balance()
#
#     def withdraw_money(self, val):
#         if val > self.__value:
#             print(f'к сожалению у вас нет {val} {Acount.suffix}')
#         else:
#             self.__value -= val
#         print(self.print_balance())
#
#     def add_money(self, val):
#         self.__value += val
#         print(f'{val} {Acount.suffix} было успешно добавлено!')
#         self.print_balance()
#
#
# acc = Acount('12345', 'Долгих', 0.03, 1000)
# acc.print_info()
# acc.convert_to_usd()
# acc.convert_to_eur()
#
# Acount.set_usd_rate(2)
# acc.convert_to_usd()
# print()
# acc.withdraw_money(3000)
# print()
# acc.add_money(5000)
# print()
# acc.withdraw_money(3000)


# -------------- @property ------------

class Acount:
    rate_usd = 0.013
    rate_eur = 0.011
    suffix = 'RUB'
    suffix_usd = 'USD'
    suffix_eur = 'EUR'

    def __init__(self, num, surname, precent, value=0):
        self.__num = num
        self.__surname = surname
        self.__precent = precent
        self.__value = value
        print(f'счет #{self.num}, принадлежащий {self.surname} был открыт.')
        print('-' * 50)

    def __del__(self):
        print('*' * 50)
        print(f'счет #{self.num} на фамилию {self.surname} был зыкрыт.')

    def print_balance(self):
        print(f'текущий баланс {self.value} {Acount.suffix}')

    def print_info(self):
        print('информация о счете')
        print('-' * 20)
        print(f'#{self.num}')
        print(f'владелец: {self.surname}')
        self.print_balance()
        print(f'проценты: {self.precent:.0%}')
        print('-' * 20)

    @property
    def num(self):
        return self.__num

    @num.setter
    def num(self, num):
        self.__num = num

    @num.deleter
    def num(self):
        del self.__num

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, surname):
        self.__surname = surname

    @surname.deleter
    def surname(self):
        del self.__surname

    @staticmethod
    def convert(value, rate):
        return value * rate

    @property
    def precent(self):
        return self.__precent

    @precent.setter
    def precent(self, precent):
        self.__precent = precent

    @precent.deleter
    def precent(self):
        del self.__precent

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value

    @value.deleter
    def value(self):
        del self.__value

    def convert_to_usd(self):
        usd_val = Acount.convert(self.value, Acount.rate_usd)
        print(f'состояние счета {usd_val} {Acount.suffix_usd}')

    def convert_to_eur(self):
        usd_val = Acount.convert(self.value, Acount.rate_eur)
        print(f'состояние счета {usd_val} {Acount.suffix_eur}')

    @classmethod
    def set_usd_rate(cls, rate):
        cls.rate_usd = rate

    @classmethod
    def set_eur_rate(cls, rate):
        cls.rate_eur = rate

    def edit_owner(self, surname):
        self.surname = surname

    def add_precents(self):
        self.value += self.value * self.precent
        print('Проценты были начислены!')
        self.print_balance()

    def withdraw_money(self, val):
        if val > self.value:
            print(f'к сожалению у вас нет {val} {Acount.suffix}')
        else:
            self.value -= val
        print(self.print_balance())

    def add_money(self, val):
        self.value += val
        print(f'{val} {Acount.suffix} было успешно добавлено!')
        self.print_balance()


acc = Acount('12345', 'Долгих', 0.03, 1000)
acc.print_info()
acc.convert_to_usd()
acc.convert_to_eur()

Acount.set_usd_rate(2)
acc.convert_to_usd()
print()
acc.withdraw_money(3000)
print()
acc.add_money(5000)
print()
acc.withdraw_money(3000)
