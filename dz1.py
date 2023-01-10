# # пятизначное число ...
#
#
# num =int(input('Введите пятизначное число: '))
# e = (num % 10)
# num = num // 10
# d = (num % 10)
# num = num // 10
# c = (num % 10)
# num = num // 10
# b = (num % 10)
# num = num // 10
# a = num
# print('Произвидение цифр числа ' + str(a) + str(b) + str(c) + str(d) + str(e) + ' : ' + str(a * b * c * d * e))
# print('Среднее арифмитическое: ' + str((a + b + c + d + e)//5))
#
#
# # четное нечетное ...
#
#
# a = int(input('Ввкдите число: '))
# if a % 2 == 0:
#     print('Число',a,'-Четное')
# else:
#     print('Число',a,'- Нечетное')
#
#
# #копеек
#
#
num =int(input('Введите кол-во копеек(1 - 99): '))
a = (num % 10)
if a == 1 :
    print(1, 'копейка')

elif 1 < a < 5 :
    print(num, 'копейки')
elif 4 < a < 10 :
    print(num, 'копеек')
elif a == 0 :
    print(num, 'копеек')
else:
    print('Вы указали не верное число')

#
# #калькулятор
#
#
# print('Перечень операций:')
# print('1 - "r" - применяет унарный минус к операнду (используется только к первому числу)')
# print('2 - "+" - сложение')
# print('3 - "-" - вычитание')
# print('4 - "/" - деление')
# print('5 - "*" - умножение')
# print('6 - "%" - деление по модулю (остаток от деления)')
# print('7 - "<" - минимальное из двух чисел')
# print('8 - ">" - максимальное из двух чисел')
# op = int(input('Выберите операцию: '))
# a = int(input('Введите первое число:  '))
# b = int(input('Введите второе число:  '))
# if op == 1:
#     print(a*(-1))
# elif op == 2:
#     print(a+b)
# elif op == 3:
#     print(a-b)
# elif op == 4:
#     if b!=0:
#         print(a / b)
#     else:
#         print('На ноль делить нельзя!!!')
# elif op == 5:
#     print(a*b)
# elif op == 6:
#     print(a%b)
# elif op == 7:
#     if a<b:
#         print(a)
#     elif b<a:
#         print(b)
#     else:
#         print('Числа равны')
# elif op == 8:
#     if a>b:
#         print(a)
#     elif b>a:
#         print(b)
#     else:
#         print('Числа равны')






