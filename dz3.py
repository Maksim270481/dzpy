#1 номер
a = int(input('Введите начало диапозона: '))
b = int(input('Введите конец диапозона: '))
while a < b:
    if a % 2 != 0:
        print(a)
    a += 1
while b < a:
    if b % 2 != 0:
        print(b)
    b += 1






